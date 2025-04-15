# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.loyalty_program_status import LoyaltyProgramStatus
import typing
from .loyalty_program_reward_tier import LoyaltyProgramRewardTierParams
from .loyalty_program_expiration_policy import LoyaltyProgramExpirationPolicyParams
from .loyalty_program_terminology import LoyaltyProgramTerminologyParams
from .loyalty_program_accrual_rule import LoyaltyProgramAccrualRuleParams


class LoyaltyProgramParams(typing_extensions.TypedDict):
    """
    Represents a Square loyalty program. Loyalty programs define how buyers can earn points and redeem points for rewards.
    Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard.
    For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).
    """

    id: typing_extensions.NotRequired[str]
    """
    The Square-assigned ID of the loyalty program. Updates to 
    the loyalty program do not modify the identifier.
    """

    status: typing_extensions.NotRequired[LoyaltyProgramStatus]
    """
    Whether the program is currently active.
    See [LoyaltyProgramStatus](#type-loyaltyprogramstatus) for possible values
    """

    reward_tiers: typing_extensions.NotRequired[typing.Optional[typing.Sequence[LoyaltyProgramRewardTierParams]]]
    """
    The list of rewards for buyers, sorted by ascending points.
    """

    expiration_policy: typing_extensions.NotRequired[LoyaltyProgramExpirationPolicyParams]
    """
    If present, details for how points expire.
    """

    terminology: typing_extensions.NotRequired[LoyaltyProgramTerminologyParams]
    """
    A cosmetic name for the “points” currency.
    """

    location_ids: typing_extensions.NotRequired[typing.Optional[typing.Sequence[str]]]
    """
    The [locations](entity:Location) at which the program is active.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the program was created, in RFC 3339 format.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the reward was last updated, in RFC 3339 format.
    """

    accrual_rules: typing_extensions.NotRequired[typing.Optional[typing.Sequence[LoyaltyProgramAccrualRuleParams]]]
    """
    Defines how buyers can earn loyalty points from the base loyalty program.
    To check for associated [loyalty promotions](entity:LoyaltyPromotion) that enable
    buyers to earn extra points, call [ListLoyaltyPromotions](api-endpoint:Loyalty-ListLoyaltyPromotions).
    """
