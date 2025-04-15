# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class CatalogQueryItemVariationsForItemOptionValuesParams(typing_extensions.TypedDict):
    """
    The query filter to return the item variations containing the specified item option value IDs.
    """

    item_option_value_ids: typing_extensions.NotRequired[typing.Optional[typing.Sequence[str]]]
    """
    A set of `CatalogItemOptionValue` IDs to be used to find associated
    `CatalogItemVariation`s. All ItemVariations that contain all of the given
    Item Option Values (in any order) will be returned.
    """
