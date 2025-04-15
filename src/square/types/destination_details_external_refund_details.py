# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DestinationDetailsExternalRefundDetails(UncheckedBaseModel):
    """
    Stores details about an external refund. Contains only non-confidential information.
    """

    type: str = pydantic.Field()
    """
    The type of external refund the seller paid to the buyer. It can be one of the
    following:
    - CHECK - Refunded using a physical check.
    - BANK_TRANSFER - Refunded using external bank transfer.
    - OTHER\_GIFT\_CARD - Refunded using a non-Square gift card.
    - CRYPTO - Refunded using a crypto currency.
    - SQUARE_CASH - Refunded using Square Cash App.
    - SOCIAL - Refunded using peer-to-peer payment applications.
    - EXTERNAL - A third-party application gathered this refund outside of Square.
    - EMONEY - Refunded using an E-money provider.
    - CARD - A credit or debit card that Square does not support.
    - STORED_BALANCE - Use for house accounts, store credit, and so forth.
    - FOOD_VOUCHER - Restaurant voucher provided by employers to employees to pay for meals
    - OTHER - A type not listed here.
    """

    source: str = pydantic.Field()
    """
    A description of the external refund source. For example,
    "Food Delivery Service".
    """

    source_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An ID to associate the refund to its originating source.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
