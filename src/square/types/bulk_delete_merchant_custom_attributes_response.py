# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .bulk_delete_merchant_custom_attributes_response_merchant_custom_attribute_delete_response import (
    BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponse,
)
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BulkDeleteMerchantCustomAttributesResponse(UncheckedBaseModel):
    """
    Represents a [BulkDeleteMerchantCustomAttributes](api-endpoint:MerchantCustomAttributes-BulkDeleteMerchantCustomAttributes) response,
    which contains a map of responses that each corresponds to an individual delete request.
    """

    values: typing.Dict[str, BulkDeleteMerchantCustomAttributesResponseMerchantCustomAttributeDeleteResponse] = (
        pydantic.Field()
    )
    """
    A map of responses that correspond to individual delete requests. Each response has the
    same key as the corresponding request.
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
