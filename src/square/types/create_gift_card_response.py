# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .gift_card import GiftCard
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateGiftCardResponse(UncheckedBaseModel):
    """
    A response that contains a `GiftCard`. The response might contain a set of `Error` objects if the request
    resulted in errors.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    gift_card: typing.Optional[GiftCard] = pydantic.Field(default=None)
    """
    The new gift card.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
