# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .tender_square_account_details_status import TenderSquareAccountDetailsStatus
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TenderSquareAccountDetails(UncheckedBaseModel):
    """
    Represents the details of a tender with `type` `SQUARE_ACCOUNT`.
    """

    status: typing.Optional[TenderSquareAccountDetailsStatus] = pydantic.Field(default=None)
    """
    The Square Account payment's current state (such as `AUTHORIZED` or
    `CAPTURED`). See [TenderSquareAccountDetailsStatus](entity:TenderSquareAccountDetailsStatus)
    for possible values.
    See [Status](#type-status) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
