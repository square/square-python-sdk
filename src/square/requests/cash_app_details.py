# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class CashAppDetailsParams(typing_extensions.TypedDict):
    """
    Additional details about `WALLET` type payments with the `brand` of `CASH_APP`.
    """

    buyer_full_name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the Cash App account holder.
    """

    buyer_country_code: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The country of the Cash App account holder, in ISO 3166-1-alpha-2 format.
    
    For possible values, see [Country](entity:Country).
    """

    buyer_cashtag: typing_extensions.NotRequired[str]
    """
    $Cashtag of the Cash App account holder.
    """
