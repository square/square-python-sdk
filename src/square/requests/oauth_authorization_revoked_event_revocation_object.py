# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from ..types.oauth_authorization_revoked_event_revoker_type import OauthAuthorizationRevokedEventRevokerType


class OauthAuthorizationRevokedEventRevocationObjectParams(typing_extensions.TypedDict):
    revoked_at: typing_extensions.NotRequired[typing.Optional[str]]
    """
    Timestamp of when the revocation event occurred, in RFC 3339 format.
    """

    revoker_type: typing_extensions.NotRequired[OauthAuthorizationRevokedEventRevokerType]
    """
    Type of client that performed the revocation, either APPLICATION, MERCHANT, or SQUARE.
    See [OauthAuthorizationRevokedEventRevokerType](#type-oauthauthorizationrevokedeventrevokertype) for possible values
    """
