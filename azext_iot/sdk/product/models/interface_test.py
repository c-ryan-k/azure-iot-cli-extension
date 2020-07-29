# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InterfaceTest(Model):
    """InterfaceTest.

    :param id:
    :type id: str
    :param is_mandatory:
    :type is_mandatory: bool
    :param should_validate:
    :type should_validate: bool
    :param component_name:
    :type component_name: str
    :param display_name:
    :type display_name: str
    :param resolution_source: Possible values include: 'Unknown',
     'GlobalRepository', 'PrivateRepository', 'UserUploads'
    :type resolution_source: str or ~product.models.enum
    :param property_tests:
    :type property_tests: list[~product.models.PropertyTest]
    :param command_tests:
    :type command_tests: list[~product.models.CommandTest]
    :param telemetry_tests:
    :type telemetry_tests: list[~product.models.TelemetryTest]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'should_validate': {'key': 'shouldValidate', 'type': 'bool'},
        'component_name': {'key': 'componentName', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'resolution_source': {'key': 'resolutionSource', 'type': 'str'},
        'property_tests': {'key': 'propertyTests', 'type': '[PropertyTest]'},
        'command_tests': {'key': 'commandTests', 'type': '[CommandTest]'},
        'telemetry_tests': {'key': 'telemetryTests', 'type': '[TelemetryTest]'},
    }

    def __init__(self, **kwargs):
        super(InterfaceTest, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.is_mandatory = kwargs.get('is_mandatory', None)
        self.should_validate = kwargs.get('should_validate', None)
        self.component_name = kwargs.get('component_name', None)
        self.display_name = kwargs.get('display_name', None)
        self.resolution_source = kwargs.get('resolution_source', None)
        self.property_tests = kwargs.get('property_tests', None)
        self.command_tests = kwargs.get('command_tests', None)
        self.telemetry_tests = kwargs.get('telemetry_tests', None)
