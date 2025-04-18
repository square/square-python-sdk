# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .employee import Employee
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ListEmployeesResponse(UncheckedBaseModel):
    employees: typing.Optional[typing.List[Employee]] = None
    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    The token to be used to retrieve the next page of results.
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
