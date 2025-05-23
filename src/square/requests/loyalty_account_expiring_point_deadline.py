# This file was auto-generated by Fern from our API Definition.

import typing_extensions


class LoyaltyAccountExpiringPointDeadlineParams(typing_extensions.TypedDict):
    """
    Represents a set of points for a loyalty account that are scheduled to expire on a specific date.
    """

    points: int
    """
    The number of points scheduled to expire at the `expires_at` timestamp.
    """

    expires_at: str
    """
    The timestamp of when the points are scheduled to expire, in RFC 3339 format.
    """
