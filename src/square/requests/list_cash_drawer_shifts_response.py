# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .error import ErrorParams
from .cash_drawer_shift_summary import CashDrawerShiftSummaryParams


class ListCashDrawerShiftsResponseParams(typing_extensions.TypedDict):
    cursor: typing_extensions.NotRequired[str]
    """
    Opaque cursor for fetching the next page of results. Cursor is not
    present in the last page of results.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any errors that occurred during the request.
    """

    cash_drawer_shifts: typing_extensions.NotRequired[typing.Sequence[CashDrawerShiftSummaryParams]]
    """
    A collection of CashDrawerShiftSummary objects for shifts that match
    the query.
    """
