# -*- coding: utf-8 -*-

from apimatic_core.http.http_callback import HttpCallBack


class HttpCallBack(HttpCallBack):

    """An interface for the callback to be called before and after the
    HTTP call for an endpoint is made.

    This class should not be instantiated but should be used as a base class
    for HttpCallBack classes.

    """