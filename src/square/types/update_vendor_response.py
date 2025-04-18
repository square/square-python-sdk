# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .vendor import Vendor
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateVendorResponse(UncheckedBaseModel):
    """
    Represents an output from a call to [UpdateVendor](api-endpoint:Vendors-UpdateVendor).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors occurred when the request fails.
    """

    vendor: typing.Optional[Vendor] = pydantic.Field(default=None)
    """
    The [Vendor](entity:Vendor) that has been updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
