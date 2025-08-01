# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .team_member_updated_event_data import TeamMemberUpdatedEventDataParams


class TeamMemberUpdatedEventParams(typing_extensions.TypedDict):
    """
    Published when a Team Member is updated.
    """

    merchant_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The ID of the target merchant associated with the event.
    """

    type: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The type of event this represents, `"team_member.updated"`.
    """

    event_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID for the event.
    """

    created_at: typing_extensions.NotRequired[str]
    """
    Timestamp of when the event was created, in RFC 3339 format.
    """

    data: typing_extensions.NotRequired[TeamMemberUpdatedEventDataParams]
    """
    Data associated with the event.
    """
