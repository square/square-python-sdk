# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .destination_type import DestinationType
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Destination(UncheckedBaseModel):
    """
    Information about the destination against which the payout was made.
    """

    type: typing.Optional[DestinationType] = pydantic.Field(default=None)
    """
    Type of the destination such as a bank account or debit card.
    See [DestinationType](#type-destinationtype) for possible values
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Square issued unique ID (also known as the instrument ID) associated with this destination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
