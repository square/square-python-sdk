# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .bank_account import BankAccountParams


class GetBankAccountByV1IdResponseParams(typing_extensions.TypedDict):
    """
    Response object returned by GetBankAccountByV1Id.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information on errors encountered during the request.
    """

    bank_account: typing_extensions.NotRequired[BankAccountParams]
    """
    The requested `BankAccount` object.
    """
