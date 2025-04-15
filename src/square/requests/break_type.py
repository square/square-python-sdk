# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions


class BreakTypeParams(typing_extensions.TypedDict):
    """
    A defined break template that sets an expectation for possible `Break`
    instances on a `Shift`.
    """

    id: typing_extensions.NotRequired[str]
    """
    The UUID for this object.
    """

    location_id: str
    """
    The ID of the business location this type of break applies to.
    """

    break_name: str
    """
    A human-readable name for this type of break. The name is displayed to
    employees in Square products.
    """

    expected_duration: str
    """
    Format: RFC-3339 P[n]Y[n]M[n]DT[n]H[n]M[n]S. The expected length of
    this break. Precision less than minutes is truncated.
    
    Example for break expected duration of 15 minutes: T15M
    """

    is_paid: bool
    """
    Whether this break counts towards time worked for compensation
    purposes.
    """

    version: typing_extensions.NotRequired[int]
    """
    Used for resolving concurrency issues. The request fails if the version
    provided does not match the server version at the time of the request. If a value is not
    provided, Square's servers execute a "blind" write; potentially
    overwriting another writer's data.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    A read-only timestamp in RFC 3339 format.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    A read-only timestamp in RFC 3339 format.
    """
