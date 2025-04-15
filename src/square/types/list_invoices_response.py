# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .invoice import Invoice
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListInvoicesResponse(UncheckedBaseModel):
    """
    Describes a `ListInvoice` response.
    """

    invoices: typing.Optional[typing.List[Invoice]] = pydantic.Field(default=None)
    """
    The invoices retrieved.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    When a response is truncated, it includes a cursor that you can use in a 
    subsequent request to retrieve the next set of invoices. If empty, this is the final 
    response. 
    For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).
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
