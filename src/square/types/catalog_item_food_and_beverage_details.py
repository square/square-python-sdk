# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .catalog_item_food_and_beverage_details_dietary_preference import (
    CatalogItemFoodAndBeverageDetailsDietaryPreference,
)
from .catalog_item_food_and_beverage_details_ingredient import CatalogItemFoodAndBeverageDetailsIngredient
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CatalogItemFoodAndBeverageDetails(UncheckedBaseModel):
    """
    The food and beverage-specific details of a `FOOD_AND_BEV` item.
    """

    calorie_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The calorie count (in the unit of kcal) for the `FOOD_AND_BEV` type of items.
    """

    dietary_preferences: typing.Optional[typing.List[CatalogItemFoodAndBeverageDetailsDietaryPreference]] = (
        pydantic.Field(default=None)
    )
    """
    The dietary preferences for the `FOOD_AND_BEV` item.
    """

    ingredients: typing.Optional[typing.List[CatalogItemFoodAndBeverageDetailsIngredient]] = pydantic.Field(
        default=None
    )
    """
    The ingredients for the `FOOD_AND_BEV` type item.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
