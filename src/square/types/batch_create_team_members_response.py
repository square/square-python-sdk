# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .create_team_member_response import CreateTeamMemberResponse
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BatchCreateTeamMembersResponse(UncheckedBaseModel):
    """
    Represents a response from a bulk create request containing the created `TeamMember` objects or error messages.
    """

    team_members: typing.Optional[typing.Dict[str, CreateTeamMemberResponse]] = pydantic.Field(default=None)
    """
    The successfully created `TeamMember` objects. Each key is the `idempotency_key` that maps to the `CreateTeamMemberRequest`.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    The errors that occurred during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
