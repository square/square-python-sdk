# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .card import CardParams
from .device_details import DeviceDetailsParams
from .card_payment_timeline import CardPaymentTimelineParams
from .error import ErrorParams


class CardPaymentDetailsParams(typing_extensions.TypedDict):
    """
    Reflects the current status of a card payment. Contains only non-confidential information.
    """

    status: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The card payment's current state. The state can be AUTHORIZED, CAPTURED, VOIDED, or
    FAILED.
    """

    card: typing_extensions.NotRequired[CardParams]
    """
    The credit card's non-confidential details.
    """

    entry_method: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The method used to enter the card's details for the payment. The method can be
    `KEYED`, `SWIPED`, `EMV`, `ON_FILE`, or `CONTACTLESS`.
    """

    cvv_status: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The status code returned from the Card Verification Value (CVV) check. The code can be
    `CVV_ACCEPTED`, `CVV_REJECTED`, or `CVV_NOT_CHECKED`.
    """

    avs_status: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The status code returned from the Address Verification System (AVS) check. The code can be
    `AVS_ACCEPTED`, `AVS_REJECTED`, or `AVS_NOT_CHECKED`.
    """

    auth_result_code: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The status code returned by the card issuer that describes the payment's
    authorization status.
    """

    application_identifier: typing_extensions.NotRequired[typing.Optional[str]]
    """
    For EMV payments, the application ID identifies the EMV application used for the payment.
    """

    application_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    For EMV payments, the human-readable name of the EMV application used for the payment.
    """

    application_cryptogram: typing_extensions.NotRequired[typing.Optional[str]]
    """
    For EMV payments, the cryptogram generated for the payment.
    """

    verification_method: typing_extensions.NotRequired[typing.Optional[str]]
    """
    For EMV payments, the method used to verify the cardholder's identity. The method can be
    `PIN`, `SIGNATURE`, `PIN_AND_SIGNATURE`, `ON_DEVICE`, or `NONE`.
    """

    verification_results: typing_extensions.NotRequired[typing.Optional[str]]
    """
    For EMV payments, the results of the cardholder verification. The result can be
    `SUCCESS`, `FAILURE`, or `UNKNOWN`.
    """

    statement_description: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The statement description sent to the card networks.
    
    Note: The actual statement description varies and is likely to be truncated and appended with
    additional information on a per issuer basis.
    """

    device_details: typing_extensions.NotRequired[DeviceDetailsParams]
    """
    __Deprecated__: Use `Payment.device_details` instead.
    
    Details about the device that took the payment.
    """

    card_payment_timeline: typing_extensions.NotRequired[CardPaymentTimelineParams]
    """
    The timeline for card payments.
    """

    refund_requires_card_presence: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Whether the card must be physically present for the payment to
    be refunded.  If set to `true`, the card must be present.
    """

    errors: typing_extensions.NotRequired[typing.Optional[typing.Sequence[ErrorParams]]]
    """
    Information about errors encountered during the request.
    """
