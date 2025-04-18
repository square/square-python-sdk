# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from ..types.action_cancel_reason import ActionCancelReason
from ..types.terminal_action_action_type import TerminalActionActionType
from .qr_code_options import QrCodeOptionsParams
from .save_card_options import SaveCardOptionsParams
from .signature_options import SignatureOptionsParams
from .confirmation_options import ConfirmationOptionsParams
from .receipt_options import ReceiptOptionsParams
from .data_collection_options import DataCollectionOptionsParams
from .select_options import SelectOptionsParams
from .device_metadata import DeviceMetadataParams


class TerminalActionParams(typing_extensions.TypedDict):
    """
    Represents an action processed by the Square Terminal.
    """

    id: typing_extensions.NotRequired[str]
    """
    A unique ID for this `TerminalAction`.
    """

    device_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The unique Id of the device intended for this `TerminalAction`.
    The Id can be retrieved from /v2/devices api.
    """

    deadline_duration: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The duration as an RFC 3339 duration, after which the action will be automatically canceled.
    TerminalActions that are `PENDING` will be automatically `CANCELED` and have a cancellation reason
    of `TIMED_OUT`
    
    Default: 5 minutes from creation
    
    Maximum: 5 minutes
    """

    status: typing_extensions.NotRequired[str]
    """
    The status of the `TerminalAction`.
    Options: `PENDING`, `IN_PROGRESS`, `CANCEL_REQUESTED`, `CANCELED`, `COMPLETED`
    """

    cancel_reason: typing_extensions.NotRequired[ActionCancelReason]
    """
    The reason why `TerminalAction` is canceled. Present if the status is `CANCELED`.
    See [ActionCancelReason](#type-actioncancelreason) for possible values
    """

    created_at: typing_extensions.NotRequired[str]
    """
    The time when the `TerminalAction` was created as an RFC 3339 timestamp.
    """

    updated_at: typing_extensions.NotRequired[str]
    """
    The time when the `TerminalAction` was last updated as an RFC 3339 timestamp.
    """

    app_id: typing_extensions.NotRequired[str]
    """
    The ID of the application that created the action.
    """

    location_id: typing_extensions.NotRequired[str]
    """
    The location id the action is attached to, if a link can be made.
    """

    type: typing_extensions.NotRequired[TerminalActionActionType]
    """
    Represents the type of the action.
    See [ActionType](#type-actiontype) for possible values
    """

    qr_code_options: typing_extensions.NotRequired[QrCodeOptionsParams]
    """
    Describes configuration for the QR code action. Requires `QR_CODE` type.
    """

    save_card_options: typing_extensions.NotRequired[SaveCardOptionsParams]
    """
    Describes configuration for the save-card action. Requires `SAVE_CARD` type.
    """

    signature_options: typing_extensions.NotRequired[SignatureOptionsParams]
    """
    Describes configuration for the signature capture action. Requires `SIGNATURE` type.
    """

    confirmation_options: typing_extensions.NotRequired[ConfirmationOptionsParams]
    """
    Describes configuration for the confirmation action. Requires `CONFIRMATION` type.
    """

    receipt_options: typing_extensions.NotRequired[ReceiptOptionsParams]
    """
    Describes configuration for the receipt action. Requires `RECEIPT` type.
    """

    data_collection_options: typing_extensions.NotRequired[DataCollectionOptionsParams]
    """
    Describes configuration for the data collection action. Requires `DATA_COLLECTION` type.
    """

    select_options: typing_extensions.NotRequired[SelectOptionsParams]
    """
    Describes configuration for the select action. Requires `SELECT` type.
    """

    device_metadata: typing_extensions.NotRequired[DeviceMetadataParams]
    """
    Details about the Terminal that received the action request (such as battery level,
    operating system version, and network connection settings).
    
    Only available for `PING` action type.
    """

    await_next_action: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Indicates the action will be linked to another action and requires a waiting dialog to be
    displayed instead of returning to the idle screen on completion of the action.
    
    Only supported on SIGNATURE, CONFIRMATION, DATA_COLLECTION, and SELECT types.
    """

    await_next_action_duration: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The timeout duration of the waiting dialog as an RFC 3339 duration, after which the
    waiting dialog will no longer be displayed and the Terminal will return to the idle screen.
    
    Default: 5 minutes from when the waiting dialog is displayed
    
    Maximum: 5 minutes
    """
