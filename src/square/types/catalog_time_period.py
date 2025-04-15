# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CatalogTimePeriod(UncheckedBaseModel):
    """
    Represents a time period - either a single period or a repeating period.
    """

    event: typing.Optional[str] = pydantic.Field(default=None)
    """
    An iCalendar (RFC 5545) [event](https://tools.ietf.org/html/rfc5545#section-3.6.1), which
    specifies the name, timing, duration and recurrence of this time period.
    
    Example:
    
    ```
    DTSTART:20190707T180000
    DURATION:P2H
    RRULE:FREQ=WEEKLY;BYDAY=MO,WE,FR
    ```
    
    Only `SUMMARY`, `DTSTART`, `DURATION` and `RRULE` fields are supported.
    `DTSTART` must be in local (unzoned) time format. Note that while `BEGIN:VEVENT`
    and `END:VEVENT` is not required in the request. The response will always
    include them.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
