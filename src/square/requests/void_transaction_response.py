# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams


class VoidTransactionResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body of
    a request to the [VoidTransaction](api-endpoint:Transactions-VoidTransaction) endpoint.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """
