# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .error import Error
import pydantic
from .card import Card
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateCardResponse(UncheckedBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the [CreateCard](api-endpoint:Cards-CreateCard) endpoint.

    Note: if there are errors processing the request, the card field will not be
    present.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Errors resulting from the request.
    """

    card: typing.Optional[Card] = pydantic.Field(default=None)
    """
    The card created by the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
