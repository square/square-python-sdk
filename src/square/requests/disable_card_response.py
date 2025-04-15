# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .card import CardParams


class DisableCardResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body of
    a request to the [DisableCard](api-endpoint:Cards-DisableCard) endpoint.

    Note: if there are errors processing the request, the card field will not be
    present.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information on errors encountered during the request.
    """

    card: typing_extensions.NotRequired[CardParams]
    """
    The retrieved card.
    """
