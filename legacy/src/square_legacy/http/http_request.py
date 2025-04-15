# -*- coding: utf-8 -*-

from apimatic_core.http.request.http_request import HttpRequest


class HttpRequest(HttpRequest):

    """Information about an HTTP Request including its method, headers,
        parameters, URL, and Basic Auth details

    Attributes:
        http_method (HttpMethodEnum): The HTTP Method that this request should
            perform when called.
        headers (dict): A dictionary of headers (key : value) that should be
            sent along with the request.
        query_url (string): The URL that the request should be sent to.
        parameters (dict): A dictionary of parameters that are to be sent along
            with the request in the form body of the request

    """

    def __init__(self,
                 http_method,
                 query_url,
                 headers=None,
                 query_parameters=None,
                 parameters=None,
                 files=None):
        """Constructor for the HttpRequest class

        Args:
            http_method (HttpMethodEnum): The HTTP Method.
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the
                URL.
            parameters (dict, optional): Form or body parameters to be included
                in the body.
            files (dict, optional): Files to be sent with the request.

        """
        super().__init__(http_method,
                         query_url,
                         headers,
                         query_parameters,
                         parameters,
                         files)
