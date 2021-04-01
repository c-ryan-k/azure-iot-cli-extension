# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.authentication import Authentication


class TrackTwoAuthentication(Authentication):
    """
    Used for only testing
    Shared Access Signature authorization for Azure IoT Hub.

    """

    def __init__(self, cmd, resource_id):
        self.resource_id = resource_id
        self.cmd = cmd
        self.parsed_token = None

    def signed_session(self, session=None):
        """
        Create requests session with SAS auth headers.

        If a session object is provided, configure it directly. Otherwise,
        create a new session and return it.

        Returns:
            session (): requests.Session.
        """

        return self.refresh_session(session)

    def refresh_session(
        self, session=None,
    ):
        """
        Refresh requests session with SAS auth headers.

        If a session object is provided, configure it directly. Otherwise,
        create a new session and return it.

        Returns:
            session (): requests.Session.
        """

        session = session or super(TrackTwoAuthentication, self).signed_session()
        session.headers["Authorization"] = self.generate_token()
        return session

    def generate_token(self):
        from azure.cli.core._profile import Profile

        profile = Profile(cli_ctx=self.cmd.cli_ctx)
        creds, subscription, tenant = profile.get_raw_token(resource=self.resource_id)
        self.parsed_token = {
            "tokenType": creds[0],
            "accessToken": creds[1],
            "expires_on": creds[2].get("expires_on", "N/A"),
            "subscription": subscription,
            "tenant": tenant,
        }
        return "{} {}".format(self.parsed_token["tokenType"], self.parsed_token["accessToken"])

    def get_token(self, *scopes):
        if self.parsed_token is None:
            self.refresh_session()
        return self.parsed_token["accessToken"]
