## Terminal Checkout Cancel Reason

### Enumeration

`TerminalCheckoutCancelReason`

### Fields

| Name | Description |
|  --- | --- |
| `BUYER_CANCELED` | A person canceled the `TerminalCheckout` from a Square device. |
| `SELLER_CANCELED` | A client canceled the `TerminalCheckout` using the API. |
| `TIMED_OUT` | The `TerminalCheckout` timed out (see `deadline_duration` on the `TerminalCheckout`). |

