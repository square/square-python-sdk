# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .dispute_evidence import DisputeEvidenceParams


class CreateDisputeEvidenceFileResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields in a `CreateDisputeEvidenceFile` response.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    evidence: typing_extensions.NotRequired[DisputeEvidenceParams]
    """
    The metadata of the newly uploaded dispute evidence.
    """
