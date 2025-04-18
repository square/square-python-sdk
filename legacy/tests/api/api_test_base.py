# -*- coding: utf-8 -*-

import os
import unittest
from tests.http_response_catcher import HttpResponseCatcher
from square_legacy.configuration import Configuration
from square_legacy.client import Client


class ApiTestBase(unittest.TestCase):

    """All test classes inherit from this base class. It abstracts out
    common functionality and configuration variables set up."""

    client = None
    config = None

    @classmethod
    def setUpClass(cls):
        """Class method called once before running tests in a test class."""
        cls.request_timeout = 30
        cls.assert_precision = 0.01
        cls.config = ApiTestBase.create_configuration()
        cls.client = Client(config=cls.config)

    @staticmethod
    def create_configuration():
        return Configuration(access_token=os.environ['SQUARE_SANDBOX_TOKEN'],
                             environment='sandbox',
                             http_call_back=HttpResponseCatcher())
