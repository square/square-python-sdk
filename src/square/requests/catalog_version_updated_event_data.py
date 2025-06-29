# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .catalog_version_updated_event_object import CatalogVersionUpdatedEventObjectParams


class CatalogVersionUpdatedEventDataParams(typing_extensions.TypedDict):
    type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Name of the affected object’s type.
    """

    object: typing_extensions.NotRequired[CatalogVersionUpdatedEventObjectParams]
    """
    An object containing fields and values relevant to the event. Is absent if affected object was deleted.
    """
