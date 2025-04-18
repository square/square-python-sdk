# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateMobileAuthorizationCodeResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the `CreateMobileAuthorizationCode` endpoint.
    """

    authorization_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    The generated authorization code that connects a mobile application instance
    to a Square account.
    """

    expires_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when `authorization_code` expires, in
    [RFC 3339](https://tools.ietf.org/html/rfc3339) format (for example, "2016-09-04T23:59:33.123Z").
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
