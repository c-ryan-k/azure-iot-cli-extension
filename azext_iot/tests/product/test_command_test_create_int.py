# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from . import AICSLiveScenarioTest
from azext_iot.product.shared import AttestationType, BadgeType, DeviceType
from uuid import uuid4


class TestTestCreateInt(AICSLiveScenarioTest):
    def __init__(self, test_case):
        self.product_id = str(uuid4())
        super(TestTestCreateInt, self).__init__(test_case)

    def test_create_symmetric_key(self):
        device_type = DeviceType.DevKit.value
        attestation_type = AttestationType.symmetricKey.value
        badge_type = BadgeType.IotDevice.value

        # call the POST /deviceTest
        output = self.cmd(
            "iot product test create -p {} --dt {} --at {} --bt {} --base-url {}".format(
                self.product_id,
                device_type,
                attestation_type,
                badge_type,
                self.kwargs["BASE_URL"],
            )
        ).get_output_in_json()

        assert output["productId"] == self.product_id
        assert output["deviceType"].lower() == device_type.lower()
        assert (
            output["provisioningConfiguration"]["type"].lower()
            == attestation_type.lower()
        )
        # assert service created symmetric key info
        assert output["provisioningConfiguration"]["symmetricKeyEnrollmentInformation"][
            "primaryKey"
        ]
