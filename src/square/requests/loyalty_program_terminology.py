# This file was auto-generated by Fern from our API Definition.

import typing_extensions


class LoyaltyProgramTerminologyParams(typing_extensions.TypedDict):
    """
    Represents the naming used for loyalty points.
    """

    one: str
    """
    A singular unit for a point (for example, 1 point is called 1 star).
    """

    other: str
    """
    A plural unit for point (for example, 10 points is called 10 stars).
    """
