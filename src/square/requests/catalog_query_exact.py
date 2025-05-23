# This file was auto-generated by Fern from our API Definition.

import typing_extensions


class CatalogQueryExactParams(typing_extensions.TypedDict):
    """
    The query filter to return the search result by exact match of the specified attribute name and value.
    """

    attribute_name: str
    """
    The name of the attribute to be searched. Matching of the attribute name is exact.
    """

    attribute_value: str
    """
    The desired value of the search attribute. Matching of the attribute value is case insensitive and can be partial.
    For example, if a specified value of "sma", objects with the named attribute value of "Small", "small" are both matched.
    """
