# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .customer_group import CustomerGroup
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetCustomerGroupResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [RetrieveCustomerGroup](api-endpoint:CustomerGroups-RetrieveCustomerGroup) endpoint.

    Either `errors` or `group` is present in a given response (never both).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    group: typing.Optional[CustomerGroup] = pydantic.Field(default=None)
    """
    The retrieved customer group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
