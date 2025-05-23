# This file was auto-generated by Fern from our API Definition.

from ..core.unchecked_base_model import UncheckedBaseModel
import pydantic
import typing
from .activity_type import ActivityType
from .money import Money
from .payment_balance_activity_app_fee_revenue_detail import PaymentBalanceActivityAppFeeRevenueDetail
from .payment_balance_activity_app_fee_refund_detail import PaymentBalanceActivityAppFeeRefundDetail
from .payment_balance_activity_automatic_savings_detail import PaymentBalanceActivityAutomaticSavingsDetail
from .payment_balance_activity_automatic_savings_reversed_detail import (
    PaymentBalanceActivityAutomaticSavingsReversedDetail,
)
from .payment_balance_activity_charge_detail import PaymentBalanceActivityChargeDetail
from .payment_balance_activity_deposit_fee_detail import PaymentBalanceActivityDepositFeeDetail
from .payment_balance_activity_deposit_fee_reversed_detail import PaymentBalanceActivityDepositFeeReversedDetail
from .payment_balance_activity_dispute_detail import PaymentBalanceActivityDisputeDetail
from .payment_balance_activity_fee_detail import PaymentBalanceActivityFeeDetail
from .payment_balance_activity_free_processing_detail import PaymentBalanceActivityFreeProcessingDetail
from .payment_balance_activity_hold_adjustment_detail import PaymentBalanceActivityHoldAdjustmentDetail
from .payment_balance_activity_open_dispute_detail import PaymentBalanceActivityOpenDisputeDetail
from .payment_balance_activity_other_detail import PaymentBalanceActivityOtherDetail
from .payment_balance_activity_other_adjustment_detail import PaymentBalanceActivityOtherAdjustmentDetail
from .payment_balance_activity_refund_detail import PaymentBalanceActivityRefundDetail
from .payment_balance_activity_release_adjustment_detail import PaymentBalanceActivityReleaseAdjustmentDetail
from .payment_balance_activity_reserve_hold_detail import PaymentBalanceActivityReserveHoldDetail
from .payment_balance_activity_reserve_release_detail import PaymentBalanceActivityReserveReleaseDetail
from .payment_balance_activity_square_capital_payment_detail import PaymentBalanceActivitySquareCapitalPaymentDetail
from .payment_balance_activity_square_capital_reversed_payment_detail import (
    PaymentBalanceActivitySquareCapitalReversedPaymentDetail,
)
from .payment_balance_activity_tax_on_fee_detail import PaymentBalanceActivityTaxOnFeeDetail
from .payment_balance_activity_third_party_fee_detail import PaymentBalanceActivityThirdPartyFeeDetail
from .payment_balance_activity_third_party_fee_refund_detail import PaymentBalanceActivityThirdPartyFeeRefundDetail
from .payment_balance_activity_square_payroll_transfer_detail import PaymentBalanceActivitySquarePayrollTransferDetail
from .payment_balance_activity_square_payroll_transfer_reversed_detail import (
    PaymentBalanceActivitySquarePayrollTransferReversedDetail,
)
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class PayoutEntry(UncheckedBaseModel):
    """
    One or more PayoutEntries that make up a Payout. Each one has a date, amount, and type of activity.
    The total amount of the payout will equal the sum of the payout entries for a batch payout
    """

    id: str = pydantic.Field()
    """
    A unique ID for the payout entry.
    """

    payout_id: str = pydantic.Field()
    """
    The ID of the payout entries’ associated payout.
    """

    effective_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of when the payout entry affected the balance, in RFC 3339 format.
    """

    type: typing.Optional[ActivityType] = pydantic.Field(default=None)
    """
    The type of activity associated with this payout entry.
    See [ActivityType](#type-activitytype) for possible values
    """

    gross_amount_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of money involved in this payout entry.
    """

    fee_amount_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The amount of Square fees associated with this payout entry.
    """

    net_amount_money: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The net proceeds from this transaction after any fees.
    """

    type_app_fee_revenue_details: typing.Optional[PaymentBalanceActivityAppFeeRevenueDetail] = pydantic.Field(
        default=None
    )
    """
    Details of any developer app fee revenue generated on a payment.
    """

    type_app_fee_refund_details: typing.Optional[PaymentBalanceActivityAppFeeRefundDetail] = pydantic.Field(
        default=None
    )
    """
    Details of a refund for an app fee on a payment.
    """

    type_automatic_savings_details: typing.Optional[PaymentBalanceActivityAutomaticSavingsDetail] = pydantic.Field(
        default=None
    )
    """
    Details of any automatic transfer from the payment processing balance to the Square Savings account. These are, generally, proportional to the merchant's sales.
    """

    type_automatic_savings_reversed_details: typing.Optional[PaymentBalanceActivityAutomaticSavingsReversedDetail] = (
        pydantic.Field(default=None)
    )
    """
    Details of any automatic transfer from the Square Savings account back to the processing balance. These are, generally, proportional to the merchant's refunds.
    """

    type_charge_details: typing.Optional[PaymentBalanceActivityChargeDetail] = pydantic.Field(default=None)
    """
    Details of credit card payment captures.
    """

    type_deposit_fee_details: typing.Optional[PaymentBalanceActivityDepositFeeDetail] = pydantic.Field(default=None)
    """
    Details of any fees involved with deposits such as for instant deposits.
    """

    type_deposit_fee_reversed_details: typing.Optional[PaymentBalanceActivityDepositFeeReversedDetail] = pydantic.Field(
        default=None
    )
    """
    Details of any reversal or refund of fees involved with deposits such as for instant deposits.
    """

    type_dispute_details: typing.Optional[PaymentBalanceActivityDisputeDetail] = pydantic.Field(default=None)
    """
    Details of any balance change due to a dispute event.
    """

    type_fee_details: typing.Optional[PaymentBalanceActivityFeeDetail] = pydantic.Field(default=None)
    """
    Details of adjustments due to the Square processing fee.
    """

    type_free_processing_details: typing.Optional[PaymentBalanceActivityFreeProcessingDetail] = pydantic.Field(
        default=None
    )
    """
    Square offers Free Payments Processing for a variety of business scenarios including seller referral or when Square wants to apologize for a bug, customer service, repricing complication, and so on. This entry represents details of any credit to the merchant for the purposes of Free Processing.
    """

    type_hold_adjustment_details: typing.Optional[PaymentBalanceActivityHoldAdjustmentDetail] = pydantic.Field(
        default=None
    )
    """
    Details of any adjustment made by Square related to the holding or releasing of a payment.
    """

    type_open_dispute_details: typing.Optional[PaymentBalanceActivityOpenDisputeDetail] = pydantic.Field(default=None)
    """
    Details of any open disputes.
    """

    type_other_details: typing.Optional[PaymentBalanceActivityOtherDetail] = pydantic.Field(default=None)
    """
    Details of any other type that does not belong in the rest of the types.
    """

    type_other_adjustment_details: typing.Optional[PaymentBalanceActivityOtherAdjustmentDetail] = pydantic.Field(
        default=None
    )
    """
    Details of any other type of adjustments that don't fall under existing types.
    """

    type_refund_details: typing.Optional[PaymentBalanceActivityRefundDetail] = pydantic.Field(default=None)
    """
    Details of a refund for an existing card payment.
    """

    type_release_adjustment_details: typing.Optional[PaymentBalanceActivityReleaseAdjustmentDetail] = pydantic.Field(
        default=None
    )
    """
    Details of fees released for adjustments.
    """

    type_reserve_hold_details: typing.Optional[PaymentBalanceActivityReserveHoldDetail] = pydantic.Field(default=None)
    """
    Details of fees paid for funding risk reserve.
    """

    type_reserve_release_details: typing.Optional[PaymentBalanceActivityReserveReleaseDetail] = pydantic.Field(
        default=None
    )
    """
    Details of fees released from risk reserve.
    """

    type_square_capital_payment_details: typing.Optional[PaymentBalanceActivitySquareCapitalPaymentDetail] = (
        pydantic.Field(default=None)
    )
    """
    Details of capital merchant cash advance (MCA) assessments. These are, generally, proportional to the merchant's sales but may be issued for other reasons related to the MCA.
    """

    type_square_capital_reversed_payment_details: typing.Optional[
        PaymentBalanceActivitySquareCapitalReversedPaymentDetail
    ] = pydantic.Field(default=None)
    """
    Details of capital merchant cash advance (MCA) assessment refunds. These are, generally, proportional to the merchant's refunds but may be issued for other reasons related to the MCA.
    """

    type_tax_on_fee_details: typing.Optional[PaymentBalanceActivityTaxOnFeeDetail] = pydantic.Field(default=None)
    """
    Details of tax paid on fee amounts.
    """

    type_third_party_fee_details: typing.Optional[PaymentBalanceActivityThirdPartyFeeDetail] = pydantic.Field(
        default=None
    )
    """
    Details of fees collected by a 3rd party platform.
    """

    type_third_party_fee_refund_details: typing.Optional[PaymentBalanceActivityThirdPartyFeeRefundDetail] = (
        pydantic.Field(default=None)
    )
    """
    Details of refunded fees from a 3rd party platform.
    """

    type_square_payroll_transfer_details: typing.Optional[PaymentBalanceActivitySquarePayrollTransferDetail] = (
        pydantic.Field(default=None)
    )
    """
    Details of a payroll payment that was transferred to a team member’s bank account.
    """

    type_square_payroll_transfer_reversed_details: typing.Optional[
        PaymentBalanceActivitySquarePayrollTransferReversedDetail
    ] = pydantic.Field(default=None)
    """
    Details of a payroll payment to a team member’s bank account that was deposited back to the seller’s account by Square.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
