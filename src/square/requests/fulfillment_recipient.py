# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .address import AddressParams


class FulfillmentRecipientParams(typing_extensions.TypedDict):
    """
    Information about the fulfillment recipient.
    """

    customer_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the customer associated with the fulfillment.
    
    If `customer_id` is provided, the fulfillment recipient's `display_name`,
    `email_address`, and `phone_number` are automatically populated from the
    targeted customer profile. If these fields are set in the request, the request
    values override the information from the customer profile. If the
    targeted customer profile does not contain the necessary information and
    these fields are left unset, the request results in an error.
    """

    display_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The display name of the fulfillment recipient. This field is required.
    
    If provided, the display name overrides the corresponding customer profile value
    indicated by `customer_id`.
    """

    email_address: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The email address of the fulfillment recipient.
    
    If provided, the email address overrides the corresponding customer profile value
    indicated by `customer_id`.
    """

    phone_number: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The phone number of the fulfillment recipient. This field is required.
    
    If provided, the phone number overrides the corresponding customer profile value
    indicated by `customer_id`.
    """

    address: typing_extensions.NotRequired[AddressParams]
    """
    The address of the fulfillment recipient. This field is required.
    
    If provided, the address overrides the corresponding customer profile value
    indicated by `customer_id`.
    """
