# -*- coding: utf-8 -*-


class APIException(Exception):

    """Class that handles HTTP Exceptions when fetching API Endpoints.

    Attributes:
        response_code (int): The status code of the response.
        response (HttpResponse): The HttpResponse of the API call.

    """

    def __init__(self,
                 reason,
                 response):
        """Constructor for the APIException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(APIException, self).__init__(reason)
        self.reason = reason
        self.response = response
        self.response_code = response.status_code
