# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class PhaseParams(typing_extensions.TypedDict):
    """
    Represents a phase, which can override subscription phases as defined by plan_id
    """

    uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    id of subscription phase
    """

    ordinal: typing_extensions.NotRequired[typing.Optional[int]]
    """
    index of phase in total subscription plan
    """

    order_template_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    id of order to be used in billing
    """

    plan_phase_uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    the uid from the plan's phase in catalog
    """
