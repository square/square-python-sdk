# -*- coding: utf-8 -*-

from square.api_helper import APIHelper
from square.http.api_response import ApiResponse
from square.utilities.file_wrapper import FileWrapper
from square.api.base_api import BaseApi


class DisputesApi(BaseApi):

    """A Controller to access Endpoints in the square API."""
    def __init__(self, config, auth_managers):
        super(DisputesApi, self).__init__(config, auth_managers)

    def list_disputes(self,
                      cursor=None,
                      states=None,
                      location_id=None):
        """Does a GET request to /v2/disputes.

        Returns a list of disputes associated with a particular account.

        Args:
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for the original query. For
                more information, see
                [Pagination](https://developer.squareup.com/docs/basics/api101/
                pagination).
            states (DisputeState, optional): The dispute states used to filter
                the result. If not specified, the endpoint returns all
                disputes.
            location_id (string, optional): The ID of the location for which
                to return a list of disputes. If not specified, the endpoint
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

        # Prepare query URL
        _url_path = '/v2/disputes'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor,
            'states': states,
            'location_id': location_id
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

    def retrieve_dispute(self,
                         dispute_id):
        """Does a GET request to /v2/disputes/{dispute_id}.

        Returns details about a specific dispute.

        Args:
            dispute_id (string): The ID of the dispute you want more details
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

        # Prepare query URL
        _url_path = '/v2/disputes/{dispute_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True}
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
            dispute_id (string): The ID of the dispute you want to accept.

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
        _url_path = '/v2/disputes/{dispute_id}/accept'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True}
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

    def list_dispute_evidence(self,
                              dispute_id,
                              cursor=None):
        """Does a GET request to /v2/disputes/{dispute_id}/evidence.

        Returns a list of evidence associated with a dispute.

        Args:
            dispute_id (string): The ID of the dispute.
            cursor (string, optional): A pagination cursor returned by a
                previous call to this endpoint. Provide this cursor to
                retrieve the next set of results for the original query. For
                more information, see
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

        # Prepare query URL
        _url_path = '/v2/disputes/{dispute_id}/evidence'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_parameters = {
            'cursor': cursor
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
            dispute_id (string): The ID of the dispute for which you want to
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

        # Prepare query URL
        _url_path = '/v2/disputes/{dispute_id}/evidence-files'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        if isinstance(image_file, FileWrapper):
            image_file_wrapper = image_file.file_stream
            image_file_content_type = image_file.content_type
        else:
            image_file_wrapper = image_file
            image_file_content_type = 'image/jpeg'

        # Prepare files
        _files = {
            'request': (None, APIHelper.json_serialize(request), 'application/json; charset=utf-8'),
            'image_file': (image_file_wrapper.name, image_file_wrapper, image_file_content_type)
        }

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, files=_files)
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

    def create_dispute_evidence_text(self,
                                     dispute_id,
                                     body):
        """Does a POST request to /v2/disputes/{dispute_id}/evidence-text.

        Uploads text to use as evidence for a dispute challenge.

        Args:
            dispute_id (string): The ID of the dispute for which you want to
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

        # Prepare query URL
        _url_path = '/v2/disputes/{dispute_id}/evidence-text'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True}
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

    def delete_dispute_evidence(self,
                                dispute_id,
                                evidence_id):
        """Does a DELETE request to /v2/disputes/{dispute_id}/evidence/{evidence_id}.

        Removes specified evidence from a dispute.
        Square does not send the bank any evidence that is removed.

        Args:
            dispute_id (string): The ID of the dispute from which you want to
                remove evidence.
            evidence_id (string): The ID of the evidence you want to remove.

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
        _url_path = '/v2/disputes/{dispute_id}/evidence/{evidence_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True},
            'evidence_id': {'value': evidence_id, 'encode': True}
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
            dispute_id (string): The ID of the dispute from which you want to
                retrieve evidence metadata.
            evidence_id (string): The ID of the evidence to retrieve.

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
        _url_path = '/v2/disputes/{dispute_id}/evidence/{evidence_id}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True},
            'evidence_id': {'value': evidence_id, 'encode': True}
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
            dispute_id (string): The ID of the dispute for which you want to
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

        # Prepare query URL
        _url_path = '/v2/disputes/{dispute_id}/submit-evidence'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'dispute_id': {'value': dispute_id, 'encode': True}
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
