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


class TestRun(Model):
    """Test run result for API.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id:
    :type id: str
    :param start_time:
    :type start_time: datetime
    :param end_time:
    :type end_time: datetime
    :param status: Possible values include: 'Queued', 'Started', 'Running',
     'Failed', 'Completed', 'Cancelled'
    :type status: str or ~product.models.enum
    :ivar certification_badge_results:
    :vartype certification_badge_results: list[object]
    """

    _validation = {
        'certification_badge_results': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'status': {'key': 'status', 'type': 'str'},
        'certification_badge_results': {'key': 'certificationBadgeResults', 'type': '[object]'},
    }

    def __init__(self, *, id: str=None, start_time=None, end_time=None, status=None, **kwargs) -> None:
        super(TestRun, self).__init__(**kwargs)
        self.id = id
        self.start_time = start_time
        self.end_time = end_time
        self.status = status
        self.certification_badge_results = None
