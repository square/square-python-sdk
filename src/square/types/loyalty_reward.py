# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .loyalty_reward_status import LoyaltyRewardStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LoyaltyReward(UncheckedBaseModel):
    """
    Represents a contract to redeem loyalty points for a [reward tier](entity:LoyaltyProgramRewardTier) discount. Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state.
    For more information, see [Manage loyalty rewards](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards).
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the loyalty reward.
    """

    status: typing.Optional[LoyaltyRewardStatus] = pydantic.Field(default=None)
    """
    The status of a loyalty reward.
    See [LoyaltyRewardStatus](#type-loyaltyrewardstatus) for possible values
    """

    loyalty_account_id: str = pydantic.Field()
    """
    The Square-assigned ID of the [loyalty account](entity:LoyaltyAccount) to which the reward belongs.
    """

    reward_tier_id: str = pydantic.Field()
    """
    The Square-assigned ID of the [reward tier](entity:LoyaltyProgramRewardTier) used to create the reward.
    """

    points: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of loyalty points used for the reward.
    """

    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-assigned ID of the [order](entity:Order) to which the reward is attached.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the reward was created, in RFC 3339 format.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the reward was last updated, in RFC 3339 format.
    """

    redeemed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when the reward was redeemed, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
