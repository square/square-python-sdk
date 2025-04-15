# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .business_booking_profile_customer_timezone_choice import BusinessBookingProfileCustomerTimezoneChoice
from .business_booking_profile_booking_policy import BusinessBookingProfileBookingPolicy
from .business_appointment_settings import BusinessAppointmentSettings
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BusinessBookingProfile(UncheckedBaseModel):
    """
    A seller's business booking profile, including booking policy, appointment settings, etc.
    """

    seller_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the seller, obtainable using the Merchants API.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The RFC 3339 timestamp specifying the booking's creation time.
    """

    booking_enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the seller is open for booking.
    """

    customer_timezone_choice: typing.Optional[BusinessBookingProfileCustomerTimezoneChoice] = pydantic.Field(
        default=None
    )
    """
    The choice of customer's time zone information of a booking.
    The Square online booking site and all notifications to customers uses either the seller location’s time zone
    or the time zone the customer chooses at booking.
    See [BusinessBookingProfileCustomerTimezoneChoice](#type-businessbookingprofilecustomertimezonechoice) for possible values
    """

    booking_policy: typing.Optional[BusinessBookingProfileBookingPolicy] = pydantic.Field(default=None)
    """
    The policy for the seller to automatically accept booking requests (`ACCEPT_ALL`) or not (`REQUIRES_ACCEPTANCE`).
    See [BusinessBookingProfileBookingPolicy](#type-businessbookingprofilebookingpolicy) for possible values
    """

    allow_user_cancel: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether customers can cancel or reschedule their own bookings (`true`) or not (`false`).
    """

    business_appointment_settings: typing.Optional[BusinessAppointmentSettings] = pydantic.Field(default=None)
    """
    Settings for appointment-type bookings.
    """

    support_seller_level_writes: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the seller's subscription to Square Appointments supports creating, updating or canceling an appointment through the API (`true`) or not (`false`) using seller permission.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
