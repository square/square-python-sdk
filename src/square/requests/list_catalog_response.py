# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .catalog_object import CatalogObjectParams


class ListCatalogResponseParams(typing_extensions.TypedDict):
    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    cursor: typing_extensions.NotRequired[str]
    """
    The pagination cursor to be used in a subsequent request. If unset, this is the final response.
    See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.
    """

    objects: typing_extensions.NotRequired[typing.Sequence[CatalogObjectParams]]
    """
    The CatalogObjects returned.
    """
