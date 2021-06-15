# -*- coding: utf-8 -*-

from copy import deepcopy
from square.api_helper import APIHelper
from square.http.requests_client import RequestsClient


class Configuration(object):
    """A class used for configuring the SDK by a user.
    """

    @property
    def http_client(self):
        return self._http_client

    @property
    def timeout(self):
        return self._timeout

    @property
    def max_retries(self):
        return self._max_retries

    @property
    def backoff_factor(self):
        return self._backoff_factor

    @property
    def retry_statuses(self):
        return self._retry_statuses

    @property
    def retry_methods(self):
        return self._retry_methods

    @property
    def environment(self):
        return self._environment

    @property
    def custom_url(self):
        return self._custom_url

    @property
    def square_version(self):
        return self._square_version

    @property
    def access_token(self):
        return self._access_token

    @property
    def additional_headers(self):
        return deepcopy(self._additional_headers)

    def __init__(
        self, timeout=60, max_retries=0, backoff_factor=2,
        retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
        retry_methods=['GET', 'PUT'], environment='production',
        custom_url='https://connect.squareup.com', square_version='2021-06-16',
        access_token='TODO: Replace', additional_headers={}
    ):
        # The value to use for connection timeout
        self._timeout = timeout

        # The number of times to retry an endpoint call if it fails
        self._max_retries = max_retries

        # A backoff factor to apply between attempts after the second try.
        # urllib3 will sleep for:
        # `{backoff factor} * (2 ** ({number of total retries} - 1))`
        self._backoff_factor = backoff_factor

        # The http statuses on which retry is to be done
        self._retry_statuses = retry_statuses

        # The http methods on which retry is to be done
        self._retry_methods = retry_methods

        # Current API environment
        self._environment = environment

        # Sets the base URL requests are made to. Defaults to `https://connect.squareup.com`
        self._custom_url = custom_url

        # Square Connect API versions
        self._square_version = square_version

        # The OAuth 2.0 Access Token to use for API requests.
        self._access_token = access_token

        # Additional headers to add to each API request
        self._additional_headers = deepcopy(additional_headers)

        # The Http Client to use for making requests.
        self._http_client = self.create_http_client()

    def clone_with(self, timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   custom_url=None, square_version=None, access_token=None,
                   additional_headers=None):
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        custom_url = custom_url or self.custom_url
        square_version = square_version or self.square_version
        access_token = access_token or self.access_token
        additional_headers = additional_headers or self.additional_headers

        return Configuration(timeout=timeout, max_retries=max_retries,
                             backoff_factor=backoff_factor,
                             retry_statuses=retry_statuses,
                             retry_methods=retry_methods,
                             environment=environment, custom_url=custom_url,
                             square_version=square_version,
                             access_token=access_token,
                             additional_headers=additional_headers)

    def create_http_client(self):
        return RequestsClient(timeout=self.timeout,
                              max_retries=self.max_retries,
                              backoff_factor=self.backoff_factor,
                              retry_statuses=self.retry_statuses,
                              retry_methods=self.retry_methods)

    # All the environments the SDK can run in
    environments = {
        'production': {
            'default': 'https://connect.squareup.com'
        },
        'sandbox': {
            'default': 'https://connect.squareupsandbox.com'
        },
        'custom': {
            'default': '{custom_url}'
        }
    }

    def get_base_uri(self, server='default'):
        """Generates the appropriate base URI for the environment and the
        server.

        Args:
            server (Configuration.Server): The server enum for which the base
            URI is required.

        Returns:
            String: The base URI.

        """
        parameters = {
            "custom_url": {'value': self.custom_url, 'encode': False},
        }

        return APIHelper.append_url_with_template_parameters(
            self.environments[self.environment][server], parameters
        )
