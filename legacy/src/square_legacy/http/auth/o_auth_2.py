# -*- coding: utf-8 -*-

from apimatic_core.authentication.header_auth import HeaderAuth


class OAuth2(HeaderAuth):

    @property
    def error_message(self):
        """Display error message on occurrence of authentication failure
        in BearerAuth

        """
        return "BearerAuth: AccessToken is undefined."

    def __init__(self, bearer_auth_credentials):
        self._access_token = bearer_auth_credentials.access_token \
            if bearer_auth_credentials is not None else None
        auth_params = {}
        if self._access_token:
            auth_params = {"Authorization": "Bearer {}".format(self._access_token)}
        super().__init__(auth_params=auth_params)


class BearerAuthCredentials:

    @property
    def access_token(self):
        return self._access_token

    def __init__(self, access_token):
        if access_token is None:
            raise ValueError('access_token cannot be None')
        self._access_token = access_token

    def clone_with(self, access_token=None):
        return BearerAuthCredentials(access_token or self.access_token)
