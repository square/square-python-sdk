# -*- coding: utf-8 -*-

from square.api_helper import APIHelper


class BaseApi(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        global_headers (dict): The global headers of the API which are sent with
            every request.

    """

    def global_headers(self):
        return {
            'user-agent': 'Square-Python-SDK/8.1.0.20210121',
            'Square-Version': self.config.square_version
        }

    def __init__(self, config, call_back=None):
        self._config = config
        self._http_call_back = call_back

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    def validate_parameters(self, **kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError("Required parameter {} cannot be None.".format(name))

    def execute_request(self, request, binary=False):
        """Executes an HttpRequest.

        Args:
            request (HttpRequest): The HttpRequest to execute.
            binary (bool): A flag which should be set to True if
                a binary response is expected.

        Returns:
            HttpResponse: The HttpResponse received.

        """
        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back is not None:
            self.http_call_back.on_before_request(request)

        # Add global headers to request
        request.headers = APIHelper.merge_dicts(self.global_headers(), request.headers)
        if self.config.additional_headers is not None:
            request.headers.update(self.config.additional_headers)

        # Invoke the API call to fetch the response.
        func = self.config.http_client.execute_as_binary if binary else self.config.http_client.execute_as_string
        response = func(request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back is not None:
            self.http_call_back.on_after_response(response)

        return response
