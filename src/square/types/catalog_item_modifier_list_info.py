# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from .catalog_modifier_override import CatalogModifierOverride
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CatalogItemModifierListInfo(UncheckedBaseModel):
    """
    References a text-based modifier or a list of non text-based modifiers applied to a `CatalogItem` instance
    and specifies supported behaviors of the application.
    """

    modifier_list_id: str = pydantic.Field()
    """
    The ID of the `CatalogModifierList` controlled by this `CatalogModifierListInfo`.
    """

    modifier_overrides: typing.Optional[typing.List[CatalogModifierOverride]] = pydantic.Field(default=None)
    """
    A set of `CatalogModifierOverride` objects that override whether a given `CatalogModifier` is enabled by default.
    """

    min_selected_modifiers: typing.Optional[int] = pydantic.Field(default=None)
    """
    If 0 or larger, the smallest number of `CatalogModifier`s that must be selected from this `CatalogModifierList`.
    The default value is `-1`.
    
    When  `CatalogModifierList.selection_type` is `MULTIPLE`, `CatalogModifierListInfo.min_selected_modifiers=-1` 
    and `CatalogModifierListInfo.max_selected_modifier=-1` means that from zero to the maximum number of modifiers of
    the `CatalogModifierList` can be selected from the `CatalogModifierList`. 
    
    When the `CatalogModifierList.selection_type` is `SINGLE`, `CatalogModifierListInfo.min_selected_modifiers=-1`
    and `CatalogModifierListInfo.max_selected_modifier=-1` means that exactly one modifier must be present in 
    and can be selected from the `CatalogModifierList`
    """

    max_selected_modifiers: typing.Optional[int] = pydantic.Field(default=None)
    """
    If 0 or larger, the largest number of `CatalogModifier`s that can be selected from this `CatalogModifierList`.
    The default value is `-1`.
    
    When  `CatalogModifierList.selection_type` is `MULTIPLE`, `CatalogModifierListInfo.min_selected_modifiers=-1` 
    and `CatalogModifierListInfo.max_selected_modifier=-1` means that from zero to the maximum number of modifiers of
    the `CatalogModifierList` can be selected from the `CatalogModifierList`. 
    
    When the `CatalogModifierList.selection_type` is `SINGLE`, `CatalogModifierListInfo.min_selected_modifiers=-1`
    and `CatalogModifierListInfo.max_selected_modifier=-1` means that exactly one modifier must be present in 
    and can be selected from the `CatalogModifierList`
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `true`, enable this `CatalogModifierList`. The default value is `true`.
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    The position of this `CatalogItemModifierListInfo` object within the `modifier_list_info` list applied 
    to a `CatalogItem` instance.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
