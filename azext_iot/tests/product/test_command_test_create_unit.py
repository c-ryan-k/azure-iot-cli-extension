# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import unittest
import mock
from knack.util import CLIError
from azext_iot.product.test.command_tests import create
from azext_iot.product.shared import BadgeType, AttestationType, DeviceType, TaskType


class TestTestCreateUnit(unittest.TestCase):
    def __init__(self, test_case):
        self.product_id = "b70a3805-5800-4272-93f2-1b4d0150f683"
        super(TestTestCreateUnit, self).__init__(test_case)

    def test_create_with_no_parameters_fails(self):
        with self.assertRaises(CLIError):
            create(self)

    def test_create_with_x509_and_no_certificate_fails(self):
        with self.assertRaises(CLIError) as context:
            create(self, attestation_type=AttestationType.x509.value)

        self.assertEqual(
            "If attestation type is x509, certificate path is required",
            str(context.exception),
        )

    def test_create_with_tpm_and_no_endorsement_key_fails(self):
        with self.assertRaises(CLIError) as context:
            create(self, attestation_type=AttestationType.tpm.value)

        self.assertEqual(
            "If attestation type is TPM, endorsement key is required",
            str(context.exception),
        )

    def test_edge_module_without_connection_string_fails(self):
        with self.assertRaises(CLIError) as context:
            create(
                self,
                attestation_type=AttestationType.connectionString.value,
                badge_type=BadgeType.IotEdgeCompatible.value,
            )

        self.assertEqual(
            "Connection string is required for Edge Compatible modules testing",
            str(context.exception),
        )

    def test_connection_string_for_pnp_fails(self):
        with self.assertRaises(CLIError) as context:
            create(
                self,
                attestation_type=AttestationType.connectionString.value,
                badge_type=BadgeType.Pnp.value,
                models="./stuff",
            )

        self.assertEqual(
            "Connection string is only available for Edge Compatible modules testing",
            str(context.exception),
        )

    def test_connection_string_for_iot_device_fails(self):
        with self.assertRaises(CLIError) as context:
            create(self, attestation_type=AttestationType.connectionString.value)

        self.assertEqual(
            "Connection string is only available for Edge Compatible modules testing",
            str(context.exception),
        )

    def test_create_with_pnp_and_no_models_fails(self):
        with self.assertRaises(CLIError) as context:
            create(self, badge_type=BadgeType.Pnp.value)

        self.assertEqual(
            "If badge type is Pnp, models is required", str(context.exception)
        )

    def test_create_with_missing_device_type_fails(self):
        with self.assertRaises(CLIError) as context:
            create(
                self,
                attestation_type=AttestationType.symmetricKey.value,
                product_id=self.product_id,
                badge_type=BadgeType.Pnp.value,
                models="models_folder",
            )

        self.assertEqual(
            "If configuration file is not specified, attestation and device definition parameters must be specified",
            str(context.exception),
        )

    def test_create_with_missing_product_id_fails(self):
        with self.assertRaises(CLIError) as context:
            create(
                self,
                attestation_type=AttestationType.symmetricKey.value,
                device_type=DeviceType.DevKit.value,
                badge_type=BadgeType.Pnp.value,
                models="models_folder",
            )

        self.assertEqual(
            "If configuration file is not specified, attestation and device definition parameters must be specified",
            str(context.exception),
        )

    @mock.patch("azext_iot.product.test.command_tests._process_models_directory")
    @mock.patch("azext_iot.sdk.product.aicsapi.AICSAPI.create_device_test")
    def test_create_with_default_badge_type_doesnt_check_models(
        self, mock_service, mock_process_models
    ):
        create(
            self,
            attestation_type=AttestationType.symmetricKey.value,
            product_id=self.product_id,
            device_type=DeviceType.DevKit.value,
            models="models_folder",
        )

        mock_process_models.assert_not_called()
        mock_service.assert_called_with(
            provisioning=True,
            body={
                "validationType": "Certification",
                "productId": self.product_id,
                "deviceType": "DevKit",
                "provisioningConfiguration": {
                    "type": "SymmetricKey",
                    "symmetricKeyEnrollmentInformation": {},
                },
                "certificationBadgeConfigurations": [{"type": "IotDevice"}],
            },
        )

    @mock.patch("azext_iot.product.test.command_tests._process_models_directory")
    @mock.patch("azext_iot.sdk.product.aicsapi.AICSAPI.create_device_test")
    def test_create_with_pnp_badge_type_checks_models(
        self, mock_service, mock_process_models
    ):
        mock_process_models.return_value = [
            '{"@id":"model1"}',
            '{"@id":"model2"}',
            '{"@id":"model3"}',
        ]
        create(
            self,
            attestation_type=AttestationType.symmetricKey.value,
            product_id=self.product_id,
            device_type=DeviceType.DevKit.value,
            models="models_folder",
            badge_type=BadgeType.Pnp.value,
        )

        mock_process_models.assert_called_with("models_folder")
        mock_service.assert_called_with(
            provisioning=True,
            body={
                "validationType": "Certification",
                "productId": self.product_id,
                "deviceType": "DevKit",
                "provisioningConfiguration": {
                    "type": "SymmetricKey",
                    "symmetricKeyEnrollmentInformation": {},
                },
                "certificationBadgeConfigurations": [
                    {
                        "type": "Pnp",
                        "digitalTwinModelDefinitions": [
                            '{"@id":"model1"}',
                            '{"@id":"model2"}',
                            '{"@id":"model3"}',
                        ],
                    }
                ],
            },
        )

    @mock.patch("azext_iot.product.test.command_tests._read_certificate_from_file")
    @mock.patch("azext_iot.product.test.command_tests._process_models_directory")
    @mock.patch("azext_iot.sdk.product.aicsapi.AICSAPI.create_device_test")
    def test_create_with_cert_auth_reads_cert_file(
        self, mock_service, mock_process_models, mock_read_certificate
    ):
        mock_read_certificate.return_value = "MockBase64String"
        mock_process_models.return_value = [
            '{"@id":"model1"}',
            '{"@id":"model2"}',
            '{"@id":"model3"}',
        ]
        create(
            self,
            attestation_type=AttestationType.x509.value,
            product_id=self.product_id,
            device_type=DeviceType.DevKit.value,
            models="models_folder",
            badge_type=BadgeType.Pnp.value,
            certificate_path="mycertificate.cer",
        )

        mock_read_certificate.assert_called_with("mycertificate.cer")
        mock_process_models.assert_called_with("models_folder")
        mock_service.assert_called_with(
            provisioning=True,
            body={
                "validationType": "Certification",
                "productId": self.product_id,
                "deviceType": "DevKit",
                "provisioningConfiguration": {
                    "type": "X509",
                    "x509EnrollmentInformation": {
                        "base64EncodedX509Certificate": "MockBase64String"
                    },
                },
                "certificationBadgeConfigurations": [
                    {
                        "type": "Pnp",
                        "digitalTwinModelDefinitions": [
                            '{"@id":"model1"}',
                            '{"@id":"model2"}',
                            '{"@id":"model3"}',
                        ],
                    }
                ],
            },
        )

    @mock.patch("azext_iot.product.test.command_tests._read_certificate_from_file")
    @mock.patch("azext_iot.product.test.command_tests._process_models_directory")
    @mock.patch("azext_iot.sdk.product.aicsapi.AICSAPI.create_device_test")
    def test_create_with_tpm(
        self, mock_service, mock_process_models, mock_read_certificate
    ):
        mock_process_models.return_value = [
            '{"@id":"model1"}',
            '{"@id":"model2"}',
            '{"@id":"model3"}',
        ]
        create(
            self,
            attestation_type=AttestationType.tpm.value,
            endorsement_key="12345",
            product_id=self.product_id,
            device_type=DeviceType.DevKit.value,
            models="models_folder",
            badge_type=BadgeType.Pnp.value,
            certificate_path="mycertificate.cer",
        )

        mock_read_certificate.assert_not_called()
        mock_process_models.assert_called_with("models_folder")
        mock_service.assert_called_with(
            provisioning=True,
            body={
                "validationType": "Certification",
                "productId": self.product_id,
                "deviceType": "DevKit",
                "provisioningConfiguration": {
                    "type": "TPM",
                    "tpmEnrollmentInformation": {"endorsementKey": "12345"},
                },
                "certificationBadgeConfigurations": [
                    {
                        "type": "Pnp",
                        "digitalTwinModelDefinitions": [
                            '{"@id":"model1"}',
                            '{"@id":"model2"}',
                            '{"@id":"model3"}',
                        ],
                    }
                ],
            },
        )

    @mock.patch("azext_iot.sdk.product.aicsapi.AICSAPI.create_device_test")
    @mock.patch("azext_iot.product.test.command_tests._create_from_file")
    def test_create_with_configuration_file(self, mock_from_file, mock_sdk_create):
        mock_file_data = {"mock": "data"}
        mock_from_file.return_value = mock_file_data
        create(self, configuration_file="somefile")
        mock_from_file.assert_called_with("somefile")
        mock_sdk_create.assert_called_with(provisioning=True, body=mock_file_data)

    @mock.patch("azext_iot.product.test.command_test_tasks.create")
    @mock.patch("azext_iot.sdk.product.aicsapi.AICSAPI.create_device_test")
    @mock.patch("azext_iot.product.test.command_tests._process_models_directory")
    def test_create_with_generate_tests(
        self, mock_process_models, mock_service, mock_tasks_create,
    ):
        mock_process_models.return_value = [
            '{"@id":"model1"}',
            '{"@id":"model2"}',
            '{"@id":"model3"}',
        ]
        test_data = mock.Mock()
        test_data.id = "test123"
        mock_service.return_value = test_data

        create(
            self,
            attestation_type=AttestationType.tpm.value,
            endorsement_key="12345",
            product_id=self.product_id,
            device_type=DeviceType.DevKit.value,
            models="models_folder",
            badge_type=BadgeType.Pnp.value,
            generate_test_cases=True
        )

        mock_process_models.assert_called_with("models_folder")
        mock_service.assert_called_with(
            provisioning=True,
            body={
                "validationType": "Certification",
                "productId": self.product_id,
                "deviceType": "DevKit",
                "provisioningConfiguration": {
                    "type": "TPM",
                    "tpmEnrollmentInformation": {"endorsementKey": "12345"},
                },
                "certificationBadgeConfigurations": [
                    {
                        "type": "Pnp",
                        "digitalTwinModelDefinitions": [
                            '{"@id":"model1"}',
                            '{"@id":"model2"}',
                            '{"@id":"model3"}',
                        ],
                    }
                ],
            },
        )
        mock_tasks_create.assert_called_with(
            cmd=self,
            test_id="test123",
            task_type=TaskType.GenerateTestCases.value,
            wait=True,
            base_url=None
        )
