# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .order import OrderParams
import typing
from .error import ErrorParams


class CloneOrderResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body of
    a request to the [CloneOrder](api-endpoint:Orders-CloneOrder) endpoint.
    """

    order: typing_extensions.NotRequired[OrderParams]
    """
    The cloned order.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
