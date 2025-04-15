# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing


class CatalogQueryItemsForModifierListParams(typing_extensions.TypedDict):
    """
    The query filter to return the items containing the specified modifier list IDs.
    """

    modifier_list_ids: typing.Sequence[str]
    """
    A set of `CatalogModifierList` IDs to be used to find associated `CatalogItem`s.
    """
