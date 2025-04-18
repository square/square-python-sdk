# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CashAppDetails(UncheckedBaseModel):
    """
    Additional details about `WALLET` type payments with the `brand` of `CASH_APP`.
    """

    buyer_full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the Cash App account holder.
    """

    buyer_country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country of the Cash App account holder, in ISO 3166-1-alpha-2 format.
    
    For possible values, see [Country](entity:Country).
    """

    buyer_cashtag: typing.Optional[str] = pydantic.Field(default=None)
    """
    $Cashtag of the Cash App account holder.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
