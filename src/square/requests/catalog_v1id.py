# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from ..core.serialization import FieldMetadata


class CatalogV1IdParams(typing_extensions.TypedDict):
    """
    A Square API V1 identifier of an item, including the object ID and its associated location ID.
    """

    catalog_v1id: typing_extensions.NotRequired[
        typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="catalog_v1_id")]
    ]
    """
    The ID for an object used in the Square API V1, if the object ID differs from the Square API V2 object ID.
    """

    location_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the `Location` this Connect V1 ID is associated with.
    """
