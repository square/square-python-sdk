# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from ...core.http_response import HttpResponse
from ...types.get_employee_wage_response import GetEmployeeWageResponse
from ...core.jsonable_encoder import jsonable_encoder
from ...core.unchecked_base_model import construct_type
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper
from ...core.http_response import AsyncHttpResponse


class RawEmployeeWagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEmployeeWageResponse]:
        """
        Returns a single `EmployeeWage` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `EmployeeWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEmployeeWageResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/labor/employee-wages/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEmployeeWageResponse,
                    construct_type(
                        type_=GetEmployeeWageResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRawEmployeeWagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEmployeeWageResponse]:
        """
        Returns a single `EmployeeWage` specified by `id`.

        Parameters
        ----------
        id : str
            The UUID for the `EmployeeWage` being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEmployeeWageResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/labor/employee-wages/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEmployeeWageResponse,
                    construct_type(
                        type_=GetEmployeeWageResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
