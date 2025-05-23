# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .update_customer_response import UpdateCustomerResponseParams
from .error import ErrorParams


class BulkUpdateCustomersResponseParams(typing_extensions.TypedDict):
    """
    Defines the fields included in the response body from the
    [BulkUpdateCustomers](api-endpoint:Customers-BulkUpdateCustomers) endpoint.
    """

    responses: typing_extensions.NotRequired[typing.Dict[str, UpdateCustomerResponseParams]]
    """
    A map of responses that correspond to individual update requests, represented by
    key-value pairs.
    
    Each key is the customer ID that was specified for an update request and each value
    is the corresponding response.
    If the request succeeds, the value is the updated customer profile.
    If the request fails, the value contains any errors that occurred during the request.
    """

    errors: typing_extensions.NotRequired[typing.Sequence[ErrorParams]]
    """
    Any top-level errors that prevented the bulk operation from running.
    """
