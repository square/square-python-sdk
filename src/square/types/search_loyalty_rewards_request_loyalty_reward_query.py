# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from .loyalty_reward_status import LoyaltyRewardStatus
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchLoyaltyRewardsRequestLoyaltyRewardQuery(UncheckedBaseModel):
    """
    The set of search requirements.
    """

    loyalty_account_id: str = pydantic.Field()
    """
    The ID of the [loyalty account](entity:LoyaltyAccount) to which the loyalty reward belongs.
    """

    status: typing.Optional[LoyaltyRewardStatus] = pydantic.Field(default=None)
    """
    The status of the loyalty reward.
    See [LoyaltyRewardStatus](#type-loyaltyrewardstatus) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
