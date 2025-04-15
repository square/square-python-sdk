# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
from .terminal_checkout_query_filter import TerminalCheckoutQueryFilterParams
from .terminal_checkout_query_sort import TerminalCheckoutQuerySortParams


class TerminalCheckoutQueryParams(typing_extensions.TypedDict):
    filter: typing_extensions.NotRequired[TerminalCheckoutQueryFilterParams]
    """
    Options for filtering returned `TerminalCheckout` objects.
    """

    sort: typing_extensions.NotRequired[TerminalCheckoutQuerySortParams]
    """
    Option for sorting returned `TerminalCheckout` objects.
    """
