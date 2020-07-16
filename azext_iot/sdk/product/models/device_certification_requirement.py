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


class DeviceCertificationRequirement(Model):
    """DeviceCertificationRequirement.

    :param badge_type: Possible values include: 'IotDevice', 'Pnp',
     'IotEdgeCompatible'
    :type badge_type: str or ~product.models.enum
    :param provisioning_requirement:
    :type provisioning_requirement:
     ~product.models.DeviceCertificationProvisioningRequirement
    """

    _attribute_map = {
        'badge_type': {'key': 'badgeType', 'type': 'str'},
        'provisioning_requirement': {'key': 'provisioningRequirement', 'type': 'DeviceCertificationProvisioningRequirement'},
    }

    def __init__(self, **kwargs):
        super(DeviceCertificationRequirement, self).__init__(**kwargs)
        self.badge_type = kwargs.get('badge_type', None)
        self.provisioning_requirement = kwargs.get('provisioning_requirement', None)
