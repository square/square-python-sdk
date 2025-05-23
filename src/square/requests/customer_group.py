# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions


class CustomerGroupParams(typing_extensions.TypedDict):
    """
    Represents a group of customer profiles.

    Customer groups can be created, be modified, and have their membership defined using
    the Customers API or within the Customer Directory in the Square Seller Dashboard or Point of Sale.
    """

    id: typing_extensions.NotRequired[str]
    """
    A unique Square-generated ID for the customer group.
    """

    name: str
    """
    The name of the customer group.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the customer group was created, in RFC 3339 format.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the customer group was last updated, in RFC 3339 format.
    """
