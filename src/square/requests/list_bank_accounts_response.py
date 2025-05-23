# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .bank_account import BankAccountParams


class ListBankAccountsResponseParams(typing_extensions.TypedDict):
    """
    Response object returned by ListBankAccounts.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Information on errors encountered during the request.
    """

    bank_accounts: typing_extensions.NotRequired[typing.Sequence[BankAccountParams]]
    """
    List of BankAccounts associated with this account.
    """

    cursor: typing_extensions.NotRequired[str]
    """
    When a response is truncated, it includes a cursor that you can 
    use in a subsequent request to fetch next set of bank accounts.
    If empty, this is the final response.
    
    For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    """
