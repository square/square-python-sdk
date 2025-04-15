# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .application_type import ApplicationType
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DeviceComponentDetailsApplicationDetails(UncheckedBaseModel):
    application_type: typing.Optional[ApplicationType] = pydantic.Field(default=None)
    """
    The type of application.
    See [ApplicationType](#type-applicationtype) for possible values
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the application.
    """

    session_location: typing.Optional[str] = pydantic.Field(default=None)
    """
    The location_id of the session for the application.
    """

    device_code_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the device code that was used to log in to the device.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
