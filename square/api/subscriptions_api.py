# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class SubscriptionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(SubscriptionsApi, self).__init__(config, call_back)

    def create_subscription(self,
                            body):
        """Does a POST request to /v2/subscriptions.

        Creates a subscription for a customer to a subscription plan.
        If you provide a card on file in the request, Square charges the card
        for 
        the subscription. Otherwise, Square bills an invoice to the customer's
        email 
        address. The subscription starts immediately, unless the request
        includes 
        the optional `start_date`. Each individual subscription is associated
        with a particular location.

        Args:
            body (CreateSubscriptionRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
        _url_path = '/v2/subscriptions'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def search_subscriptions(self,
                             body):
        """Does a POST request to /v2/subscriptions/search.

        Searches for subscriptions. 
        Results are ordered chronologically by subscription creation date. If
        the request specifies more than one location ID, 
        the endpoint orders the result 
        by location ID, and then by creation date within each location. If no
        locations are given
        in the query, all locations are searched.
        You can also optionally specify `customer_ids` to search by customer.
                If left unset, all customers 
        associated with the specified locations are returned. 
        If the request specifies customer IDs, the endpoint orders results 
        first by location, within location by customer ID, and within 
        customer by subscription creation date.
        For more information, see 
        [Retrieve
        subscriptions](https://developer.squareup.com/docs/subscriptions-api/ov
        erview#retrieve-subscriptions).

        Args:
            body (SearchSubscriptionsRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
        _url_path = '/v2/subscriptions/search'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_subscription(self,
                              subscription_id):
        """Does a GET request to /v2/subscriptions/{subscription_id}.

        Retrieves a subscription.

        Args:
            subscription_id (string): The ID of the subscription to retrieve.

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
        _url_path = '/v2/subscriptions/{subscription_id}'
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def update_subscription(self,
                            subscription_id,
                            body):
        """Does a PUT request to /v2/subscriptions/{subscription_id}.

        Updates a subscription. You can set, modify, and clear the 
        `subscription` field values.

        Args:
            subscription_id (string): The ID for the subscription to update.
            body (UpdateSubscriptionRequest): An object containing the fields
                to POST for the request.  See the corresponding object
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
        _url_path = '/v2/subscriptions/{subscription_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'content-type': 'application/json; charset=utf-8'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def cancel_subscription(self,
                            subscription_id):
        """Does a POST request to /v2/subscriptions/{subscription_id}/cancel.

        Sets the `canceled_date` field to the end of the active billing
        period.
        After this date, the status changes from ACTIVE to CANCELED.

        Args:
            subscription_id (string): The ID of the subscription to cancel.

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
        _url_path = '/v2/subscriptions/{subscription_id}/cancel'
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
        _request = self.config.http_client.post(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def list_subscription_events(self,
                                 subscription_id,
                                 cursor=None,
                                 limit=None):
        """Does a GET request to /v2/subscriptions/{subscription_id}/events.

        Lists all events for a specific subscription.
        In the current implementation, only `START_SUBSCRIPTION` and
        `STOP_SUBSCRIPTION` (when the subscription was canceled) events are
        returned.

        Args:
            subscription_id (string): The ID of the subscription to retrieve
                the events for.
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this to retrieve the
                next set of results for the original query.  For more
                information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            limit (int, optional): The upper limit on the number of
                subscription events to return  in the response.   Default:
                `200`

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
        _url_path = '/v2/subscriptions/{subscription_id}/events'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result
