# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from ..types.custom_attribute_definition_visibility import CustomAttributeDefinitionVisibility
from .custom_attribute_definition import CustomAttributeDefinitionParams


class CustomAttributeParams(typing_extensions.TypedDict):
    """
    A custom attribute value. Each custom attribute value has a corresponding
    `CustomAttributeDefinition` object.
    """

    key: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The identifier
    of the custom attribute definition and its corresponding custom attributes. This value
    can be a simple key, which is the key that is provided when the custom attribute definition
    is created, or a qualified key, if the requesting
    application is not the definition owner. The qualified key consists of the application ID
    of the custom attribute definition owner
    followed by the simple key that was provided when the definition was created. It has the
    format application_id:simple key.
    
    The value for a simple key can contain up to 60 alphanumeric characters, periods (.),
    underscores (_), and hyphens (-).
    """

    value: typing_extensions.NotRequired[typing.Optional[typing.Any]]
    version: typing_extensions.NotRequired[int]
    """
    Read only. The current version of the custom attribute. This field is incremented when the custom attribute is changed.
    When updating an existing custom attribute value, you can provide this field
    and specify the current version of the custom attribute to enable
    [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency).
    This field can also be used to enforce strong consistency for reads. For more information about strong consistency for reads,
    see [Custom Attributes Overview](https://developer.squareup.com/docs/devtools/customattributes/overview).
    """

    visibility: typing_extensions.NotRequired[CustomAttributeDefinitionVisibility]
    """
    A copy of the `visibility` field value for the associated custom attribute definition.
    See [CustomAttributeDefinitionVisibility](#type-customattributedefinitionvisibility) for possible values
    """

    definition: typing_extensions.NotRequired[CustomAttributeDefinitionParams]
    """
    A copy of the associated custom attribute definition object. This field is only set when
    the optional field is specified on the request.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The timestamp that indicates when the custom attribute was created or was most recently
    updated, in RFC 3339 format.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp that indicates when the custom attribute was created, in RFC 3339 format.
    """
