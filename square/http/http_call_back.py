# -*- coding: utf-8 -*-


class HttpCallBack(object):

    """An interface for  the callback to be called before and after the
    HTTP call for an endpoint is made.

    This class should not be instantiated but should be used as a base class
    for HttpCallBack classes.

    """

    def on_before_request(self,
                          request):
        """The controller will call this method before making the HttpRequest.

        Args:
            request (HttpRequest): The request object which will be sent
                to the HttpClient to be executed.
        """
        raise NotImplementedError("This method has not been implemented.")

    def on_after_response(self,
                          http_response):
        """The controller will call this method after making the HttpRequest.

        Args:
            http_response (HttpResponse): The HttpResponse of the API call.
        """
        raise NotImplementedError("This method has not been implemented.")
