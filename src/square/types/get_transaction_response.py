# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .transaction import Transaction
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetTransactionResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [RetrieveTransaction](api-endpoint:Transactions-RetrieveTransaction) endpoint.

    One of `errors` or `transaction` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    transaction: typing.Optional[Transaction] = pydantic.Field(default=None)
    """
    The requested transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
