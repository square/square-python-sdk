# -*- coding: utf-8 -*-

from apimatic_core.authentication.header_auth import HeaderAuth


class OAuth2(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in BearerAuth

        """
        return "BearerAuth: access_token is undefined."

    def __init__(self, access_token):
        auth_params = {}
        self._access_token = access_token
        if self._access_token:
            auth_params["Authorization"] = "Bearer {}".format(self._access_token)
        super().__init__(auth_params=auth_params)

