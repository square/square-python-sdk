# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing
from .catalog_object import CatalogObjectParams


class CatalogObjectBatchParams(typing_extensions.TypedDict):
    """
    A batch of catalog objects.
    """

    objects: typing.Sequence[CatalogObjectParams]
    """
    A list of CatalogObjects belonging to this batch.
    """
