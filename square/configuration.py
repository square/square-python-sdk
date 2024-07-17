# -*- coding: utf-8 -*-

import warnings
from copy import deepcopy
from square.api_helper import APIHelper
from apimatic_core.http.configurations.http_client_configuration import HttpClientConfiguration
from apimatic_requests_client_adapter.requests_client import RequestsClient


class Configuration(HttpClientConfiguration):
    """A class used for configuring the SDK by a user.
    """

    @property
    def environment(self):
        return self._environment

    @property
    def custom_url(self):
        return self._custom_url

    @property
    def access_token(self):
        return self._bearer_auth_credentials.access_token

    @property
    def square_version(self):
        return self._square_version

    @property
    def additional_headers(self):
        return deepcopy(self._additional_headers)

    @property
    def user_agent_detail(self):
        return self._user_agent_detail

    @property
    def bearer_auth_credentials(self):
        return self._bearer_auth_credentials

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment='production',
                 custom_url='https://connect.squareup.com', access_token=None,
                 bearer_auth_credentials=None, square_version='2024-07-17',
                 additional_headers={}, user_agent_detail=''):
        if retry_methods is None:
            retry_methods = ['GET', 'PUT']

        if retry_statuses is None:
            retry_statuses = [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]

        super().__init__(http_client_instance,
                         override_http_client_configuration, http_call_back,
                         timeout, max_retries, backoff_factor, retry_statuses,
                         retry_methods)

        # Current API environment
        self._environment = environment

        # Sets the base URL requests are made to. Defaults to `https://connect.squareup.com`
        self._custom_url = custom_url

        # Square Connect API versions
        self._square_version = square_version

        # Additional headers to add to each API request
        self._additional_headers = deepcopy(additional_headers)

        self._bearer_auth_credentials = self.create_auth_credentials_object(
            access_token, bearer_auth_credentials)

        # User agent detail, to be appended with user-agent header.
        self._user_agent_detail = Configuration.validate_user_agent(user_agent_detail)

        # The Http Client to use for making requests.
        self.set_http_client(self.create_http_client())

    def clone_with(self, http_client_instance=None,
                   override_http_client_configuration=None, http_call_back=None,
                   timeout=None, max_retries=None, backoff_factor=None,
                   retry_statuses=None, retry_methods=None, environment=None,
                   custom_url=None, access_token=None,
                   bearer_auth_credentials=None, square_version=None,
                   additional_headers=None, user_agent_detail=None):
        http_client_instance = http_client_instance or self.http_client_instance
        override_http_client_configuration = override_http_client_configuration or self.override_http_client_configuration
        http_call_back = http_call_back or self.http_callback
        timeout = timeout or self.timeout
        max_retries = max_retries or self.max_retries
        backoff_factor = backoff_factor or self.backoff_factor
        retry_statuses = retry_statuses or self.retry_statuses
        retry_methods = retry_methods or self.retry_methods
        environment = environment or self.environment
        custom_url = custom_url or self.custom_url
        square_version = square_version or self.square_version
        additional_headers = additional_headers or self.additional_headers
        user_agent_detail = user_agent_detail or self.user_agent_detail
        bearer_auth_credentials = self.create_auth_credentials_object(
            access_token,
            bearer_auth_credentials or self.bearer_auth_credentials,
            stack_level=3)
        return Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, custom_url=custom_url,
            square_version=square_version, additional_headers=additional_headers,
            user_agent_detail=user_agent_detail,
            bearer_auth_credentials=bearer_auth_credentials
        )

    def create_http_client(self):
        return RequestsClient(
            timeout=self.timeout, max_retries=self.max_retries,
            backoff_factor=self.backoff_factor, retry_statuses=self.retry_statuses,
            retry_methods=self.retry_methods,
            http_client_instance=self.http_client_instance,
            override_http_client_configuration=self.override_http_client_configuration,
            response_factory=self.http_response_factory
        )

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

    @staticmethod
    def validate_user_agent(user_agent):
        if len(user_agent) > 128:
            raise ValueError('The length of user-agent detail should not exceed 128 characters.') 
        return user_agent

    @staticmethod
    def create_auth_credentials_object(access_token, bearer_auth_credentials,
                                       stack_level=4):
        if access_token is None:
            return bearer_auth_credentials

        warnings.warn(message=('The \'access_token\' params are deprecated. Use'
                               ' \'bearer_auth_credentials\' param instead.'),
                      category=DeprecationWarning,
                      stacklevel=stack_level)

        if bearer_auth_credentials is not None:
            return bearer_auth_credentials.clone_with(access_token)

        from square.http.auth.o_auth_2 import BearerAuthCredentials
        return BearerAuthCredentials(access_token)
