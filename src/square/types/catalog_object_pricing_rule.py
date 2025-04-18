# This file was auto-generated by Fern from our API Definition.

from .catalog_object_base import CatalogObjectBase
import typing
from .catalog_pricing_rule import CatalogPricingRule
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CatalogObjectPricingRule(CatalogObjectBase):
    pricing_rule_data: typing.Optional[CatalogPricingRule] = pydantic.Field(default=None)
    """
    Structured data for a `CatalogPricingRule`, set for CatalogObjects of type `PRICING_RULE`.
    A `CatalogPricingRule` object often works with a `CatalogProductSet` object or a `CatalogTimePeriod` object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
