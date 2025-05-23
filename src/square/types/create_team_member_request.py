# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .team_member import TeamMember
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateTeamMemberRequest(UncheckedBaseModel):
    """
    Represents a create request for a `TeamMember` object.
    """

    idempotency_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    A unique string that identifies this `CreateTeamMember` request.
    Keys can be any valid string, but must be unique for every request.
    For more information, see [Idempotency](https://developer.squareup.com/docs/build-basics/common-api-patterns/idempotency).
    
    The minimum length is 1 and the maximum length is 45.
    """

    team_member: typing.Optional[TeamMember] = pydantic.Field(default=None)
    """
    **Required** The data used to create the `TeamMember` object. If you include `wage_setting`, you must provide
    `job_id` for each job assignment. To get job IDs, call [ListJobs](api-endpoint:Team-ListJobs).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
