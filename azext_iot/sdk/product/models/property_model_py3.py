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


class PropertyModel(Model):
    """PropertyModel.

    :param supplemental_types:
    :type supplemental_types: list[str]
    :param schema:
    :type schema: object
    :param writable:
    :type writable: bool
    :param supplemental_properties:
    :type supplemental_properties: dict[str, object]
    :param name:
    :type name: str
    :param comment:
    :type comment: str
    :param display_name:
    :type display_name: dict[str, str]
    :param id:
    :type id: str
    :param description:
    :type description: dict[str, str]
    :param language_version:
    :type language_version: int
    """

    _attribute_map = {
        'supplemental_types': {'key': 'supplementalTypes', 'type': '[str]'},
        'schema': {'key': 'schema', 'type': 'object'},
        'writable': {'key': 'writable', 'type': 'bool'},
        'supplemental_properties': {'key': 'supplementalProperties', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'comment': {'key': 'comment', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': '{str}'},
        'id': {'key': 'id', 'type': 'str'},
        'description': {'key': 'description', 'type': '{str}'},
        'language_version': {'key': 'languageVersion', 'type': 'int'},
    }

    def __init__(self, *, supplemental_types=None, schema=None, writable: bool=None, supplemental_properties=None, name: str=None, comment: str=None, display_name=None, id: str=None, description=None, language_version: int=None, **kwargs) -> None:
        super(PropertyModel, self).__init__(**kwargs)
        self.supplemental_types = supplemental_types
        self.schema = schema
        self.writable = writable
        self.supplemental_properties = supplemental_properties
        self.name = name
        self.comment = comment
        self.display_name = display_name
        self.id = id
        self.description = description
        self.language_version = language_version
