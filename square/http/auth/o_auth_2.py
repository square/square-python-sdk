# -*- coding: utf-8 -*-


class OAuth2:

    def __init__(self, access_token):
        self._access_token = access_token

    def validate_arguments(self):
        if self._access_token:
            return True

    def apply(self, http_request):
        """ Add OAuth2 authentication to the request.

            http_request (HttpRequest): The HttpRequest object to which
                authentication header will be added.

        """
        token = self._access_token
        http_request.headers['Authorization'] = "Bearer {}".format(token)

    def error_message(self):
        """Display error message on occurrence of authentication faliure
        in BearerAuth

        """
        return "BearerAuth: _access_token is undefined."
