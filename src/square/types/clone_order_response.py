# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .order import Order
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CloneOrderResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [CloneOrder](api-endpoint:Orders-CloneOrder) endpoint.
    """

    order: typing.Optional[Order] = pydantic.Field(default=None)
    """
    The cloned order.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
