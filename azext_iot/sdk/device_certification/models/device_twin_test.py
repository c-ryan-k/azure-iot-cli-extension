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


class DeviceTwinTest(Model):
    """DeviceTwinTest.

    :param desired_properties:
    :type desired_properties: str
    :param reported_properties:
    :type reported_properties: str
    :param validation_timeout:
    :type validation_timeout: int
    :param is_mandatory:
    :type is_mandatory: bool
    :param should_validate:
    :type should_validate: bool
    """

    _attribute_map = {
        'desired_properties': {'key': 'desiredProperties', 'type': 'str'},
        'reported_properties': {'key': 'reportedProperties', 'type': 'str'},
        'validation_timeout': {'key': 'validationTimeout', 'type': 'int'},
        'is_mandatory': {'key': 'isMandatory', 'type': 'bool'},
        'should_validate': {'key': 'shouldValidate', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(DeviceTwinTest, self).__init__(**kwargs)
        self.desired_properties = kwargs.get('desired_properties', None)
        self.reported_properties = kwargs.get('reported_properties', None)
        self.validation_timeout = kwargs.get('validation_timeout', None)
        self.is_mandatory = kwargs.get('is_mandatory', None)
        self.should_validate = kwargs.get('should_validate', None)
