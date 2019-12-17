# -*- coding: utf-8 -*-


class OAuth2:

    @staticmethod
    def apply(config, http_request):
        """ Add OAuth2 authentication to the request.

        Args:
            config (Configuration): The Configuration object which holds the
                authentication information.
            http_request (HttpRequest): The HttpRequest object to which
                authentication header will be added.

        """
        token = config.access_token
        http_request.headers['Authorization'] = "Bearer {}".format(token)
