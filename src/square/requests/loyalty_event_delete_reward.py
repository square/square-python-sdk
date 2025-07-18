# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions


class LoyaltyEventDeleteRewardParams(typing_extensions.TypedDict):
    """
    Provides metadata when the event `type` is `DELETE_REWARD`.
    """

    loyalty_program_id: typing_extensions.NotRequired[str]
    """
    The ID of the [loyalty program](entity:LoyaltyProgram).
    """

    reward_id: typing_extensions.NotRequired[str]
    """
    The ID of the deleted [loyalty reward](entity:LoyaltyReward).
    This field is returned only if the event source is `LOYALTY_API`.
    """

    points: typing_extensions.NotRequired[int]
    """
    The number of points returned to the loyalty account.
    """
