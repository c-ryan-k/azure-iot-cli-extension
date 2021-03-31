# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import re
import pytest
import responses
import json
from knack.cli import CLIError
from azext_iot.operations import hub as subject
from azext_iot.tests.generators import generate_generic_id
from azext_iot.tests.conftest import mock_target

hub_name = "HUBNAME"
blob_container_uri = "https://example.com"
resource_group_name = "RESOURCEGROUP"
managed_identity = "EXAMPLEMANAGEDIDENTITY"
generic_result = json.dumps({"result": generate_generic_id()})

@pytest.fixture
def get_mgmt_client(mocker, fixture_cmd):
    from azure.mgmt.iothub import IotHubClient
    from azext_iot.digitaltwins.providers.auth import DigitalTwinAuthentication

    patched_get_raw_token = mocker.patch(
        "azure.cli.core._profile.Profile.get_raw_token"
    )
    patched_get_raw_token.return_value = (
        mocker.MagicMock(name="creds"),
        mocker.MagicMock(name="subscription"),
        mocker.MagicMock(name="tenant"),
    )

    patch = mocker.patch(
        "azext_iot._factory.iot_hub_service_factory"
    )
    patch.return_value = IotHubClient(
        credential=DigitalTwinAuthentication(
            fixture_cmd, "00000000-0000-0000-0000-000000000000"
        ),
        subscription_id="00000000-0000-0000-0000-000000000000",
    )

    return patch


class TestIoTHubDeviceIdentityExport(object):
    @pytest.fixture
    def service_client(self, mocked_response, get_mgmt_client):
        mocked_response.assert_all_requests_are_fired = False

        mocked_response.add(
            method=responses.POST,
            url=re.compile(
                "https://management.azure.com/subscriptions/(.*)/"
                "providers/Microsoft.Devices/IotHubs/{}/exportDevices".format(
                    hub_name
                )
            ),
            body=generic_result,
            status=200,
            content_type="application/json",
            match_querystring=False,
        )

        yield mocked_response

    @pytest.mark.parametrize(
        "blob_container_uri, include_keys, storage_authentication_type, identity, resource_group_name",
        [
            (blob_container_uri, False, None, None, None),
            (blob_container_uri, False, 'identity', None, None),
            (blob_container_uri, False, 'identity', '[system]', None),
            (blob_container_uri, False, 'identity', 'managed_identity', None),
            (blob_container_uri, False, 'key', None, None),
            (blob_container_uri, False, 'key', '[system]', None),
            (blob_container_uri, False, 'identity', 'managed_identity', None),
            (blob_container_uri, False, None, None, resource_group_name),
        ]
    )
    def test_device_identity_export(self, fixture_cmd, service_client, blob_container_uri, include_keys, storage_authentication_type, identity, resource_group_name):
        result = subject.iot_device_export(
            cmd=fixture_cmd,
            hub_name=hub_name,
            blob_container_uri=blob_container_uri,
            include_keys=include_keys,
            storage_authentication_type=storage_authentication_type,
            identity=identity,
            resource_group_name=resource_group_name,
        )
        # test = service_client.calls
        # import pdb; pdb.set_trace()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"The result in the test is {result.__dict__}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"payload is {result['payload']}")
        print(f"Number of calls {len(service_client.calls)}")

        request = service_client.calls[0].request
        request_body = json.loads(request.body)
        assert request_body["exportBlobContainerUri"] == blob_container_uri
        assert request_body["excludeKeys"] == (not include_keys)
        assert request_body["authenticationType"] == storage_authentication_type
        if identity not in (None, "[system]"):
            assert request_body["authenticationType"] == storage_authentication_type

        assert result["payload"] == json.loads(generic_result)


class TestIoTHubDeviceIdentityImport(object):
    @pytest.fixture
    def service_client(self, mocked_response, fixture_ghcs, fixture_sas, request):
        mocked_response.assert_all_requests_are_fired = False

        mocked_response.add(
            method=responses.POST,
            content_type="application/json",
            url=re.compile(
                "https://management.azure.com/subscriptions/(.*)/"
                "providers/Microsoft.Devices/IotHubs/{}/exportDevices".format(
                    hub_name
                )
            ),
            status=200,
            match_querystring=False,
            body=json.dumps(generic_result),
        )

        yield mocked_response

    @pytest.mark.parametrize(
        "input_blob_container_uri, output_blob_container_uri, storage_authentication_type, identity, resource_group_name",
        [
            (blob_container_uri, blob_container_uri, None, None, None),
            (blob_container_uri, blob_container_uri, 'identity', None, None),
            (blob_container_uri, blob_container_uri, 'identity', '[system]', None),
            (blob_container_uri, blob_container_uri, 'identity', 'managed_identity', None),
            (blob_container_uri, blob_container_uri, 'key', None, None),
            (blob_container_uri, blob_container_uri, 'key', '[system]', None),
            (blob_container_uri, blob_container_uri, 'identity', 'managed_identity', None),
            (blob_container_uri, blob_container_uri, None, None, resource_group_name),
        ]
    )
    def test_device_identity_import(self, fixture_cmd, service_client, input_blob_container_uri, output_blob_container_uri, storage_authentication_type, identity, resource_group_name):
        result = subject.iot_device_import(
            cmd=fixture_cmd,
            hub_name=hub_name,
            input_blob_container_uri=input_blob_container_uri,
            output_blob_container_uri=output_blob_container_uri,
            storage_authentication_type=storage_authentication_type,
            identity=identity,
            resource_group_name=resource_group_name,
        )
        print(len(service_client.calls))
        request = service_client.calls[0].request
        request_body = json.loads(request.body)
        assert request_body["exportBlobContainerUri"] == blob_container_uri
        assert request_body["exportBlobContainerUri"] == blob_container_uri
        assert request_body["authenticationType"] == storage_authentication_type
        if identity not in ("", "[system]"):
            assert request_body["authenticationType"] == storage_authentication_type

        assert result == json.loads(generic_result)