# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .dispute_evidence import DisputeEvidence
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class GetDisputeEvidenceResponse(UncheckedBaseModel):
    """
    Defines the fields in a `RetrieveDisputeEvidence` response.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    evidence: typing.Optional[DisputeEvidence] = pydantic.Field(default=None)
    """
    Metadata about the dispute evidence file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
