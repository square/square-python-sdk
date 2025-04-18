# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from ..types.booking_status import BookingStatus
import typing
from .appointment_segment import AppointmentSegmentParams
from ..types.business_appointment_settings_booking_location_type import BusinessAppointmentSettingsBookingLocationType
from .booking_creator_details import BookingCreatorDetailsParams
from ..types.booking_booking_source import BookingBookingSource
from .address import AddressParams


class BookingParams(typing_extensions.TypedDict):
    """
    Represents a booking as a time-bound service contract for a seller's staff member to provide a specified service
    at a given location to a requesting customer in one or more appointment segments.
    """

    id: typing_extensions.NotRequired[str]
    """
    A unique ID of this object representing a booking.
    """

    version: typing_extensions.NotRequired[int]
    """
    The revision number for the booking used for optimistic concurrency.
    """

    status: typing_extensions.NotRequired[BookingStatus]
    """
    The status of the booking, describing where the booking stands with respect to the booking state machine.
    See [BookingStatus](#type-bookingstatus) for possible values
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The RFC 3339 timestamp specifying the creation time of this booking.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The RFC 3339 timestamp specifying the most recent update time of this booking.
    """

    start_at: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The RFC 3339 timestamp specifying the starting time of this booking.
    """

    location_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the [Location](entity:Location) object representing the location where the booked service is provided. Once set when the booking is created, its value cannot be changed.
    """

    customer_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the [Customer](entity:Customer) object representing the customer receiving the booked service.
    """

    customer_note: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The free-text field for the customer to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a relevant [CatalogObject](entity:CatalogObject) instance.
    """

    seller_note: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The free-text field for the seller to supply notes about the booking. For example, the note can be preferences that cannot be expressed by supported attributes of a specific [CatalogObject](entity:CatalogObject) instance.
    This field should not be visible to customers.
    """

    appointment_segments: typing_extensions.NotRequired[typing.Optional[typing.Sequence[AppointmentSegmentParams]]]
    """
    A list of appointment segments for this booking.
    """

    transition_time_minutes: typing_extensions.NotRequired[int]
    """
    Additional time at the end of a booking.
    Applications should not make this field visible to customers of a seller.
    """

    all_day: typing_extensions.NotRequired[bool]
    """
    Whether the booking is of a full business day.
    """

    location_type: typing_extensions.NotRequired[BusinessAppointmentSettingsBookingLocationType]
    """
    The type of location where the booking is held.
    See [BusinessAppointmentSettingsBookingLocationType](#type-businessappointmentsettingsbookinglocationtype) for possible values
    """

    creator_details: typing_extensions.NotRequired[BookingCreatorDetailsParams]
    """
    Information about the booking creator.
    """

    source: typing_extensions.NotRequired[BookingBookingSource]
    """
    The source of the booking.
    Access to this field requires seller-level permissions.
    See [BookingBookingSource](#type-bookingbookingsource) for possible values
    """

    address: typing_extensions.NotRequired[AddressParams]
    """
    Stores a customer address if the location type is `CUSTOMER_LOCATION`.
    """
