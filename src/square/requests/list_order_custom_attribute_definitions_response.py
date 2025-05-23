# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing
from .custom_attribute_definition import CustomAttributeDefinitionParams
import typing_extensions
from .error import ErrorParams


class ListOrderCustomAttributeDefinitionsResponseParams(typing_extensions.TypedDict):
    """
    Represents a response from listing order custom attribute definitions.
    """

    custom_attribute_definitions: typing.Sequence[CustomAttributeDefinitionParams]
    """
    The retrieved custom attribute definitions. If no custom attribute definitions are found, Square returns an empty object (`{}`).
    """

    cursor: typing_extensions.NotRequired[str]
    """
    The cursor to provide in your next call to this endpoint to retrieve the next page of results for your original request. 
    This field is present only if the request succeeded and additional results are available.
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
