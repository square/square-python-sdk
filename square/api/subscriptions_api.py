# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or


class SubscriptionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(SubscriptionsApi, self).__init__(config)

    def create_subscription(self,
                            body):
        """Does a POST request to /v2/subscriptions.

        Enrolls a customer in a subscription.
        If you provide a card on file in the request, Square charges the card
        for
        the subscription. Otherwise, Square sends an invoice to the customer's
        email
        address. The subscription starts immediately, unless the request
        includes
        the optional `start_date`. Each individual subscription is associated
        with a particular location.
        For more information, see [Create a
        subscription](https://developer.squareup.com/docs/subscriptions-api/man
        age-subscriptions#create-a-subscription).

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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def bulk_swap_plan(self,
                       body):
        """Does a POST request to /v2/subscriptions/bulk-swap-plan.

        Schedules a plan variation change for all active subscriptions under a
        given plan
        variation. For more information, see [Swap Subscription Plan
        Variations](https://developer.squareup.com/docs/subscriptions-api/swap-
        plan-variations).

        Args:
            body (BulkSwapPlanRequest): An object containing the fields to
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/bulk-swap-plan')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/search')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def retrieve_subscription(self,
                              subscription_id,
                              include=None):
        """Does a GET request to /v2/subscriptions/{subscription_id}.

        Retrieves a specific subscription.

        Args:
            subscription_id (str): The ID of the subscription to retrieve.
            include (str, optional): A query parameter to specify related
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('include')
                         .value(include))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def update_subscription(self,
                            subscription_id,
                            body):
        """Does a PUT request to /v2/subscriptions/{subscription_id}.

        Updates a subscription by modifying or clearing `subscription` field
        values.
        To clear a field, set its value to `null`.

        Args:
            subscription_id (str): The ID of the subscription to update.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def delete_subscription_action(self,
                                   subscription_id,
                                   action_id):
        """Does a DELETE request to /v2/subscriptions/{subscription_id}/actions/{action_id}.

        Deletes a scheduled action for a subscription.

        Args:
            subscription_id (str): The ID of the subscription the targeted
                action is to act upon.
            action_id (str): The ID of the targeted action to be deleted.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}/actions/{action_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('action_id')
                            .value(action_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def change_billing_anchor_date(self,
                                   subscription_id,
                                   body):
        """Does a POST request to /v2/subscriptions/{subscription_id}/billing-anchor.

        Changes the [billing anchor
        date](https://developer.squareup.com/docs/subscriptions-api/subscriptio
        n-billing#billing-dates)
        for a subscription.

        Args:
            subscription_id (str): The ID of the subscription to update the
                billing anchor date.
            body (ChangeBillingAnchorDateRequest): An object containing the
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}/billing-anchor')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def cancel_subscription(self,
                            subscription_id):
        """Does a POST request to /v2/subscriptions/{subscription_id}/cancel.

        Schedules a `CANCEL` action to cancel an active subscription. This 
        sets the `canceled_date` field to the end of the active billing
        period. After this date, 
        the subscription status changes from ACTIVE to CANCELED.

        Args:
            subscription_id (str): The ID of the subscription to cancel.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def list_subscription_events(self,
                                 subscription_id,
                                 cursor=None,
                                 limit=None):
        """Does a GET request to /v2/subscriptions/{subscription_id}/events.

        Lists all
        [events](https://developer.squareup.com/docs/subscriptions-api/actions-
        events) for a specific subscription.

        Args:
            subscription_id (str): The ID of the subscription to retrieve the
                events for.
            cursor (str, optional): When the total number of resulting
                subscription events exceeds the limit of a paged response, 
                specify the cursor returned from a preceding response here to
                fetch the next set of results. If the cursor is unset, the
                response contains the last page of the results.  For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}/events')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def pause_subscription(self,
                           subscription_id,
                           body):
        """Does a POST request to /v2/subscriptions/{subscription_id}/pause.

        Schedules a `PAUSE` action to pause an active subscription.

        Args:
            subscription_id (str): The ID of the subscription to pause.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}/pause')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def resume_subscription(self,
                            subscription_id,
                            body):
        """Does a POST request to /v2/subscriptions/{subscription_id}/resume.

        Schedules a `RESUME` action to resume a paused or a deactivated
        subscription.

        Args:
            subscription_id (str): The ID of the subscription to resume.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}/resume')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()

    def swap_plan(self,
                  subscription_id,
                  body):
        """Does a POST request to /v2/subscriptions/{subscription_id}/swap-plan.

        Schedules a `SWAP_PLAN` action to swap a subscription plan variation
        in an existing subscription. 
        For more information, see [Swap Subscription Plan
        Variations](https://developer.squareup.com/docs/subscriptions-api/swap-
        plan-variations).

        Args:
            subscription_id (str): The ID of the subscription to swap the
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/subscriptions/{subscription_id}/swap-plan')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .is_api_response(True)
            .convertor(ApiResponse.create)
        ).execute()
