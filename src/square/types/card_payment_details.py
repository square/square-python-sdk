# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .card import Card
from .device_details import DeviceDetails
from .card_payment_timeline import CardPaymentTimeline
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CardPaymentDetails(UncheckedBaseModel):
    """
    Reflects the current status of a card payment. Contains only non-confidential information.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The card payment's current state. The state can be AUTHORIZED, CAPTURED, VOIDED, or
    FAILED.
    """

    card: typing.Optional[Card] = pydantic.Field(default=None)
    """
    The credit card's non-confidential details.
    """

    entry_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    The method used to enter the card's details for the payment. The method can be
    `KEYED`, `SWIPED`, `EMV`, `ON_FILE`, or `CONTACTLESS`.
    """

    cvv_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status code returned from the Card Verification Value (CVV) check. The code can be
    `CVV_ACCEPTED`, `CVV_REJECTED`, or `CVV_NOT_CHECKED`.
    """

    avs_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status code returned from the Address Verification System (AVS) check. The code can be
    `AVS_ACCEPTED`, `AVS_REJECTED`, or `AVS_NOT_CHECKED`.
    """

    auth_result_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status code returned by the card issuer that describes the payment's
    authorization status.
    """

    application_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the application ID identifies the EMV application used for the payment.
    """

    application_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the human-readable name of the EMV application used for the payment.
    """

    application_cryptogram: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the cryptogram generated for the payment.
    """

    verification_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the method used to verify the cardholder's identity. The method can be
    `PIN`, `SIGNATURE`, `PIN_AND_SIGNATURE`, `ON_DEVICE`, or `NONE`.
    """

    verification_results: typing.Optional[str] = pydantic.Field(default=None)
    """
    For EMV payments, the results of the cardholder verification. The result can be
    `SUCCESS`, `FAILURE`, or `UNKNOWN`.
    """

    statement_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The statement description sent to the card networks.
    
    Note: The actual statement description varies and is likely to be truncated and appended with
    additional information on a per issuer basis.
    """

    device_details: typing.Optional[DeviceDetails] = pydantic.Field(default=None)
    """
    __Deprecated__: Use `Payment.device_details` instead.
    
    Details about the device that took the payment.
    """

    card_payment_timeline: typing.Optional[CardPaymentTimeline] = pydantic.Field(default=None)
    """
    The timeline for card payments.
    """

    refund_requires_card_presence: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the card must be physically present for the payment to
    be refunded.  If set to `true`, the card must be present.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
