# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class OrderLineItemPricingBlocklistsBlockedTax(UncheckedBaseModel):
    """
    A tax to block from applying to a line item. The tax must be
    identified by either `tax_uid` or `tax_catalog_object_id`, but not both.
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique ID of the `BlockedTax` within the order.
    """

    tax_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `uid` of the tax that should be blocked. Use this field to block
    ad hoc taxes. For catalog, taxes use the `tax_catalog_object_id` field.
    """

    tax_catalog_object_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The `catalog_object_id` of the tax that should be blocked.
    Use this field to block catalog taxes. For ad hoc taxes, use the
    `tax_uid` field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
