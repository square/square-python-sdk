# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .terminal_checkout import TerminalCheckout
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateTerminalCheckoutResponse(UncheckedBaseModel):
    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    checkout: typing.Optional[TerminalCheckout] = pydantic.Field(default=None)
    """
    The created `TerminalCheckout`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
