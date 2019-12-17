# -*- coding: utf-8 -*-

from square.http.http_method_enum import HttpMethodEnum
from square.http.http_request import HttpRequest


class HttpClient(object):

    """An interface for the methods that an HTTP Client must implement

    This class should not be instantiated but should be used as a base class
    for HTTP Client classes.

    """

    def execute_as_string(self, request):
        """Execute a given HttpRequest to get a string response back

        Args:
            request (HttpRequest): The given HttpRequest to execute.

        Returns:
            HttpResponse: The response of the HttpRequest.

        """
        raise NotImplementedError("Please Implement this method")

    def execute_as_binary(self, request):
        """Execute a given HttpRequest to get a binary response back

        Args:
            request (HttpRequest): The given HttpRequest to execute.

        Returns:
            HttpResponse: The response of the HttpRequest.

        """
        raise NotImplementedError("Please Implement this method")

    def convert_response(self, response, binary):
        """Converts the Response object of the HttpClient into an
        HttpResponse object.

        Args:
            response (dynamic): The original response object.

        Returns:
            HttpResponse: The converted HttpResponse object.

        """
        raise NotImplementedError("Please Implement this method")

    def get(self, query_url,
            headers={},
            query_parameters={}):
        """Create a simple GET HttpRequest object for the given parameters

        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the
                URL.

        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.

        """
        return HttpRequest(HttpMethodEnum.GET,
                           query_url,
                           headers,
                           query_parameters,
                           None,
                           None)

    def head(self, query_url,
             headers={},
             query_parameters={}):
        """Create a simple HEAD HttpRequest object for the given parameters

        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the
                URL.

        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.

        """
        return HttpRequest(HttpMethodEnum.HEAD,
                           query_url,
                           headers,
                           query_parameters,
                           None,
                           None)

    def post(self, query_url,
             headers={},
             query_parameters={},
             parameters={},
             files={}):
        """Create a simple POST HttpRequest object for the given parameters

        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the
                URL.
            parameters (dict, optional): Form or body parameters to be included
                in the body.
            files (dict, optional): Files to be sent with the request.

        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.

        """
        return HttpRequest(HttpMethodEnum.POST,
                           query_url,
                           headers,
                           query_parameters,
                           parameters,
                           files)

    def put(self, query_url,
            headers={},
            query_parameters={},
            parameters={},
            files={}):
        """Create a simple PUT HttpRequest object for the given parameters

        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the
                URL.
            parameters (dict, optional): Form or body parameters to be included
                in the body.
            files (dict, optional): Files to be sent with the request.

        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.

        """
        return HttpRequest(HttpMethodEnum.PUT,
                           query_url,
                           headers,
                           query_parameters,
                           parameters,
                           files)

    def patch(self, query_url,
              headers={},
              query_parameters={},
              parameters={},
              files={}):
        """Create a simple PATCH HttpRequest object for the given parameters

        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the
                URL.
            parameters (dict, optional): Form or body parameters to be included
                in the body.
            files (dict, optional): Files to be sent with the request.

        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.

        """
        return HttpRequest(HttpMethodEnum.PATCH,
                           query_url,
                           headers,
                           query_parameters,
                           parameters,
                           files)

    def delete(self, query_url,
               headers={},
               query_parameters={},
               parameters={},
               files={}):
        """Create a simple DELETE HttpRequest object for the given parameters

        Args:
            query_url (string): The URL to send the request to.
            headers (dict, optional): The headers for the HTTP Request.
            query_parameters (dict, optional): Query parameters to add in the
                URL.
            parameters (dict, optional): Form or body parameters to be
                included in the body.
            files (dict, optional): Files to be sent with the request.

        Returns:
            HttpRequest: The generated HttpRequest for the given paremeters.

        """
        return HttpRequest(HttpMethodEnum.DELETE,
                           query_url,
                           headers,
                           query_parameters,
                           parameters,
                           files)
