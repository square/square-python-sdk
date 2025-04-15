# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
from .custom_attribute import CustomAttribute
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BulkUpsertMerchantCustomAttributesRequestMerchantCustomAttributeUpsertRequest(UncheckedBaseModel):
    """
    Represents an individual upsert request in a [BulkUpsertMerchantCustomAttributes](api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes)
    request. An individual request contains a merchant ID, the custom attribute to create or update,
    and an optional idempotency key.
    """

    merchant_id: str = pydantic.Field()
    """
    The ID of the target [merchant](entity:Merchant).
    """

    custom_attribute: CustomAttribute = pydantic.Field()
    """
    The custom attribute to create or update, with following fields:
    - `key`. This key must match the `key` of a custom attribute definition in the Square seller
    account. If the requesting application is not the definition owner, you must provide the qualified key.
    - `value`. This value must conform to the `schema` specified by the definition.
    For more information, see [Supported data types](https://developer.squareup.com/docs/devtools/customattributes/overview#supported-data-types).
    - The version field must match the current version of the custom attribute definition to enable
    [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)
    If this is not important for your application, version can be set to -1. For any other values, the request fails with a BAD_REQUEST error.
    """

    idempotency_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique identifier for this individual upsert request, used to ensure idempotency.
    For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
