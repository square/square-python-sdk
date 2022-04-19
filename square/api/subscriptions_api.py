# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class SubscriptionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(SubscriptionsApi, self).__init__(config, auth_managers)

    def create_subscription(self,
                            body):
        """Does a POST request to /v2/subscriptions.

        Creates a subscription to a subscription plan by a customer.
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

    def retrieve_subscription(self,
                              subscription_id,
                              include=None):
        """Does a GET request to /v2/subscriptions/{subscription_id}.

        Retrieves a subscription.

        Args:
            subscription_id (string): The ID of the subscription to retrieve.
            include (string, optional): A query parameter to specify related
                information to be included in the response.   The supported
                query parameter values are:   - `actions`: to include
                scheduled actions on the targeted subscription.

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
        _query_parameters = {
            'include': include
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

    def update_subscription(self,
                            subscription_id,
                            body):
        """Does a PUT request to /v2/subscriptions/{subscription_id}.

        Updates a subscription. You can set, modify, and clear the
        `subscription` field values.

        Args:
            subscription_id (string): The ID of the subscription to update.
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

    def delete_subscription_action(self,
                                   subscription_id,
                                   action_id):
        """Does a DELETE request to /v2/subscriptions/{subscription_id}/actions/{action_id}.

        Deletes a scheduled action for a subscription.

        Args:
            subscription_id (string): The ID of the subscription the targeted
                action is to act upon.
            action_id (string): The ID of the targeted action to be deleted.

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
        _url_path = '/v2/subscriptions/{subscription_id}/actions/{action_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'subscription_id': {'value': subscription_id, 'encode': True},
            'action_id': {'value': action_id, 'encode': True}
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

    def cancel_subscription(self,
                            subscription_id):
        """Does a POST request to /v2/subscriptions/{subscription_id}/cancel.

        Schedules a `CANCEL` action to cancel an active subscription 
        by setting the `canceled_date` field to the end of the active billing
        period 
        and changing the subscription status from ACTIVE to CANCELED after
        this date.

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

    def list_subscription_events(self,
                                 subscription_id,
                                 cursor=None,
                                 limit=None):
        """Does a GET request to /v2/subscriptions/{subscription_id}/events.

        Lists all events for a specific subscription.

        Args:
            subscription_id (string): The ID of the subscription to retrieve
                the events for.
            cursor (string, optional): When the total number of resulting
                subscription events exceeds the limit of a paged response, 
                specify the cursor returned from a preceding response here to
                fetch the next set of results. If the cursor is unset, the
                response contains the last page of the results.  For more
                information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            limit (int, optional): The upper limit on the number of
                subscription events to return in a paged response.

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

    def pause_subscription(self,
                           subscription_id,
                           body):
        """Does a POST request to /v2/subscriptions/{subscription_id}/pause.

        Schedules a `PAUSE` action to pause an active subscription.

        Args:
            subscription_id (string): The ID of the subscription to pause.
            body (PauseSubscriptionRequest): An object containing the fields
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
        _url_path = '/v2/subscriptions/{subscription_id}/pause'
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

    def resume_subscription(self,
                            subscription_id,
                            body):
        """Does a POST request to /v2/subscriptions/{subscription_id}/resume.

        Schedules a `RESUME` action to resume a paused or a deactivated
        subscription.

        Args:
            subscription_id (string): The ID of the subscription to resume.
            body (ResumeSubscriptionRequest): An object containing the fields
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
        _url_path = '/v2/subscriptions/{subscription_id}/resume'
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

    def swap_plan(self,
                  subscription_id,
                  body):
        """Does a POST request to /v2/subscriptions/{subscription_id}/swap-plan.

        Schedules a `SWAP_PLAN` action to swap a subscription plan in an
        existing subscription.

        Args:
            subscription_id (string): The ID of the subscription to swap the
                subscription plan for.
            body (SwapPlanRequest): An object containing the fields to POST
                for the request.  See the corresponding object definition for
                field details.

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
        _url_path = '/v2/subscriptions/{subscription_id}/swap-plan'
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
