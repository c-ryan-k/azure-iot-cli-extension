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


class InterfaceDefinitionSnapshot(Model):
    """InterfaceDefinitionSnapshot.

    :param interface_id:
    :type interface_id: str
    :param content:
    :type content: str
    :param resolution_source: Possible values include: 'Unknown',
     'GlobalRepository', 'PrivateRepository', 'UserUploads'
    :type resolution_source: str or ~device_certification.models.enum
    """

    _attribute_map = {
        'interface_id': {'key': 'interfaceId', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'resolution_source': {'key': 'resolutionSource', 'type': 'str'},
    }

    def __init__(self, *, interface_id: str=None, content: str=None, resolution_source=None, **kwargs) -> None:
        super(InterfaceDefinitionSnapshot, self).__init__(**kwargs)
        self.interface_id = interface_id
        self.content = content
        self.resolution_source = resolution_source
