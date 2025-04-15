# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .address import Address
from .customer_tax_ids import CustomerTaxIds
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BulkUpdateCustomerData(UncheckedBaseModel):
    """
    Defines the customer data provided in individual update requests for a
    [BulkUpdateCustomers](api-endpoint:Customers-BulkUpdateCustomers) operation.
    """

    given_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The given name (that is, the first name) associated with the customer profile.
    """

    family_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The family name (that is, the last name) associated with the customer profile.
    """

    company_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A business name associated with the customer profile.
    """

    nickname: typing.Optional[str] = pydantic.Field(default=None)
    """
    A nickname for the customer profile.
    """

    email_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    The email address associated with the customer profile.
    """

    address: typing.Optional[Address] = pydantic.Field(default=None)
    """
    The physical address associated with the customer profile. For maximum length constraints,
    see [Customer addresses](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#address).
    The `first_name` and `last_name` fields are ignored if they are present in the request.
    """

    phone_number: typing.Optional[str] = pydantic.Field(default=None)
    """
    The phone number associated with the customer profile. The phone number must be valid
    and can contain 9–16 digits, with an optional `+` prefix and country code. For more information,
    see [Customer phone numbers](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#phone-number).
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional second ID used to associate the customer profile with an
    entity in another system.
    """

    note: typing.Optional[str] = pydantic.Field(default=None)
    """
    An custom note associates with the customer profile.
    """

    birthday: typing.Optional[str] = pydantic.Field(default=None)
    """
    The birthday associated with the customer profile, in `YYYY-MM-DD` or `MM-DD` format.
    For example, specify `1998-09-21` for September 21, 1998, or `09-21` for September 21.
    Birthdays are returned in `YYYY-MM-DD` format, where `YYYY` is the specified birth year or
    `0000` if a birth year is not specified.
    """

    tax_ids: typing.Optional[CustomerTaxIds] = pydantic.Field(default=None)
    """
    The tax ID associated with the customer profile. This field is available only for
    customers of sellers in EU countries or the United Kingdom. For more information, see
    [Customer tax IDs](https://developer.squareup.com/docs/customers-api/what-it-does#customer-tax-ids).
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The current version of the customer profile.
    
    As a best practice, you should include this field to enable
    [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
    control.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
