# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class LoyaltyAccountExpiringPointDeadline(UncheckedBaseModel):
    """
    Represents a set of points for a loyalty account that are scheduled to expire on a specific date.
    """

    points: int = pydantic.Field()
    """
    The number of points scheduled to expire at the `expires_at` timestamp.
    """

    expires_at: str = pydantic.Field()
    """
    The timestamp of when the points are scheduled to expire, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
