# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi


class GiftCardsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(GiftCardsApi, self).__init__(config, auth_managers)

    def list_gift_cards(self,
                        mtype=None,
                        state=None,
                        limit=None,
                        cursor=None,
                        customer_id=None):
        """Does a GET request to /v2/gift-cards.

        Lists all gift cards. You can specify optional filters to retrieve 
        a subset of the gift cards. Results are sorted by `created_at` in
        ascending order.

        Args:
            mtype (string, optional): If a [type]($m/GiftCardType) is
                provided, the endpoint returns gift cards of the specified
                type. Otherwise, the endpoint returns gift cards of all
                types.
            state (string, optional): If a [state]($m/GiftCardStatus) is
                provided, the endpoint returns the gift cards in the specified
                state. Otherwise, the endpoint returns the gift cards of all
                states.
            limit (int, optional): If a limit is provided, the endpoint
                returns only the specified number of results per page. The
                maximum value is 50. The default value is 30. For more
                information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for the original query. If a
                cursor is not provided, the endpoint returns the first page of
                the results.  For more information, see
                [Pagination](https://developer.squareup.com/docs/working-with-a
                pis/pagination).
            customer_id (string, optional): If a customer ID is provided, the
                endpoint returns only the gift cards linked to the specified
                customer.

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
        _url_path = '/v2/gift-cards'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'type': mtype,
            'state': state,
            'limit': limit,
            'cursor': cursor,
            'customer_id': customer_id
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

    def create_gift_card(self,
                         body):
        """Does a POST request to /v2/gift-cards.

        Creates a digital gift card or registers a physical (plastic) gift
        card. After the gift card 
        is created, you must call
        [CreateGiftCardActivity]($e/GiftCardActivities/CreateGiftCardActivity)
                to activate the card with an initial balance before it can be used for
        payment.

        Args:
            body (CreateGiftCardRequest): An object containing the fields to
                POST for the request.  See the corresponding object definition
                for field details.

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
        _url_path = '/v2/gift-cards'
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

    def retrieve_gift_card_from_gan(self,
                                    body):
        """Does a POST request to /v2/gift-cards/from-gan.

        Retrieves a gift card using the gift card account number (GAN).

        Args:
            body (RetrieveGiftCardFromGANRequest): An object containing the
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
        _url_path = '/v2/gift-cards/from-gan'
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

    def retrieve_gift_card_from_nonce(self,
                                      body):
        """Does a POST request to /v2/gift-cards/from-nonce.

        Retrieves a gift card using a secure payment token that represents the
        gift card.

        Args:
            body (RetrieveGiftCardFromNonceRequest): An object containing the
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
        _url_path = '/v2/gift-cards/from-nonce'
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

    def link_customer_to_gift_card(self,
                                   gift_card_id,
                                   body):
        """Does a POST request to /v2/gift-cards/{gift_card_id}/link-customer.

        Links a customer to a gift card, which is also referred to as adding a
        card on file.

        Args:
            gift_card_id (string): The ID of the gift card to be linked.
            body (LinkCustomerToGiftCardRequest): An object containing the
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
        _url_path = '/v2/gift-cards/{gift_card_id}/link-customer'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'gift_card_id': {'value': gift_card_id, 'encode': True}
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

    def unlink_customer_from_gift_card(self,
                                       gift_card_id,
                                       body):
        """Does a POST request to /v2/gift-cards/{gift_card_id}/unlink-customer.

        Unlinks a customer from a gift card, which is also referred to as
        removing a card on file.

        Args:
            gift_card_id (string): The ID of the gift card to be unlinked.
            body (UnlinkCustomerFromGiftCardRequest): An object containing the
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
        _url_path = '/v2/gift-cards/{gift_card_id}/unlink-customer'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'gift_card_id': {'value': gift_card_id, 'encode': True}
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

    def retrieve_gift_card(self,
                           id):
        """Does a GET request to /v2/gift-cards/{id}.

        Retrieves a gift card using the gift card ID.

        Args:
            id (string): The ID of the gift card to retrieve.

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
        _url_path = '/v2/gift-cards/{id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'id': {'value': id, 'encode': True}
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
