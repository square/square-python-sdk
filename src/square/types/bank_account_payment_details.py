# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .ach_details import AchDetails
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BankAccountPaymentDetails(UncheckedBaseModel):
    """
    Additional details about BANK_ACCOUNT type payments.
    """

    bank_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the bank associated with the bank account.
    """

    transfer_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the bank transfer. The type can be `ACH` or `UNKNOWN`.
    """

    account_ownership_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ownership type of the bank account performing the transfer.
    The type can be `INDIVIDUAL`, `COMPANY`, or `ACCOUNT_TYPE_UNKNOWN`.
    """

    fingerprint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Uniquely identifies the bank account for this seller and can be used
    to determine if payments are from the same bank account.
    """

    country: typing.Optional[str] = pydantic.Field(default=None)
    """
    The two-letter ISO code representing the country the bank account is located in.
    """

    statement_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The statement description as sent to the bank.
    """

    ach_details: typing.Optional[AchDetails] = pydantic.Field(default=None)
    """
    ACH-specific information about the transfer. The information is only populated
    if the `transfer_type` is `ACH`.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
