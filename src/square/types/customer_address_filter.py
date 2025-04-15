# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .customer_text_filter import CustomerTextFilter
import pydantic
from .country import Country
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CustomerAddressFilter(UncheckedBaseModel):
    """
    The customer address filter. This filter is used in a [CustomerCustomAttributeFilterValue](entity:CustomerCustomAttributeFilterValue) filter when
    searching by an `Address`-type custom attribute.
    """

    postal_code: typing.Optional[CustomerTextFilter] = pydantic.Field(default=None)
    """
    The postal code to search for. Only an `exact` match is supported.
    """

    country: typing.Optional[Country] = pydantic.Field(default=None)
    """
    The country code to search for.
    See [Country](#type-country) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
