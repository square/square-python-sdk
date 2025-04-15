# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .payment_refund import PaymentRefund
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListPaymentRefundsResponse(UncheckedBaseModel):
    """
    Defines the response returned by [ListPaymentRefunds](api-endpoint:Refunds-ListPaymentRefunds).

    Either `errors` or `refunds` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    refunds: typing.Optional[typing.List[PaymentRefund]] = pydantic.Field(default=None)
    """
    The list of requested refunds.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The pagination cursor to be used in a subsequent request. If empty,
    this is the final response.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
