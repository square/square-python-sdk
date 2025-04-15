# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing
from .money import MoneyParams
from ..types.order_service_charge_calculation_phase import OrderServiceChargeCalculationPhase
from .order_line_item_applied_tax import OrderLineItemAppliedTaxParams
from ..types.order_service_charge_treatment_type import OrderServiceChargeTreatmentType
from ..types.order_service_charge_scope import OrderServiceChargeScope


class OrderReturnServiceChargeParams(typing_extensions.TypedDict):
    """
    Represents the service charge applied to the original order.
    """

    uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    A unique ID that identifies the return service charge only within this order.
    """

    source_service_charge_uid: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The service charge `uid` from the order containing the original
    service charge. `source_service_charge_uid` is `null` for
    unlinked returns.
    """

    name: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The name of the service charge.
    """

    catalog_object_id: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The catalog object ID of the associated [OrderServiceCharge](entity:OrderServiceCharge).
    """

    catalog_version: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The version of the catalog object that this service charge references.
    """

    percentage: typing_extensions.NotRequired[typing.Optional[str]]
    """
    The percentage of the service charge, as a string representation of
    a decimal number. For example, a value of `"7.25"` corresponds to a
    percentage of 7.25%.
    
    Either `percentage` or `amount_money` should be set, but not both.
    """

    amount_money: typing_extensions.NotRequired[MoneyParams]
    """
    The amount of a non-percentage-based service charge.
    
    Either `percentage` or `amount_money` should be set, but not both.
    """

    applied_money: typing_extensions.NotRequired[MoneyParams]
    """
    The amount of money applied to the order by the service charge, including
    any inclusive tax amounts, as calculated by Square.
    
    - For fixed-amount service charges, `applied_money` is equal to `amount_money`.
    - For percentage-based service charges, `applied_money` is the money calculated using the percentage.
    """

    total_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total amount of money to collect for the service charge.
    
    __NOTE__: If an inclusive tax is applied to the service charge, `total_money`
    does not equal `applied_money` plus `total_tax_money` because the inclusive
    tax amount is already included in both `applied_money` and `total_tax_money`.
    """

    total_tax_money: typing_extensions.NotRequired[MoneyParams]
    """
    The total amount of tax money to collect for the service charge.
    """

    calculation_phase: typing_extensions.NotRequired[OrderServiceChargeCalculationPhase]
    """
    The calculation phase after which to apply the service charge.
    See [OrderServiceChargeCalculationPhase](#type-orderservicechargecalculationphase) for possible values
    """

    taxable: typing_extensions.NotRequired[typing.Optional[bool]]
    """
    Indicates whether the surcharge can be taxed. Service charges
    calculated in the `TOTAL_PHASE` cannot be marked as taxable.
    """

    applied_taxes: typing_extensions.NotRequired[typing.Optional[typing.Sequence[OrderLineItemAppliedTaxParams]]]
    """
    The list of references to `OrderReturnTax` entities applied to the
    `OrderReturnServiceCharge`. Each `OrderLineItemAppliedTax` has a `tax_uid`
    that references the `uid` of a top-level `OrderReturnTax` that is being
    applied to the `OrderReturnServiceCharge`. On reads, the applied amount is
    populated.
    """

    treatment_type: typing_extensions.NotRequired[OrderServiceChargeTreatmentType]
    """
    The treatment type of the service charge.
    See [OrderServiceChargeTreatmentType](#type-orderservicechargetreatmenttype) for possible values
    """

    scope: typing_extensions.NotRequired[OrderServiceChargeScope]
    """
    Indicates the level at which the apportioned service charge applies. For `ORDER`
    scoped service charges, Square generates references in `applied_service_charges` on
    all order line items that do not have them. For `LINE_ITEM` scoped service charges,
    the service charge only applies to line items with a service charge reference in their
    `applied_service_charges` field.
    
    This field is immutable. To change the scope of an apportioned service charge, you must delete
    the apportioned service charge and re-add it as a new apportioned service charge.
    See [OrderServiceChargeScope](#type-orderservicechargescope) for possible values
    """
