# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import LiveScenarioTest
from azext_iot.product.shared import AttestationType


class TestTestUpdateInt(LiveScenarioTest):
    def __init__(
        self, test_case
    ):
        self.test_id = '9825514b-27e6-4563-8cd9-2b384f3ac10d'
        super(TestTestUpdateInt, self).__init__(test_case)

    def test_update_symmetric_key(self):
        # call the GET /deviceTest/{test_id}
        output = self.cmd(
            'iot product test update -t {} --at symmetricKey'.format(
                self.test_id,
            )
        ).get_output_in_json()

        assert output['id'] == self.test_id
        assert output['provisioningConfiguration']['type'] == AttestationType.symmetricKey
        assert output['provisioningConfiguration']['symmetricKeyEnrollmentInformation']
