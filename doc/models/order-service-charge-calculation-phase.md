## Order Service Charge Calculation Phase

Represents a phase in the process of calculating order totals. Service charges will
be applied after the phase indicated.

[Read more about how order totals are calculated.](https://developer.squareup.com/docs/orders-api/how-it-works#how-totals-are-calculated)

### Enumeration

`OrderServiceChargeCalculationPhase`

### Fields

| Name | Description |
|  --- | --- |
| `SUBTOTAL_PHASE` | The service charge will be applied after discounts but before taxes. |
| `TOTAL_PHASE` | The service charge will be applied after both discounts and taxes are applied. |

