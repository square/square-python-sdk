# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DeviceMetadata(UncheckedBaseModel):
    battery_percentage: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Terminal’s remaining battery percentage, between 1-100.
    """

    charging_state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current charging state of the Terminal.
    Options: `CHARGING`, `NOT_CHARGING`
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the Square seller business location associated with the Terminal.
    """

    merchant_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the Square merchant account that is currently signed-in to the Terminal.
    """

    network_connection_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Terminal’s current network connection type.
    Options: `WIFI`, `ETHERNET`
    """

    payment_region: typing.Optional[str] = pydantic.Field(default=None)
    """
    The country in which the Terminal is authorized to take payments.
    """

    serial_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier assigned to the Terminal, which can be found on the lower back
    of the device.
    """

    os_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current version of the Terminal’s operating system.
    """

    app_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current version of the application running on the Terminal.
    """

    wifi_network_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the Wi-Fi network to which the Terminal is connected.
    """

    wifi_network_strength: typing.Optional[str] = pydantic.Field(default=None)
    """
    The signal strength of the Wi-FI network connection.
    Options: `POOR`, `FAIR`, `GOOD`, `EXCELLENT`
    """

    ip_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address of the Terminal.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
