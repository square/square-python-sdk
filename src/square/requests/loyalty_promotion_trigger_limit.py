# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.loyalty_promotion_trigger_limit_interval import LoyaltyPromotionTriggerLimitInterval


class LoyaltyPromotionTriggerLimitParams(typing_extensions.TypedDict):
    """
    Represents the number of times a buyer can earn points during a [loyalty promotion](entity:LoyaltyPromotion).
    If this field is not set, buyers can trigger the promotion an unlimited number of times to earn points during
    the time that the promotion is available.

    A purchase that is disqualified from earning points because of this limit might qualify for another active promotion.
    """

    times: int
    """
    The maximum number of times a buyer can trigger the promotion during the specified `interval`.
    """

    interval: typing_extensions.NotRequired[LoyaltyPromotionTriggerLimitInterval]
    """
    The time period the limit applies to.
    See [LoyaltyPromotionTriggerLimitInterval](#type-loyaltypromotiontriggerlimitinterval) for possible values
    """
