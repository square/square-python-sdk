# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .terminal_refund import TerminalRefund
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class DismissTerminalRefundResponse(UncheckedBaseModel):
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information on errors encountered during the request.
    """

    refund: typing.Optional[TerminalRefund] = pydantic.Field(default=None)
    """
    Current state of the refund to be dismissed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
