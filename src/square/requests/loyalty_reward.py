# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.loyalty_reward_status import LoyaltyRewardStatus
import typing


class LoyaltyRewardParams(typing_extensions.TypedDict):
    """
    Represents a contract to redeem loyalty points for a [reward tier](entity:LoyaltyProgramRewardTier) discount. Loyalty rewards can be in an ISSUED, REDEEMED, or DELETED state.
    For more information, see [Manage loyalty rewards](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards).
    """

    id: typing_extensions.NotRequired[str]
    """
    The Square-assigned ID of the loyalty reward.
    """

    status: typing_extensions.NotRequired[LoyaltyRewardStatus]
    """
    The status of a loyalty reward.
    See [LoyaltyRewardStatus](#type-loyaltyrewardstatus) for possible values
    """

    loyalty_account_id: str
    """
    The Square-assigned ID of the [loyalty account](entity:LoyaltyAccount) to which the reward belongs.
    """

    reward_tier_id: str
    """
    The Square-assigned ID of the [reward tier](entity:LoyaltyProgramRewardTier) used to create the reward.
    """

    points: typing_extensions.NotRequired[int]
    """
    The number of loyalty points used for the reward.
    """

    order_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The Square-assigned ID of the [order](entity:Order) to which the reward is attached.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the reward was created, in RFC 3339 format.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the reward was last updated, in RFC 3339 format.
    """

    redeemed_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the reward was redeemed, in RFC 3339 format.
    """
