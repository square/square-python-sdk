# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .loyalty_program_reward_definition import LoyaltyProgramRewardDefinitionParams
from .catalog_object_reference import CatalogObjectReferenceParams


class LoyaltyProgramRewardTierParams(typing_extensions.TypedDict):
    """
    Represents a reward tier in a loyalty program. A reward tier defines how buyers can redeem points for a reward, such as the number of points required and the value and scope of the discount. A loyalty program can offer multiple reward tiers.
    """

    id: typing_extensions.NotRequired[str]
    """
    The Square-assigned ID of the reward tier.
    """

    points: int
    """
    The points exchanged for the reward tier.
    """

    name: typing_extensions.NotRequired[str]
    """
    The name of the reward tier.
    """

    definition: typing_extensions.NotRequired[LoyaltyProgramRewardDefinitionParams]
    """
    Provides details about the reward tier definition.
    DEPRECATED at version 2020-12-16. Replaced by the `pricing_rule_reference` field.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the reward tier was created, in RFC 3339 format.
    """

    pricing_rule_reference: CatalogObjectReferenceParams
    """
    A reference to the specific version of a `PRICING_RULE` catalog object that contains information about the reward tier discount.
    
    Use `object_id` and `catalog_version` with the [RetrieveCatalogObject](api-endpoint:Catalog-RetrieveCatalogObject) endpoint
    to get discount details. Make sure to set `include_related_objects` to true in the request to retrieve all catalog objects
    that define the discount. For more information, see [Getting discount details for a reward tier](https://developer.squareup.com/docs/loyalty-api/loyalty-rewards#get-discount-details).
    """
