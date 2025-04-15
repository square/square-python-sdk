# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .inventory_state import InventoryState
from .source_application import SourceApplication
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class InventoryTransfer(UncheckedBaseModel):
    """
    Represents the transfer of a quantity of product inventory at a
    particular time from one location to another.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID generated by Square for the
    `InventoryTransfer`.
    """

    reference_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional ID provided by the application to tie the
    `InventoryTransfer` to an external system.
    """

    state: typing.Optional[InventoryState] = pydantic.Field(default=None)
    """
    The [inventory state](entity:InventoryState) for the quantity of
    items being transferred.
    See [InventoryState](#type-inventorystate) for possible values
    """

    from_location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the [Location](entity:Location) where the related
    quantity of items was tracked before the transfer.
    """

    to_location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the [Location](entity:Location) where the related
    quantity of items was tracked after the transfer.
    """

    catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the
    [CatalogObject](entity:CatalogObject) being tracked.
    """

    catalog_object_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The [type](entity:CatalogObjectType) of the [CatalogObject](entity:CatalogObject) being tracked. 
    
    The Inventory API supports setting and reading the `"catalog_object_type": "ITEM_VARIATION"` field value. 
    In addition, it can also read the `"catalog_object_type": "ITEM"` field value that is set by the Square Restaurants app.
    """

    quantity: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of items affected by the transfer as a decimal string.
    Can support up to 5 digits after the decimal point.
    """

    occurred_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    A client-generated RFC 3339-formatted timestamp that indicates when
    the transfer took place. For write actions, the `occurred_at` timestamp
    cannot be older than 24 hours or in the future relative to the time of the
    request.
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    An RFC 3339-formatted timestamp that indicates when Square
    received the transfer request.
    """

    source: typing.Optional[SourceApplication] = pydantic.Field(default=None)
    """
    Information about the application that initiated the
    inventory transfer.
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the [Employee](entity:Employee) responsible for the
    inventory transfer.
    """

    team_member_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Square-generated ID of the [Team Member](entity:TeamMember) responsible for the
    inventory transfer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
