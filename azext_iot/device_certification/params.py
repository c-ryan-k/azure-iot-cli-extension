# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

"""
CLI parameter definitions.
"""

from azure.cli.core.commands.parameters import get_three_state_flag, get_enum_type
from azext_iot.device_certification.shared import BadgeType, TaskType

def load_device_certification_params(self, _):
    with self.argument_context('iot device-certification') as c:
        c.argument('test_id',
            options_list=['--test-id'],
            help='The Id of the Microsoft.Azure.IoT.TestKit.Models.DeviceTest',
            arg_group='IoT Device Certification'
        )
        c.argument(
            'badge_type',
            options_list=['--badge-type', '--bt'],
            help='The type of certification badge',
            arg_group='IoT Device Certification',
            arg_type=get_enum_type(BadgeType)
        )
        c.argument(
            'configuration_file',
            options_list=['--configuration_file', '--cf'],
            help='The file path for test case configuration JSON',
            arg_group='IoT Device Certification'
        )
    with self.argument_context('iot device-certification test') as c:
        c.argument('provisioning',
            options_list=['--provisioning'],
            help='Determines whether the service generates provisioning configuration. Only applies to SymmetricKey and ConnectionString provisioning types',
            arg_group='IoT Device Certification'
        )
        c.argument('configuration_file',
            options_list=['--configuration_file', '--cf'],
            help='Path to device test JSON file',
            arg_group='IoT Device Certification'
        )
    with self.argument_context('iot device-certification test search') as c:
        c.argument('product_id',
            options_list=['--product-id'],
            help='The submitted product id',
            arg_group='IoT Device Certification'
        )
        c.argument(
            'registration_id',
            options_list=['--registration-id'],
            help='The regstration Id for Device Provisioning Service',
            arg_group='IoT Device Certification'
        )
        c.argument(
            'certificate_name',
            options_list=['--certificate-name', '--cn'],
            help='The x509 Certificate Common Name (cn) used for Device Provisioning Service authentication'
        )
    with self.argument_context('iot device-certification test-task') as c:
        c.argument('task_id',
            options_list=['--task-id'],
            help='The Id of the Microsoft.Azure.IoT.TestKit.Models.DeviceTestTask',
            arg_group='IoT Device Certification'
        )
        c.argument('running',
            options_list=['--running'],
            help='Get the running tasks of a device test',
            arg_group='IoT Device Certification',
            arg_type=get_three_state_flag()
        )
        c.argument(
            'type',
            options_list=['--type', '-t'],
            help='The type of task for the device test',
            arg_group='IoT Device Certification',
            arg_type=get_enum_type(TaskType)
        )
    with self.argument_context('iot device-certification test-run') as c:
        c.argument('run_id',
            options_list=['--run-id'],
            help='The Id of a Microsoft.Azure.IoT.TestKit.Models.TestRun',
            arg_group='IoT Device Certification'
        )
        c.argument('latest',
            options_list=['--latest'],
            help='Retrieve the latest test runs',
            arg_group='IoT Device Certification',
            arg_type=get_three_state_flag()
        )
