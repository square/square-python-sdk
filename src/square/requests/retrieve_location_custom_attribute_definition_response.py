# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .custom_attribute_definition import CustomAttributeDefinitionParams
import typing
from .error import ErrorParams


class RetrieveLocationCustomAttributeDefinitionResponseParams(typing_extensions.TypedDict):
    """
    Represents a [RetrieveLocationCustomAttributeDefinition](api-endpoint:LocationCustomAttributes-RetrieveLocationCustomAttributeDefinition) response.
    Either `custom_attribute_definition` or `errors` is present in the response.
    """

    custom_attribute_definition: typing_extensions.NotRequired[CustomAttributeDefinitionParams]
    """
    The retrieved custom attribute definition.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
