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


class DigitalTwinsEndpointResourceProperties(Model):
    """Properties related to Digital Twins Endpoint.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ServiceBus, EventHub, EventGrid

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar provisioning_state: The provisioning state. Possible values include:
     'Provisioning', 'Deleting', 'Succeeded', 'Failed', 'Canceled', 'Deleted',
     'Warning', 'Suspending', 'Restoring', 'Moving', 'Disabled'
    :vartype provisioning_state: str or
     ~azure.mgmt.digitaltwins.models.EndpointProvisioningState
    :ivar created_time: Time when the Endpoint was added to
     DigitalTwinsInstance.
    :vartype created_time: datetime
    :param dead_letter_secret: Dead letter storage secret. Will be obfuscated
     during read.
    :type dead_letter_secret: str
    :param endpoint_type: Required. Constant filled by server.
    :type endpoint_type: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'created_time': {'readonly': True},
        'endpoint_type': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'created_time': {'key': 'createdTime', 'type': 'iso-8601'},
        'dead_letter_secret': {'key': 'deadLetterSecret', 'type': 'str'},
        'endpoint_type': {'key': 'endpointType', 'type': 'str'},
    }

    _subtype_map = {
        'endpoint_type': {'ServiceBus': 'ServiceBus', 'EventHub': 'EventHub', 'EventGrid': 'EventGrid'}
    }

    def __init__(self, **kwargs):
        super(DigitalTwinsEndpointResourceProperties, self).__init__(**kwargs)
        self.provisioning_state = None
        self.created_time = None
        self.dead_letter_secret = kwargs.get('dead_letter_secret', None)
        self.endpoint_type = None
