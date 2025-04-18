# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .get_customer_response import GetCustomerResponse
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BulkRetrieveCustomersResponse(UncheckedBaseModel):
    """
    Defines the fields included in the response body from the
    [BulkRetrieveCustomers](api-endpoint:Customers-BulkRetrieveCustomers) endpoint.
    """

    responses: typing.Optional[typing.Dict[str, GetCustomerResponse]] = pydantic.Field(default=None)
    """
    A map of responses that correspond to individual retrieve requests, represented by
    key-value pairs.
    
    Each key is the customer ID that was specified for a retrieve request and each value
    is the corresponding response.
    If the request succeeds, the value is the requested customer profile.
    If the request fails, the value contains any errors that occurred during the request.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any top-level errors that prevented the bulk operation from running.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
