# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import typing
from .invoice_attachment import InvoiceAttachment
import pydantic
from .error import Error
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class CreateInvoiceAttachmentResponse(UncheckedBaseModel):
    """
    Represents a [CreateInvoiceAttachment](api-endpoint:Invoices-CreateInvoiceAttachment) response.
    """

    attachment: typing.Optional[InvoiceAttachment] = pydantic.Field(default=None)
    """
    Metadata about the attachment that was added to the invoice.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Information about errors encountered during the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
