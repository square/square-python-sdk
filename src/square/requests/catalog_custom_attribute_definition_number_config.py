# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class CatalogCustomAttributeDefinitionNumberConfigParams(typing_extensions.TypedDict):
    precision: typing_extensions.NotRequired[typing.Optional[int]]
    """
    An integer between 0 and 5 that represents the maximum number of
    positions allowed after the decimal in number custom attribute values
    For example:
    
    - if the precision is 0, the quantity can be 1, 2, 3, etc.
    - if the precision is 1, the quantity can be 0.1, 0.2, etc.
    - if the precision is 2, the quantity can be 0.01, 0.12, etc.
    
    Default: 5
    """
