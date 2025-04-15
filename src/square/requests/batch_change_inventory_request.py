# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .inventory_change import InventoryChangeParams


class BatchChangeInventoryRequestParams(typing_extensions.TypedDict):
    idempotency_key: str
    """
    A client-supplied, universally unique identifier (UUID) for the
    request.
    
    See [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency) in the
    [API Development 101](https://developer.squareup.com/docs/buildbasics) section for more
    information.
    """

    changes: typing_extensions.NotRequired[typing.Optional[typing.Sequence[InventoryChangeParams]]]
    """
    The set of physical counts and inventory adjustments to be made.
    Changes are applied based on the client-supplied timestamp and may be sent
    out of order.
    """

    ignore_unchanged_counts: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Indicates whether the current physical count should be ignored if
    the quantity is unchanged since the last physical count. Default: `true`.
    """
