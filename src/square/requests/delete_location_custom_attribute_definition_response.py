# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams


class DeleteLocationCustomAttributeDefinitionResponseParams(typing_extensions.TypedDict):
    """
    Represents a response from a delete request containing error messages if there are any.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
