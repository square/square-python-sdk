# This file was auto-generated by Fern from our API Definition.

from .catalog_object_base import CatalogObjectBaseParams
import typing_extensions
from .catalog_discount import CatalogDiscountParams


class CatalogObjectDiscountParams(CatalogObjectBaseParams):
    discount_data: typing_extensions.NotRequired[CatalogDiscountParams]
    """
    Structured data for a `CatalogDiscount`, set for CatalogObjects of type `DISCOUNT`.
    """
