# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
import typing_extensions
import typing_extensions
import typing
from ..types.catalog_modifier_list_selection_type import CatalogModifierListSelectionType
from ..types.catalog_modifier_list_modifier_type import CatalogModifierListModifierType
import typing

if typing.TYPE_CHECKING:
    from .catalog_object import CatalogObjectParams


class CatalogModifierListParams(typing_extensions.TypedDict):
    """
    A container for a list of modifiers, or a text-based modifier.
    For text-based modifiers, this represents text configuration for an item. (For example, custom text to print on a t-shirt).
    For non text-based modifiers, this represents a list of modifiers that can be applied to items at the time of sale.
    (For example, a list of condiments for a hot dog, or a list of ice cream flavors).
    Each element of the modifier list is a `CatalogObject` instance of the `MODIFIER` type.
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the `CatalogModifierList` instance. This is a searchable attribute for use in applicable query filters, and its value length is of 
    Unicode code points.
    """

    ordinal: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The position of this `CatalogModifierList` within a list of `CatalogModifierList` instances.
    """

    selection_type: typing_extensions.NotRequired[CatalogModifierListSelectionType]
    """
    __Deprecated__: Indicates whether a single (`SINGLE`) modifier or multiple (`MULTIPLE`) modifiers can be selected. Use
    `min_selected_modifiers` and `max_selected_modifiers` instead.
    See [CatalogModifierListSelectionType](#type-catalogmodifierlistselectiontype) for possible values
    """

    modifiers: typing_extensions.NotRequired[typing.Optional[typing.Sequence["CatalogObjectParams"]]]
    """
    A non-empty list of `CatalogModifier` objects to be included in the `CatalogModifierList`, 
    for non text-based modifiers when the `modifier_type` attribute is `LIST`. Each element of this list 
    is a `CatalogObject` instance of the `MODIFIER` type, containing the following attributes:
    ```
    {
    "id": "{{catalog_modifier_id}}",
    "type": "MODIFIER", 
    "modifier_data": {{a CatalogModifier instance>}} 
    }
    ```
    """

    image_ids: typing_extensions.NotRequired[typing.Optional[typing.Sequence[str]]]
    """
    The IDs of images associated with this `CatalogModifierList` instance.
    Currently these images are not displayed on Square products, but may be displayed in 3rd-party applications.
    """

    allow_quantities: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    When `true`, allows multiple quantities of the same modifier to be selected.
    """

    is_conversational: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    True if modifiers belonging to this list can be used conversationally.
    """

    modifier_type: typing_extensions.NotRequired[CatalogModifierListModifierType]
    """
    The type of the modifier. 
    
    When this `modifier_type` value is `TEXT`,  the `CatalogModifierList` represents a text-based modifier. 
    When this `modifier_type` value is `LIST`, the `CatalogModifierList` contains a list of `CatalogModifier` objects.
    See [CatalogModifierListModifierType](#type-catalogmodifierlistmodifiertype) for possible values
    """

    max_length: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum length, in Unicode points, of the text string of the text-based modifier as represented by 
    this `CatalogModifierList` object with the `modifier_type` set to `TEXT`.
    """

    text_required: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Whether the text string must be a non-empty string (`true`) or not (`false`) for a text-based modifier
    as represented by this `CatalogModifierList` object with the `modifier_type` set to `TEXT`.
    """

    internal_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A note for internal use by the business.   
    
    For example, for a text-based modifier applied to a T-shirt item, if the buyer-supplied text of "Hello, Kitty!"  
    is to be printed on the T-shirt, this `internal_name` attribute can be "Use italic face" as 
    an instruction for the business to follow.  
    
    For non text-based modifiers, this `internal_name` attribute can be 
    used to include SKUs, internal codes, or supplemental descriptions for internal use.
    """

    min_selected_modifiers: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The minimum number of modifiers that must be selected from this list. The value can be overridden with `CatalogItemModifierListInfo`.
    
    Values:
    
    - 0: No selection is required.
    - -1: Default value, the attribute was not set by the client. Treated as no selection required.
    - &gt;0: The required minimum modifier selections. This can be larger than the total `CatalogModifiers` when `allow_quantities` is enabled.
    - &lt; -1: Invalid. Treated as no selection required.
    """

    max_selected_modifiers: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of modifiers that must be selected from this list. The value can be overridden with `CatalogItemModifierListInfo`.
    
    Values:
    
    - 0: No maximum limit.
    - -1: Default value, the attribute was not set by the client. Treated as no maximum limit.
    - &gt;0: The maximum total modifier selections. This can be larger than the total `CatalogModifiers` when `allow_quantities` is enabled.
    - &lt; -1: Invalid. Treated as no maximum limit.
    """

    hidden_from_customer: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    If `true`, modifiers from this list are hidden from customer receipts. The default value is `false`.
    This setting can be overridden with `CatalogItemModifierListInfo.hidden_from_customer_override`.
    """
