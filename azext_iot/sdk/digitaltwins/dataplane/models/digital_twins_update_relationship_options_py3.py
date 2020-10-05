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


class DigitalTwinsUpdateRelationshipOptions(Model):
    """Additional parameters for update_relationship operation.

    :param traceparent: Identifies the request in a distributed tracing
     system.
    :type traceparent: str
    :param tracestate: Provides vendor-specific trace identification
     information and is a companion to traceparent.
    :type tracestate: str
    :param if_match: Only perform the operation if the entity's etag matches
     one of the etags provided or * is provided.
    :type if_match: str
    """

    _attribute_map = {
        'traceparent': {'key': '', 'type': 'str'},
        'tracestate': {'key': '', 'type': 'str'},
        'if_match': {'key': '', 'type': 'str'},
    }

    def __init__(self, *, traceparent: str=None, tracestate: str=None, if_match: str=None, **kwargs) -> None:
        super(DigitalTwinsUpdateRelationshipOptions, self).__init__(**kwargs)
        self.traceparent = traceparent
        self.tracestate = tracestate
        self.if_match = if_match
