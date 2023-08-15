# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.utilities.file_wrapper import FileWrapper
from square.api.base_api import BaseApi
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from square.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or


class DisputesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config):
        super(DisputesApi, self).__init__(config)

    def list_disputes(self,
                      cursor=None,
                      states=None,
                      location_id=None):
        """Does a GET request to /v2/disputes.

        Returns a list of disputes associated with a particular account.

        Args:
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query. For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).
            states (DisputeState, optional): The dispute states used to filter
                the result. If not specified, the endpoint returns all
                disputes.
            location_id (str, optional): The ID of the location for which to
                return a list of disputes. If not specified, the endpoint
                returns disputes associated with all locations.

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
            .path('/v2/disputes')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
            .query_param(Parameter()
                         .key('states')
                         .value(states))
            .query_param(Parameter()
                         .key('location_id')
                         .value(location_id))
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

    def retrieve_dispute(self,
                         dispute_id):
        """Does a GET request to /v2/disputes/{dispute_id}.

        Returns details about a specific dispute.

        Args:
            dispute_id (str): The ID of the dispute you want more details
                about.

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
            .path('/v2/disputes/{dispute_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
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

    def accept_dispute(self,
                       dispute_id):
        """Does a POST request to /v2/disputes/{dispute_id}/accept.

        Accepts the loss on a dispute. Square returns the disputed amount to
        the cardholder and
        updates the dispute state to ACCEPTED.
        Square debits the disputed amount from the seller’s Square account. If
        the Square account
        does not have sufficient funds, Square debits the associated bank
        account.

        Args:
            dispute_id (str): The ID of the dispute you want to accept.

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
            .path('/v2/disputes/{dispute_id}/accept')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
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

    def list_dispute_evidence(self,
                              dispute_id,
                              cursor=None):
        """Does a GET request to /v2/disputes/{dispute_id}/evidence.

        Returns a list of evidence associated with a dispute.

        Args:
            dispute_id (str): The ID of the dispute.
            cursor (str, optional): A pagination cursor returned by a previous
                call to this endpoint. Provide this cursor to retrieve the
                next set of results for the original query. For more
                information, see
                [Pagination](https://developer.squareup.com/docs/build-basics/c
                ommon-api-patterns/pagination).

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
            .path('/v2/disputes/{dispute_id}/evidence')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('cursor')
                         .value(cursor))
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

    def create_dispute_evidence_file(self,
                                     dispute_id,
                                     request=None,
                                     image_file=None):
        """Does a POST request to /v2/disputes/{dispute_id}/evidence-files.

        Uploads a file to use as evidence in a dispute challenge. The endpoint
        accepts HTTP
        multipart/form-data file uploads in HEIC, HEIF, JPEG, PDF, PNG, and
        TIFF formats.

        Args:
            dispute_id (str): The ID of the dispute for which you want to
                upload evidence.
            request (CreateDisputeEvidenceFileRequest, optional): Defines the
                parameters for a `CreateDisputeEvidenceFile` request.
            image_file (typing.BinaryIO, optional): TODO: type description
                here.

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
            .path('/v2/disputes/{dispute_id}/evidence-files')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
                            .should_encode(True))
            .multipart_param(Parameter()
                             .key('request')
                             .value(APIHelper.json_serialize(request))
                             .default_content_type('application/json; charset=utf-8'))
            .multipart_param(Parameter()
                             .key('image_file')
                             .value(image_file)
                             .default_content_type('image/jpeg'))
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

    def create_dispute_evidence_text(self,
                                     dispute_id,
                                     body):
        """Does a POST request to /v2/disputes/{dispute_id}/evidence-text.

        Uploads text to use as evidence for a dispute challenge.

        Args:
            dispute_id (str): The ID of the dispute for which you want to
                upload evidence.
            body (CreateDisputeEvidenceTextRequest): An object containing the
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
            .path('/v2/disputes/{dispute_id}/evidence-text')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
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

    def delete_dispute_evidence(self,
                                dispute_id,
                                evidence_id):
        """Does a DELETE request to /v2/disputes/{dispute_id}/evidence/{evidence_id}.

        Removes specified evidence from a dispute.
        Square does not send the bank any evidence that is removed.

        Args:
            dispute_id (str): The ID of the dispute from which you want to
                remove evidence.
            evidence_id (str): The ID of the evidence you want to remove.

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
            .path('/v2/disputes/{dispute_id}/evidence/{evidence_id}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('evidence_id')
                            .value(evidence_id)
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

    def retrieve_dispute_evidence(self,
                                  dispute_id,
                                  evidence_id):
        """Does a GET request to /v2/disputes/{dispute_id}/evidence/{evidence_id}.

        Returns the metadata for the evidence specified in the request URL
        path.
        You must maintain a copy of any evidence uploaded if you want to
        reference it later. Evidence cannot be downloaded after you upload
        it.

        Args:
            dispute_id (str): The ID of the dispute from which you want to
                retrieve evidence metadata.
            evidence_id (str): The ID of the evidence to retrieve.

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
            .path('/v2/disputes/{dispute_id}/evidence/{evidence_id}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('evidence_id')
                            .value(evidence_id)
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

    def submit_evidence(self,
                        dispute_id):
        """Does a POST request to /v2/disputes/{dispute_id}/submit-evidence.

        Submits evidence to the cardholder's bank.
        The evidence submitted by this endpoint includes evidence uploaded
        using the
        [CreateDisputeEvidenceFile]($e/Disputes/CreateDisputeEvidenceFile)
        and
        [CreateDisputeEvidenceText]($e/Disputes/CreateDisputeEvidenceText)
        endpoints and
        evidence automatically provided by Square, when available. Evidence
        cannot be removed from
        a dispute after submission.

        Args:
            dispute_id (str): The ID of the dispute for which you want to
                submit evidence.

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
            .path('/v2/disputes/{dispute_id}/submit-evidence')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('dispute_id')
                            .value(dispute_id)
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
