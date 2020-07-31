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


class DeviceTest(Model):
    """A DeviceTest contains basic information of a testing device and the
    provisioning
    information of that device in AICS's managed IoT Hubs.

    :param id: Id of a Microsoft.Azure.IoT.TestKit.Models.DeviceTest. It is
     generated by the service.
    :type id: str
    :param validation_type:
     Microsoft.Azure.IoT.TestKit.Shared.Models.ValidationType of a
     Microsoft.Azure.IoT.TestKit.Models.DeviceTest. Possible values include:
     'Certification'
    :type validation_type: str or ~product.models.enum
    :param product_id: Product Id of the testing device in product service. In
     CLI scenario, this can be null.
    :type product_id: str
    :param device_type: Microsoft.Azure.IoT.TestKit.Shared.Models.DeviceType
     of the testing device. Possible values include: 'FinishedProduct',
     'DevKit'
    :type device_type: str or ~product.models.enum
    :param provisioning_configuration:
    :type provisioning_configuration:
     ~product.models.ProvisioningConfiguration
    :param certification_badge_configurations: Certification badge
     configurations
    :type certification_badge_configurations: list[object]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'validation_type': {'key': 'validationType', 'type': 'str'},
        'product_id': {'key': 'productId', 'type': 'str'},
        'device_type': {'key': 'deviceType', 'type': 'str'},
        'provisioning_configuration': {'key': 'provisioningConfiguration', 'type': 'ProvisioningConfiguration'},
        'certification_badge_configurations': {'key': 'certificationBadgeConfigurations', 'type': '[object]'},
    }

    def __init__(self, *, id: str=None, validation_type=None, product_id: str=None, device_type=None, provisioning_configuration=None, certification_badge_configurations=None, **kwargs) -> None:
        super(DeviceTest, self).__init__(**kwargs)
        self.id = id
        self.validation_type = validation_type
        self.product_id = product_id
        self.device_type = device_type
        self.provisioning_configuration = provisioning_configuration
        self.certification_badge_configurations = certification_badge_configurations
