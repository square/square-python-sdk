# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .create_team_member_response import CreateTeamMemberResponseParams
from .error import ErrorParams


class BatchCreateTeamMembersResponseParams(typing_extensions.TypedDict):
    """
    Represents a response from a bulk create request containing the created `TeamMember` objects or error messages.
    """

    team_members: typing_extensions.NotRequired[typing.Dict[str, CreateTeamMemberResponseParams]]
    """
    The successfully created `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    The errors that occurred during the request.
    """
