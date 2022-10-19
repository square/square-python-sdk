# -*- coding: utf-8 -*-

from apimatic_core.http.response.http_response import HttpResponse


class HttpResponse(HttpResponse):

    """Information about an HTTP Response including its status code, returned
        headers, and raw body

    Attributes:
        status_code (int): The status code response from the server that
            corresponds to this response.
        reason_phrase (string): The reason phrase returned by the server.
        headers (dict): A dictionary of headers (key : value) that were
            returned with the response
        text (string): The Raw body of the HTTP Response as a string
        request (HttpRequest): The request that resulted in this response.

    """

    def __init__(self,
                 status_code,
                 reason_phrase,
                 headers,
                 text,
                 request):
        """Constructor for the HttpResponse class

        Args:
            status_code (int): The response status code.
            reason_phrase (string): The response reason phrase.
            headers (dict): The response headers.
            text (string): The raw body from the server.
            request (HttpRequest): The request that resulted in this response.

        """
        super().__init__(status_code, reason_phrase, headers, text, request)
