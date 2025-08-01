# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .customer_created_event_data import CustomerCreatedEventDataParams


class CustomerCreatedEventParams(typing_extensions.TypedDict):
    """
    Published when a [customer](entity:Customer) is created. Subscribe to this event to track customer profiles affected by a merge operation.
    For more information, see [Use Customer Webhooks](https://developer.squareup.com/docs/customers-api/use-the-api/customer-webhooks).

    The `customer` object in the event notification does not include the `segment_ids` field.
    """

    merchant_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the seller associated with the event.
    """

    type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The type of event. For this object, the value is `customer.created`.
    """

    event_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The unique ID of the event, which is used for [idempotency support](https://developer.squareup.com/docs/webhooks/step4manage#webhooks-best-practices).
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The timestamp of when the event was created, in RFC 3339 format.
    """

    data: typing_extensions.NotRequired[CustomerCreatedEventDataParams]
    """
    The data associated with the event.
    """
