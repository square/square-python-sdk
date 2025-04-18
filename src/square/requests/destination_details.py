# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .destination_details_card_refund_details import DestinationDetailsCardRefundDetailsParams
from .destination_details_cash_refund_details import DestinationDetailsCashRefundDetailsParams
from .destination_details_external_refund_details import DestinationDetailsExternalRefundDetailsParams


class DestinationDetailsParams(typing_extensions.TypedDict):
    """
    Details about a refund's destination.
    """

    card_details: typing_extensions.NotRequired[DestinationDetailsCardRefundDetailsParams]
    """
    Details about a card refund. Only populated if the destination_type is `CARD`.
    """

    cash_details: typing_extensions.NotRequired[DestinationDetailsCashRefundDetailsParams]
    """
    Details about a cash refund. Only populated if the destination_type is `CASH`.
    """

    external_details: typing_extensions.NotRequired[DestinationDetailsExternalRefundDetailsParams]
    """
    Details about an external refund. Only populated if the destination_type is `EXTERNAL`.
    """
