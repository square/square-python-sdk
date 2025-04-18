# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Phase(UncheckedBaseModel):
    """
    Represents a phase, which can override subscription phases as defined by plan_id
    """

    uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    id of subscription phase
    """

    ordinal: typing.Optional[int] = pydantic.Field(default=None)
    """
    index of phase in total subscription plan
    """

    order_template_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    id of order to be used in billing
    """

    plan_phase_uid: typing.Optional[str] = pydantic.Field(default=None)
    """
    the uid from the plan's phase in catalog
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
