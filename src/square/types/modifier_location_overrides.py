# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from .money import Money
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ModifierLocationOverrides(UncheckedBaseModel):
    """
    Location-specific overrides for specified properties of a `CatalogModifier` object.
    """

    location_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the `Location` object representing the location. This can include a deactivated location.
    """

    price_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The overridden price at the specified location. If this is unspecified, the modifier price is not overridden.
    The modifier becomes free of charge at the specified location, when this `price_money` field is set to 0.
    """

    sold_out: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the modifier is sold out at the specified location or not. As an example, for cheese (modifier) burger (item), when the modifier is sold out, it is the cheese, but not the burger, that is sold out.
    The seller can manually set this sold out status. Attempts by an application to set this attribute are ignored.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
