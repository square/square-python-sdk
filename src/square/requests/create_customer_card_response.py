# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .card import CardParams


class CreateCustomerCardResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body of
    a request to the `CreateCustomerCard` endpoint.

    Either `errors` or `card` is present in a given response (never both).
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    card: typing_extensions.NotRequired[CardParams]
    """
    The created card on file.
    """
