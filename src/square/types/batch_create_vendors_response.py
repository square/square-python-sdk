# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .create_vendor_response import CreateVendorResponse
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BatchCreateVendorsResponse(UncheckedBaseModel):
    """
    Represents an output from a call to [BulkCreateVendors](api-endpoint:Vendors-BulkCreateVendors).
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    responses: typing.Optional[typing.Dict[str, CreateVendorResponse]] = pydantic.Field(default=None)
    """
    A set of [CreateVendorResponse](entity:CreateVendorResponse) objects encapsulating successfully created [Vendor](entity:Vendor)
    objects or error responses for failed attempts. The set is represented by 
    a collection of idempotency-key/`Vendor`-object or idempotency-key/error-object pairs. The idempotency keys correspond to those specified
    in the input.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
