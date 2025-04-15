# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .address import AddressParams
from .customer_preferences import CustomerPreferencesParams
from ..types.customer_creation_source import CustomerCreationSource
from .customer_tax_ids import CustomerTaxIdsParams


class CustomerParams(typing_extensions.TypedDict):
    """
    Represents a Square customer profile in the Customer Directory of a Square seller.
    """

    id: typing_extensions.NotRequired[str]
    """
    A unique Square-assigned ID for the customer profile.
    
    If you need this ID for an API request, use the ID returned when you created the customer profile or call the [SearchCustomers](api-endpoint:Customers-SearchCustomers) 
    or [ListCustomers](api-endpoint:Customers-ListCustomers) endpoint.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the customer profile was created, in RFC 3339 format.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The timestamp when the customer profile was last updated, in RFC 3339 format.
    """

    given_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The given name (that is, the first name) associated with the customer profile.
    """

    family_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The family name (that is, the last name) associated with the customer profile.
    """

    nickname: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A nickname for the customer profile.
    """

    company_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A business name associated with the customer profile.
    """

    email_address: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The email address associated with the customer profile.
    """

    address: typing_extensions.NotRequired[AddressParams]
    """
    The physical address associated with the customer profile.
    """

    phone_number: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The phone number associated with the customer profile.
    """

    birthday: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The birthday associated with the customer profile, in `YYYY-MM-DD` format. For example, `1998-09-21`
    represents September 21, 1998, and `0000-09-21` represents September 21 (without a birth year).
    """

    reference_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    An optional second ID used to associate the customer profile with an
    entity in another system.
    """

    note: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A custom note associated with the customer profile.
    """

    preferences: typing_extensions.NotRequired[CustomerPreferencesParams]
    """
    Represents general customer preferences.
    """

    creation_source: typing_extensions.NotRequired[CustomerCreationSource]
    """
    The method used to create the customer profile.
    See [CustomerCreationSource](#type-customercreationsource) for possible values
    """

    group_ids: typing_extensions.NotRequired[typing.Optional[typing.Sequence[str]]]
    """
    The IDs of [customer groups](entity:CustomerGroup) the customer belongs to.
    """

    segment_ids: typing_extensions.NotRequired[typing.Optional[typing.Sequence[str]]]
    """
    The IDs of [customer segments](entity:CustomerSegment) the customer belongs to.
    """

    version: typing_extensions.NotRequired[int]
    """
    The Square-assigned version number of the customer profile. The version number is incremented each time an update is committed to the customer profile, except for changes to customer segment membership.
    """

    tax_ids: typing_extensions.NotRequired[CustomerTaxIdsParams]
    """
    The tax ID associated with the customer profile. This field is present only for customers of sellers in EU countries or the United Kingdom. 
    For more information, see [Customer tax IDs](https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids).
    """
