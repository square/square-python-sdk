# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams


class RetrieveTokenStatusResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields that are included in the response body of
    a request to the `RetrieveTokenStatus` endpoint.
    """

    scopes: typing_extensions.NotRequired[typing.Sequence[str]]
    """
    The list of scopes associated with an access token.
    """

    expires_at: typing_extensions.NotRequired[str]
    """
    The date and time when the `access_token` expires, in RFC 3339 format. Empty if the token never expires.
    """

    client_id: typing_extensions.NotRequired[str]
    """
    The Square-issued application ID associated with the access token. This is the same application ID used to obtain the token.
    """

    merchant_id: typing_extensions.NotRequired[str]
    """
    The ID of the authorizing merchant's business.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
     Any errors that occurred during the request.
    """
