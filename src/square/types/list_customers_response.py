# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .customer import Customer
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListCustomersResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the `ListCustomers` endpoint.

    Either `errors` or `customers` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    customers: typing.Optional[typing.List[Customer]] = pydantic.Field(default=None)
    """
    The customer profiles associated with the Square account or an empty object (`{}`) if none are found.
    Only customer profiles with public information (`given_name`, `family_name`, `company_name`, `email_address`, or
    `phone_number`) are included in the response.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor to retrieve the next set of results for the
    original query. A cursor is only present if the request succeeded and additional results
    are available.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total count of customers associated with the Square account. Only customer profiles with public information
    (`given_name`, `family_name`, `company_name`, `email_address`, or `phone_number`) are counted. This field is present
    only if `count` is set to `true` in the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
