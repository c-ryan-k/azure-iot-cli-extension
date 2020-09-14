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

try:
    from .digital_twins_description_py3 import DigitalTwinsDescription
    from .digital_twins_patch_description_py3 import DigitalTwinsPatchDescription
    from .digital_twins_resource_py3 import DigitalTwinsResource
    from .error_definition_py3 import ErrorDefinition
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .check_name_request_py3 import CheckNameRequest
    from .check_name_result_py3 import CheckNameResult
    from .external_resource_py3 import ExternalResource
    from .digital_twins_endpoint_resource_properties_py3 import DigitalTwinsEndpointResourceProperties
    from .digital_twins_endpoint_resource_py3 import DigitalTwinsEndpointResource
    from .service_bus_py3 import ServiceBus
    from .event_hub_py3 import EventHub
    from .event_grid_py3 import EventGrid
except (SyntaxError, ImportError):
    from .digital_twins_description import DigitalTwinsDescription
    from .digital_twins_patch_description import DigitalTwinsPatchDescription
    from .digital_twins_resource import DigitalTwinsResource
    from .error_definition import ErrorDefinition
    from .error_response import ErrorResponse, ErrorResponseException
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .check_name_request import CheckNameRequest
    from .check_name_result import CheckNameResult
    from .external_resource import ExternalResource
    from .digital_twins_endpoint_resource_properties import DigitalTwinsEndpointResourceProperties
    from .digital_twins_endpoint_resource import DigitalTwinsEndpointResource
    from .service_bus import ServiceBus
    from .event_hub import EventHub
    from .event_grid import EventGrid
from .digital_twins_description_paged import DigitalTwinsDescriptionPaged
from .digital_twins_endpoint_resource_paged import DigitalTwinsEndpointResourcePaged
from .operation_paged import OperationPaged
from .azure_digital_twins_management_client_enums import (
    ProvisioningState,
    Reason,
    EndpointProvisioningState,
)

__all__ = [
    'DigitalTwinsDescription',
    'DigitalTwinsPatchDescription',
    'DigitalTwinsResource',
    'ErrorDefinition',
    'ErrorResponse', 'ErrorResponseException',
    'OperationDisplay',
    'Operation',
    'CheckNameRequest',
    'CheckNameResult',
    'ExternalResource',
    'DigitalTwinsEndpointResourceProperties',
    'DigitalTwinsEndpointResource',
    'ServiceBus',
    'EventHub',
    'EventGrid',
    'DigitalTwinsDescriptionPaged',
    'DigitalTwinsEndpointResourcePaged',
    'OperationPaged',
    'ProvisioningState',
    'Reason',
    'EndpointProvisioningState',
]
