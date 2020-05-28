# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2


class LoyaltyApi(BaseApi):

    """A Controller to access Endpoints in the square API."""

    def __init__(self, config, call_back=None):
        super(LoyaltyApi, self).__init__(config, call_back)

    def create_loyalty_account(self,
                               body):
        """Does a POST request to /v2/loyalty/accounts.

        Creates a loyalty account. For more information, see 
        [Create a loyalty
        account](https://developer.squareup.com/docs/docs/loyalty-api/overview/
        #loyalty-overview-create-account).

        Args:
            body (CreateLoyaltyAccountRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            CreateLoyaltyAccountResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/accounts'
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

    def search_loyalty_accounts(self,
                                body):
        """Does a POST request to /v2/loyalty/accounts/search.

        Searches for loyalty accounts. 
        In the current implementation, you can search for a loyalty account
        using the phone number associated with the account. 
        If no phone number is provided, all loyalty accounts are returned.

        Args:
            body (SearchLoyaltyAccountsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            SearchLoyaltyAccountsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/accounts/search'
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

    def retrieve_loyalty_account(self,
                                 account_id):
        """Does a GET request to /v2/loyalty/accounts/{account_id}.

        Retrieves a loyalty account.

        Args:
            account_id (string): The ID of the [loyalty
                account](#type-LoyaltyAccount) to retrieve.

        Returns:
            RetrieveLoyaltyAccountResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/accounts/{account_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'account_id': account_id
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

    def accumulate_loyalty_points(self,
                                  account_id,
                                  body):
        """Does a POST request to /v2/loyalty/accounts/{account_id}/accumulate.

        Adds points to a loyalty account.
        - If you are using the Orders API to manage orders, you only provide
        the `order_id`. 
        The endpoint reads the order to compute points to add to the buyer's
        account.
        - If you are not using the Orders API to manage orders, 
        you first perform a client-side computation to compute the points.  
        For spend-based and visit-based programs, you can call 
        `CalculateLoyaltyPoints` to compute the points. For more information,
                see [Loyalty Program
        Overview](https://developer.squareup.com/docs/docs/loyalty/overview).
                You then provide the points in a request to this endpoint. 
        For more information, see [Accumulate
        points](https://developer.squareup.com/docs/docs/loyalty-api/overview/#
        accumulate-points).

        Args:
            account_id (string): The [loyalty account](#type-LoyaltyAccount)
                ID to which to add the points.
            body (AccumulateLoyaltyPointsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            AccumulateLoyaltyPointsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/accounts/{account_id}/accumulate'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'account_id': account_id
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

    def adjust_loyalty_points(self,
                              account_id,
                              body):
        """Does a POST request to /v2/loyalty/accounts/{account_id}/adjust.

        Adds points to or subtracts points from a buyer's account. 
        Use this endpoint only when you need to manually adjust points.
        Otherwise, in your application flow, you call 
        [AccumulateLoyaltyPoints](https://developer.squareup.com/docs/reference
        /square/loyalty-api/accumulate-loyalty-points) 
        to add points when a buyer pays for the purchase.

        Args:
            account_id (string): The ID of the [loyalty
                account](#type-LoyaltyAccount) in which to adjust the points.
            body (AdjustLoyaltyPointsRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            AdjustLoyaltyPointsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/accounts/{account_id}/adjust'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'account_id': account_id
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

    def search_loyalty_events(self,
                              body):
        """Does a POST request to /v2/loyalty/events/search.

        Searches for loyalty events.
        A Square loyalty program maintains a ledger of events that occur
        during the lifetime of a 
        buyer's loyalty account. Each change in the point balance 
        (for example, points earned, points redeemed, and points expired) is 
        recorded in the ledger. Using this endpoint, you can search the ledger
        for events. 
        For more information, see 
        [Loyalty
        events](https://developer.squareup.com/docs/docs/loyalty-api/overview/#
        loyalty-events).

        Args:
            body (SearchLoyaltyEventsRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            SearchLoyaltyEventsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/events/search'
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

    def list_loyalty_programs(self):
        """Does a GET request to /v2/loyalty/programs.

        Returns a list of loyalty programs in the seller's account.
        Currently, a seller can only have one loyalty program. For more
        information, see 
        [Loyalty
        Overview](https://developer.squareup.com/docs/docs/loyalty/overview).
        .

        Returns:
            ListLoyaltyProgramsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/programs'
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

    def calculate_loyalty_points(self,
                                 program_id,
                                 body):
        """Does a POST request to /v2/loyalty/programs/{program_id}/calculate.

        Calculates the points a purchase earns.
        - If you are using the Orders API to manage orders, you provide
        `order_id` in the request. The 
        endpoint calculates the points by reading the order.
        - If you are not using the Orders API to manage orders, you provide
        the purchase amount in 
        the request for the endpoint to calculate the points.
        An application might call this endpoint to show the points that a
        buyer can earn with the 
        specific purchase.

        Args:
            program_id (string): The [loyalty program](#type-LoyaltyProgram)
                ID, which defines the rules for accruing points.
            body (CalculateLoyaltyPointsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            CalculateLoyaltyPointsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/programs/{program_id}/calculate'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'program_id': program_id
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

    def create_loyalty_reward(self,
                              body):
        """Does a POST request to /v2/loyalty/rewards.

        Creates a loyalty reward. In the process, the endpoint does
        following:
        - Uses the `reward_tier_id` in the request to determine the number of
        points 
        to lock for this reward. 
        - If the request includes `order_id`, it adds the reward and related
        discount to the order. 
        After a reward is created, the points are locked and 
        not available for the buyer to redeem another reward. 
        For more information, see 
        [Loyalty
        rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/
        #loyalty-overview-loyalty-rewards).

        Args:
            body (CreateLoyaltyRewardRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            CreateLoyaltyRewardResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/rewards'
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

    def search_loyalty_rewards(self,
                               body):
        """Does a POST request to /v2/loyalty/rewards/search.

        Searches for loyalty rewards in a loyalty account. 
        In the current implementation, the endpoint supports search by the
        reward `status`.
        If you know a reward ID, use the 
        [RetrieveLoyaltyReward](https://developer.squareup.com/docs/reference/s
        quare/loyalty-api/retrieve-loyalty-reward) endpoint.
        For more information about loyalty rewards, see 
        [Loyalty
        Rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/
        #loyalty-rewards).

        Args:
            body (SearchLoyaltyRewardsRequest): An object containing the
                fields to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            SearchLoyaltyRewardsResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/rewards/search'
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

    def delete_loyalty_reward(self,
                              reward_id):
        """Does a DELETE request to /v2/loyalty/rewards/{reward_id}.

        Deletes a loyalty reward by doing the following:
        - Returns the loyalty points back to the loyalty account.
        - If an order ID was specified when the reward was created 
        (see
        [CreateLoyaltyReward](https://developer.squareup.com/docs/reference/squ
        are/loyalty-api/create-loyalty-reward)), 
        it updates the order by removing the reward and related 
        discounts.
        You cannot delete a reward that has reached the terminal state
        (REDEEMED). 
        For more information, see 
        [Loyalty
        rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/
        #loyalty-overview-loyalty-rewards).

        Args:
            reward_id (string): The ID of the [loyalty
                reward](#type-LoyaltyReward) to delete.

        Returns:
            DeleteLoyaltyRewardResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/rewards/{reward_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'reward_id': reward_id
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
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        decoded = APIHelper.json_deserialize(_response.text)
        if type(decoded) is dict:
            _errors = decoded.get('errors')
        else:
            _errors = None
        _result = ApiResponse(_response, body=decoded, errors=_errors)
        return _result

    def retrieve_loyalty_reward(self,
                                reward_id):
        """Does a GET request to /v2/loyalty/rewards/{reward_id}.

        Retrieves a loyalty reward.

        Args:
            reward_id (string): The ID of the [loyalty
                reward](#type-LoyaltyReward) to retrieve.

        Returns:
            RetrieveLoyaltyRewardResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/rewards/{reward_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'reward_id': reward_id
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

    def redeem_loyalty_reward(self,
                              reward_id,
                              body):
        """Does a POST request to /v2/loyalty/rewards/{reward_id}/redeem.

        Redeems a loyalty reward.
        The endpoint sets the reward to the terminal state (`REDEEMED`). 
        If you are using your own order processing system (not using the 
        Orders API), you call this endpoint after the buyer paid for the 
        purchase.
        After the reward reaches the terminal state, it cannot be deleted. 
        In other words, points used for the reward cannot be returned 
        to the account.
        For more information, see 
        [Loyalty
        rewards](https://developer.squareup.com/docs/docs/loyalty-api/overview/
        #loyalty-overview-loyalty-rewards).

        Args:
            reward_id (string): The ID of the [loyalty
                reward](#type-LoyaltyReward) to redeem.
            body (RedeemLoyaltyRewardRequest): An object containing the fields
                to POST for the request.  See the corresponding object
                definition for field details.

        Returns:
            RedeemLoyaltyRewardResponse: Response from the API. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/v2/loyalty/rewards/{reward_id}/redeem'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'reward_id': reward_id
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
