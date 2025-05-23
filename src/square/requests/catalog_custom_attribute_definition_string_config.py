# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class CatalogCustomAttributeDefinitionStringConfigParams(typing_extensions.TypedDict):
    """
    Configuration associated with Custom Attribute Definitions of type `STRING`.
    """

    enforce_uniqueness: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    If true, each Custom Attribute instance associated with this Custom Attribute
    Definition must have a unique value within the seller's catalog. For
    example, this may be used for a value like a SKU that should not be
    duplicated within a seller's catalog. May not be modified after the
    definition has been created.
    """
