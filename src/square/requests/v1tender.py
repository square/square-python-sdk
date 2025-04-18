# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.v1tender_type import V1TenderType
import typing
from ..types.v1tender_card_brand import V1TenderCardBrand
from ..types.v1tender_entry_method import V1TenderEntryMethod
from .v1money import V1MoneyParams


class V1TenderParams(typing_extensions.TypedDict):
    """
    A tender represents a discrete monetary exchange. Square represents this
    exchange as a money object with a specific currency and amount, where the
    amount is given in the smallest denomination of the given currency.

    Square POS can accept more than one form of tender for a single payment (such
    as by splitting a bill between a credit card and a gift card). The `tender`
    field of the Payment object lists all forms of tender used for the payment.

    Split tender payments behave slightly differently from single tender payments:

    The receipt_url for a split tender corresponds only to the first tender listed
    in the tender field. To get the receipt URLs for the remaining tenders, use
    the receipt_url fields of the corresponding Tender objects.

    *A note on gift cards**: when a customer purchases a Square gift card from a
    merchant, the merchant receives the full amount of the gift card in the
    associated payment.

    When that gift card is used as a tender, the balance of the gift card is
    reduced and the merchant receives no funds. A `Tender` object with a type of
    `SQUARE_GIFT_CARD` indicates a gift card was used for some or all of the
    associated payment.
    """

    id: typing_extensions.NotRequired[str]
    """
    The tender's unique ID.
    """

    type: typing_extensions.NotRequired[V1TenderType]
    """
    The type of tender.
    See [V1TenderType](#type-v1tendertype) for possible values
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A human-readable description of the tender.
    """

    employee_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the employee that processed the tender.
    """

    receipt_url: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The URL of the receipt for the tender.
    """

    card_brand: typing_extensions.NotRequired[V1TenderCardBrand]
    """
    The brand of credit card provided.
    See [V1TenderCardBrand](#type-v1tendercardbrand) for possible values
    """

    pan_suffix: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The last four digits of the provided credit card's account number.
    """

    entry_method: typing_extensions.NotRequired[V1TenderEntryMethod]
    """
    The tender's unique ID.
    See [V1TenderEntryMethod](#type-v1tenderentrymethod) for possible values
    """

    payment_note: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Notes entered by the merchant about the tender at the time of payment, if any. Typically only present for tender with the type: OTHER.
    """

    total_money: typing_extensions.NotRequired[V1MoneyParams]
    """
    The total amount of money provided in this form of tender.
    """

    tendered_money: typing_extensions.NotRequired[V1MoneyParams]
    """
    The amount of total_money applied to the payment.
    """

    tendered_at: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The time when the tender was created, in ISO 8601 format.
    """

    settled_at: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The time when the tender was settled, in ISO 8601 format.
    """

    change_back_money: typing_extensions.NotRequired[V1MoneyParams]
    """
    The amount of total_money returned to the buyer as change.
    """

    refunded_money: typing_extensions.NotRequired[V1MoneyParams]
    """
    The total of all refunds applied to this tender. This amount is always negative or zero.
    """

    is_exchange: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Indicates whether or not the tender is associated with an exchange. If is_exchange is true, the tender represents the value of goods returned in an exchange not the actual money paid. The exchange value reduces the tender amounts needed to pay for items purchased in the exchange.
    """
