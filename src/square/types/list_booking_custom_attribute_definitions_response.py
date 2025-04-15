# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .custom_attribute_definition import CustomAttributeDefinition
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListBookingCustomAttributeDefinitionsResponse(UncheckedBaseModel):
    """
    Represents a [ListBookingCustomAttributeDefinitions](api-endpoint:BookingCustomAttributes-ListBookingCustomAttributeDefinitions) response.
    Either `custom_attribute_definitions`, an empty object, or `errors` is present in the response.
    If additional results are available, the `cursor` field is also present along with `custom_attribute_definitions`.
    """

    custom_attribute_definitions: typing.Optional[typing.List[CustomAttributeDefinition]] = pydantic.Field(default=None)
    """
    The retrieved custom attribute definitions. If no custom attribute definitions are found,
    Square returns an empty object (`{}`).
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The cursor to provide in your next call to this endpoint to retrieve the next page of
    results for your original request. This field is present only if the request succeeded and
    additional results are available. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
