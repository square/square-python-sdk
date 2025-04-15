# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .loyalty_program import LoyaltyProgram
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetLoyaltyProgramResponse(UncheckedBaseModel):
    """
    A response that contains the loyalty program.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    program: typing.Optional[LoyaltyProgram] = pydantic.Field(default=None)
    """
    The loyalty program that was requested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
