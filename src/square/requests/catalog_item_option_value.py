# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class CatalogItemOptionValueParams(typing_extensions.TypedDict):
    """
    An enumerated value that can link a
    `CatalogItemVariation` to an item option as one of
    its item option values.
    """

    item_option_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Unique ID of the associated item option.
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Name of this item option value. This is a searchable attribute for use in applicable query filters.
    """

    description: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A human-readable description for the option value. This is a searchable attribute for use in applicable query filters.
    """

    color: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The HTML-supported hex color for the item option (e.g., "#ff8d4e85").
    Only displayed if `show_colors` is enabled on the parent `ItemOption`. When
    left unset, `color` defaults to white ("#ffffff") when `show_colors` is
    enabled on the parent `ItemOption`.
    """

    ordinal: typing_extensions.NotRequired[typing.Optional[int]]
    """
    Determines where this option value appears in a list of option values.
    """
