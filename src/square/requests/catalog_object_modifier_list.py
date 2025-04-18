# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from .catalog_object_base import CatalogObjectBaseParams
import typing_extensions
import typing

if typing.TYPE_CHECKING:
    from .catalog_modifier_list import CatalogModifierListParams


class CatalogObjectModifierListParams(CatalogObjectBaseParams):
    modifier_list_data: typing_extensions.NotRequired["CatalogModifierListParams"]
    """
    Structured data for a `CatalogModifierList`, set for CatalogObjects of type `MODIFIER_LIST`.
    """
