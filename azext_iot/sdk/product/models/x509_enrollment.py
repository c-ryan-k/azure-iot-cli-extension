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


class X509Enrollment(Model):
    """X509Enrollment.

    :param scope_id:
    :type scope_id: str
    :param subject:
    :type subject: str
    :param thumbprint:
    :type thumbprint: str
    :param registration_id:
    :type registration_id: str
    :param base64_encoded_x509_certificate:
    :type base64_encoded_x509_certificate: str
    """

    _attribute_map = {
        'scope_id': {'key': 'scopeId', 'type': 'str'},
        'subject': {'key': 'subject', 'type': 'str'},
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'registration_id': {'key': 'registrationId', 'type': 'str'},
        'base64_encoded_x509_certificate': {'key': 'base64EncodedX509Certificate', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(X509Enrollment, self).__init__(**kwargs)
        self.scope_id = kwargs.get('scope_id', None)
        self.subject = kwargs.get('subject', None)
        self.thumbprint = kwargs.get('thumbprint', None)
        self.registration_id = kwargs.get('registration_id', None)
        self.base64_encoded_x509_certificate = kwargs.get('base64_encoded_x509_certificate', None)
