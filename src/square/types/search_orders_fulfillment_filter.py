# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .fulfillment_type import FulfillmentType
import pydantic
from .fulfillment_state import FulfillmentState
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class SearchOrdersFulfillmentFilter(UncheckedBaseModel):
    """
    Filter based on [order fulfillment](entity:Fulfillment) information.
    """

    fulfillment_types: typing.Optional[typing.List[FulfillmentType]] = pydantic.Field(default=None)
    """
    A list of [fulfillment types](entity:FulfillmentType) to filter
    for. The list returns orders if any of its fulfillments match any of the fulfillment types
    listed in this field.
    See [FulfillmentType](#type-fulfillmenttype) for possible values
    """

    fulfillment_states: typing.Optional[typing.List[FulfillmentState]] = pydantic.Field(default=None)
    """
    A list of [fulfillment states](entity:FulfillmentState) to filter
    for. The list returns orders if any of its fulfillments match any of the
    fulfillment states listed in this field.
    See [FulfillmentState](#type-fulfillmentstate) for possible values
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
