import json


class ApiResponse:

    """Http response received.

    Attributes:
        status_code (int): The status code response from the server that
            corresponds to this response.
        reason_phrase (string): The reason phrase returned by the server.
        headers (dict): A dictionary of headers (key : value) that were
            returned with the response
        text (string): The Raw body of the HTTP Response as a string
        request (HttpRequest): The request that resulted in this response.
        body (Object): The data field specified for the response
        errors (Array<String>): Any errors returned by the server

    """

    def __init__(self, http_response,
                 body=None,
                 errors=None):

        """The Constructor

        Args:
            http_response (HttpResponse): The original, raw response from the api
            data (Object): The data field specified for the response
            errors (Array<String>): Any errors returned by the server

        """

        self.status_code = http_response.status_code
        self.reason_phrase = http_response.reason_phrase
        self.headers = http_response.headers
        self.text = http_response.text
        self.request = http_response.request
        self.body = body
        self.errors = errors
        if type(body) is dict:
            self.cursor = body.get('cursor')

    def is_success(self):
        """ Returns true if status code is between 200-300

        """
        return 200 <= self.status_code < 300

    def is_error(self):
        """ Returns true if status code is between 400-600

        """
        return 400 <= self.status_code < 600

    def __repr__(self):
        return '<ApiResponse [%s]>' % (self.text)
