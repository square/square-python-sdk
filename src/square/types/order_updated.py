# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .order_state import OrderState
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrderUpdated(UncheckedBaseModel):
    order_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The order's unique ID.
    """

    version: typing.Optional[int] = pydantic.Field(default=None)
    """
    The version number, which is incremented each time an update is committed to the order.
    Orders that were not created through the API do not include a version number and
    therefore cannot be updated.
    
    [Read more about working with versions.](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders)
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the seller location that this order is associated with.
    """

    state: typing.Optional[OrderState] = pydantic.Field(default=None)
    """
    The state of the order.
    See [OrderState](#type-orderstate) for possible values
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for when the order was created, in RFC 3339 format.
    """

    updated_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp for when the order was last updated, in RFC 3339 format.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
