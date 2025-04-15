# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .money import MoneyParams


class ExternalPaymentDetailsParams(typing_extensions.TypedDict):
    """
    Stores details about an external payment. Contains only non-confidential information.
    For more information, see
    [Take External Payments](https://developer.squareup.com/docs/payments-api/take-payments/external-payments).
    """

    type: str
    """
    The type of external payment the seller received. It can be one of the following:
    - CHECK - Paid using a physical check.
    - BANK_TRANSFER - Paid using external bank transfer.
    - OTHER\_GIFT\_CARD - Paid using a non-Square gift card.
    - CRYPTO - Paid using a crypto currency.
    - SQUARE_CASH - Paid using Square Cash App.
    - SOCIAL - Paid using peer-to-peer payment applications.
    - EXTERNAL - A third-party application gathered this payment outside of Square.
    - EMONEY - Paid using an E-money provider.
    - CARD - A credit or debit card that Square does not support.
    - STORED_BALANCE - Use for house accounts, store credit, and so forth.
    - FOOD_VOUCHER - Restaurant voucher provided by employers to employees to pay for meals
    - OTHER - A type not listed here.
    """

    source: str
    """
    A description of the external payment source. For example, 
    "Food Delivery Service".
    """

    source_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    An ID to associate the payment to its originating source.
    """

    source_fee_money: typing_extensions.NotRequired[MoneyParams]
    """
    The fees paid to the source. The `amount_money` minus this field is 
    the net amount seller receives.
    """
