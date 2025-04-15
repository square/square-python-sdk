# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .payment import Payment
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdatePaymentResponse(UncheckedBaseModel):
    """
    Defines the response returned by
    [UpdatePayment](api-endpoint:Payments-UpdatePayment).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    payment: typing.Optional[Payment] = pydantic.Field(default=None)
    """
    The updated payment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
