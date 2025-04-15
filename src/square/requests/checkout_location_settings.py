# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .checkout_location_settings_policy import CheckoutLocationSettingsPolicyParams
from .checkout_location_settings_branding import CheckoutLocationSettingsBrandingParams
from .checkout_location_settings_tipping import CheckoutLocationSettingsTippingParams
from .checkout_location_settings_coupons import CheckoutLocationSettingsCouponsParams


class CheckoutLocationSettingsParams(typing_extensions.TypedDict):
    location_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the location that these settings apply to.
    """

    customer_notes_enabled: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Indicates whether customers are allowed to leave notes at checkout.
    """

    policies: typing_extensions.NotRequired[typing.Optional[typing.Sequence[CheckoutLocationSettingsPolicyParams]]]
    """
    Policy information is displayed at the bottom of the checkout pages.
    You can set a maximum of two policies.
    """

    branding: typing_extensions.NotRequired[CheckoutLocationSettingsBrandingParams]
    """
    The branding settings for this location.
    """

    tipping: typing_extensions.NotRequired[CheckoutLocationSettingsTippingParams]
    """
    The tip settings for this location.
    """

    coupons: typing_extensions.NotRequired[CheckoutLocationSettingsCouponsParams]
    """
    The coupon settings for this location.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the settings were last updated, in RFC 3339 format.
    Examples for January 25th, 2020 6:25:34pm Pacific Standard Time:
    UTC: 2020-01-26T02:25:34Z
    Pacific Standard Time with UTC offset: 2020-01-25T18:25:34-08:00
    """
