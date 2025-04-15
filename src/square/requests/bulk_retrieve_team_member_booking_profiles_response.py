# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .get_team_member_booking_profile_response import GetTeamMemberBookingProfileResponseParams
from .error import ErrorParams


class BulkRetrieveTeamMemberBookingProfilesResponseParams(typing_extensions.TypedDict):
    """
    Response payload for the [BulkRetrieveTeamMemberBookingProfiles](api-endpoint:Bookings-BulkRetrieveTeamMemberBookingProfiles) endpoint.
    """

    team_member_booking_profiles: typing_extensions.NotRequired[
        typing.Dict[str, GetTeamMemberBookingProfileResponseParams]
    ]
    """
    The returned team members' booking profiles, as a map with `team_member_id` as the key and [TeamMemberBookingProfile](entity:TeamMemberBookingProfile) the value.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Errors that occurred during the request.
    """
