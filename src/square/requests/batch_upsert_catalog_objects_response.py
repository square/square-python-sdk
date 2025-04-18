# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .catalog_object import CatalogObjectParams
from .catalog_id_mapping import CatalogIdMappingParams


class BatchUpsertCatalogObjectsResponseParams(typing_extensions.TypedDict):
    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    objects: typing_extensions.NotRequired[typing.Sequence[CatalogObjectParams]]
    """
    The created successfully created CatalogObjects.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The database [timestamp](https://developer.squareup.com/docs/build-basics/working-with-dates) of this update in RFC 3339 format, e.g., "2016-09-04T23:59:33.123Z".
    """

    id_mappings: typing_extensions.NotRequired[typing.Sequence[CatalogIdMappingParams]]
    """
    The mapping between client and server IDs for this upsert.
    """
