# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .transaction import Transaction
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListTransactionsResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [ListTransactions](api-endpoint:Transactions-ListTransactions) endpoint.

    One of `errors` or `transactions` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    transactions: typing.Optional[typing.List[Transaction]] = pydantic.Field(default=None)
    """
    An array of transactions that match your query.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    A pagination cursor for retrieving the next set of results,
    if any remain. Provide this value as the `cursor` parameter in a subsequent
    request to this endpoint.
    
    See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
