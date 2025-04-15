from apimatic_core.http.response.api_response import ApiResponse
from apimatic_core.http.response.http_response import HttpResponse


class ApiResponse(ApiResponse):

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
            body (Object): The body of the actual response
            errors (Array<String>): Any errors returned by the server

        """

        super().__init__(http_response, body, errors)
        if type(body) is dict:
            self.cursor = body.get('cursor')

    def __repr__(self):
        return '<ApiResponse {}>'.format(self.text)

    @classmethod
    def create(cls, parent_instance):
        return cls(HttpResponse(parent_instance.status_code, parent_instance.reason_phrase,
                                parent_instance.headers, parent_instance.text, parent_instance.request),
                   parent_instance.body, parent_instance.errors)
