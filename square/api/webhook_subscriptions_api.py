# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single


class WebhookSubscriptionsApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(WebhookSubscriptionsApi, self).__init__(config)

    def list_webhook_event_types(self,
                                 api_version=None):
        """Does a GET request to /v2/webhooks/event-types.

        Lists all webhook event types that can be subscribed to.

        Args:
            api_version (str, optional): The API version for which to list
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/webhooks/event-types')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('api_version')
                         .value(api_version))
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

    def list_webhook_subscriptions(self,
                                   cursor=None,
                                   include_disabled=False,
                                   sort_order=None,
                                   limit=None):
        """Does a GET request to /v2/webhooks/subscriptions.

        Lists all webhook subscriptions owned by your application.

        Args:
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this to retrieve the next set
                of results for your original query.  For more information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            include_disabled (bool, optional): Includes disabled
                [Subscription](entity:WebhookSubscription)s. By default, all
                enabled [Subscription](entity:WebhookSubscription)s are
                returned.
            sort_order (SortOrder, optional): Sorts the returned list by when
                the [Subscription](entity:WebhookSubscription) was created
                with the specified order. This field defaults to ASC.
            limit (int, optional): The maximum number of results to be
                returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default
                value of 100 is also the maximum allowed value.  Default: 100

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
            .path('/v2/webhooks/subscriptions')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('include_disabled')
                         .value(include_disabled))
            .query_param(Parameter()
                         .key('sort_order')
                         .value(sort_order))
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/webhooks/subscriptions')
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

    def delete_webhook_subscription(self,
                                    subscription_id):
        """Does a DELETE request to /v2/webhooks/subscriptions/{subscription_id}.

        Deletes a webhook subscription.

        Args:
            subscription_id (str): [REQUIRED] The ID of the
                [Subscription](entity:WebhookSubscription) to delete.

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
            .path('/v2/webhooks/subscriptions/{subscription_id}')
            .http_method(HttpMethodEnum.DELETE)
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

    def retrieve_webhook_subscription(self,
                                      subscription_id):
        """Does a GET request to /v2/webhooks/subscriptions/{subscription_id}.

        Retrieves a webhook subscription identified by its ID.

        Args:
            subscription_id (str): [REQUIRED] The ID of the
                [Subscription](entity:WebhookSubscription) to retrieve.

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
            .path('/v2/webhooks/subscriptions/{subscription_id}')
            .http_method(HttpMethodEnum.GET)
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

    def update_webhook_subscription(self,
                                    subscription_id,
                                    body):
        """Does a PUT request to /v2/webhooks/subscriptions/{subscription_id}.

        Updates a webhook subscription.

        Args:
            subscription_id (str): [REQUIRED] The ID of the
                [Subscription](entity:WebhookSubscription) to update.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/webhooks/subscriptions/{subscription_id}')
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

    def update_webhook_subscription_signature_key(self,
                                                  subscription_id,
                                                  body):
        """Does a POST request to /v2/webhooks/subscriptions/{subscription_id}/signature-key.

        Updates a webhook subscription by replacing the existing signature key
        with a new one.

        Args:
            subscription_id (str): [REQUIRED] The ID of the
                [Subscription](entity:WebhookSubscription) to update.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/webhooks/subscriptions/{subscription_id}/signature-key')
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

    def test_webhook_subscription(self,
                                  subscription_id,
                                  body):
        """Does a POST request to /v2/webhooks/subscriptions/{subscription_id}/test.

        Tests a webhook subscription by sending a test event to the
        notification URL.

        Args:
            subscription_id (str): [REQUIRED] The ID of the
                [Subscription](entity:WebhookSubscription) to test.
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

        return super().new_api_call_builder.request(
            RequestBuilder().server('default')
            .path('/v2/webhooks/subscriptions/{subscription_id}/test')
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
