# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class WebhookSubscriptionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(WebhookSubscriptionsApi, self).__init__(config, auth_managers)

    def list_webhook_event_types(self,
                                 api_version=None):
        """Does a GET request to /v2/webhooks/event-types.

        Lists all webhook event types that can be subscribed to.

        Args:
            api_version (string, optional): The API version for which to list
                event types. Setting this field overrides the default version
                used by the application.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/event-types'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'api_version': api_version
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_webhook_subscriptions(self,
                                   cursor=None,
                                   include_disabled=False,
                                   sort_order=None,
                                   limit=None):
        """Does a GET request to /v2/webhooks/subscriptions.

        Lists all webhook subscriptions owned by your application.

        Args:
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for your original query.  For more
                information, see
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination).
            include_disabled (bool, optional): Includes disabled
                [Subscription]($m/WebhookSubscription)s. By default, all
                enabled [Subscription]($m/WebhookSubscription)s are returned.
            sort_order (SortOrder, optional): Sorts the returned list by when
                the [Subscription]($m/WebhookSubscription) was created with
                the specified order. This field defaults to ASC.
            limit (int, optional): The maximum number of results to be
                returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default
                value of 100 is also the maximum allowed value. If the
                provided value is greater than 100, it is ignored and the
                default value is used instead.  Default: 100

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/subscriptions'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
            'include_disabled': include_disabled,
            'sort_order': sort_order,
            'limit': limit
        }
        _query_builder = APIHelper.append_url_with_query_parameters(
            _query_builder,
            _query_parameters
        )
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def create_webhook_subscription(self,
                                    body):
        """Does a POST request to /v2/webhooks/subscriptions.

        Creates a webhook subscription.

        Args:
            body (CreateWebhookSubscriptionRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/subscriptions'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def delete_webhook_subscription(self,
                                    subscription_id):
        """Does a DELETE request to /v2/webhooks/subscriptions/{subscription_id}.

        Deletes a webhook subscription.

        Args:
            subscription_id (string): [REQUIRED] The ID of the
                [Subscription]($m/WebhookSubscription) to delete.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/subscriptions/{subscription_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_webhook_subscription(self,
                                      subscription_id):
        """Does a GET request to /v2/webhooks/subscriptions/{subscription_id}.

        Retrieves a webhook subscription identified by its ID.

        Args:
            subscription_id (string): [REQUIRED] The ID of the
                [Subscription]($m/WebhookSubscription) to retrieve.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/subscriptions/{subscription_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_webhook_subscription(self,
                                    subscription_id,
                                    body):
        """Does a PUT request to /v2/webhooks/subscriptions/{subscription_id}.

        Updates a webhook subscription.

        Args:
            subscription_id (string): [REQUIRED] The ID of the
                [Subscription]($m/WebhookSubscription) to update.
            body (UpdateWebhookSubscriptionRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/subscriptions/{subscription_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_webhook_subscription_signature_key(self,
                                                  subscription_id,
                                                  body):
        """Does a POST request to /v2/webhooks/subscriptions/{subscription_id}/signature-key.

        Updates a webhook subscription by replacing the existing signature key
        with a new one.

        Args:
            subscription_id (string): [REQUIRED] The ID of the
                [Subscription]($m/WebhookSubscription) to update.
            body (UpdateWebhookSubscriptionSignatureKeyRequest): An object
                containing the fields to POST for the request.  See the
                corresponding object definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/subscriptions/{subscription_id}/signature-key'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def test_webhook_subscription(self,
                                  subscription_id,
                                  body):
        """Does a POST request to /v2/webhooks/subscriptions/{subscription_id}/test.

        Tests a webhook subscription by sending a test event to the
        notification URL.

        Args:
            subscription_id (string): [REQUIRED] The ID of the
                [Subscription]($m/WebhookSubscription) to test.
            body (TestWebhookSubscriptionRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/webhooks/subscriptions/{subscription_id}/test'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        # Apply authentication scheme on request
        self.apply_auth_schemes(_request, 'global')

        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
