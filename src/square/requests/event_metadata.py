# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class EventMetadataParams(typing_extensions.TypedDict):
    """
    Contains metadata about a particular [Event](entity:Event).
    """

    event_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID for the event.
    """

    api_version: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The API version of the event. This corresponds to the default API version of the developer application at the time when the event was created.
    """
