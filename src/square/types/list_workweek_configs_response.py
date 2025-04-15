# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .workweek_config import WorkweekConfig
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListWorkweekConfigsResponse(UncheckedBaseModel):
    """
    The response to a request for a set of `WorkweekConfig` objects. The response contains
    the requested `WorkweekConfig` objects and might contain a set of `Error` objects if
    the request resulted in errors.
    """

    workweek_configs: typing.Optional[typing.List[WorkweekConfig]] = pydantic.Field(default=None)
    """
    A page of `WorkweekConfig` results.
    """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value supplied in the subsequent request to fetch the next page of
    `WorkweekConfig` results.
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
