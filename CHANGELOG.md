# Change Log

## Version 5.2.2.20200422 (2020-04-25)
## Existing API updates

* **OAuth API**
  * [Obtain Token](https://developer.squareup.com/reference/square_2020-04-22/oauth-api/obtain-token) endpoint: Removed the `scopes` property from the request body.

## Version 5.2.1.20200422 (2020-04-22)
## API releases
* **Customer Segments API (beta).** `limit` field removed from **ListCustomerSegments** endpoint.


**Note:** This release fixes a bug introduced on the [April 22, 2020](changelog/connect-logs/2020-04-22) release of the Square API.

## Version 5.2.0.20200422 (2020-04-22)
## API releases
* **Terminal API.** The new Terminal API lets a custom third-party POS app integrate with the Square Terminal to send terminal checkout requests to collect payments.
  * For an overview, see [Overview](/terminal-api/overview).
  * For technical reference, see [Terminal API](${SQUARE_TECH_REF}/terminal-api).

* **Devices API.** The new Devices API lets a custom third-party POS app generate a code used to sign in to a Square Terminal to create a pairing that lets the POS app send terminal checkout requests. For technical reference, see [Devices API](${SQUARE_TECH_REF}/devices-api).

* **Customer Groups API (beta).** The new Customer Groups API (Beta) enables full CRUD management of customer groups, including the ability to list, retrieve, create, update, and delete customer groups. Previously, this functionality was only available through the Square dashboard and point-of-sale product interfaces. 
  * For an overview, see [Overview](/customer-groups-api/what-it-does) 
  * For technical reference, see [Customer Groups](${SQUARE_TECH_REF}/customer-groups-api).  

* **Customer Segments API (beta).** The new Customer Segments API (Beta) lets you list and retrieve customer segment (also called smart groups) information. Coupled with the new `segment_ids` field on the customer resource, this API lets you better understand and track the customer segments to which a customer belongs.
  * For an overview, see [Overview](/customer-segmentss-api/what-it-does) 
  * For technical reference, see [Customer Segments]( ${SQUARE_TECH_REF}/customer-segments-api).  

   
* **New webhooks.** v2 Webhooks (beta) now supports webhooks for the following APIs:
  * Orders API. `order.created`, `order.updated`, and `order.fulfillment.updated`
  * Terminal API. `terminal.checkout.created` and `terminal.checkout.updated`
  * Devices API. `device.code.paired`
 
  For more information, see [Subscribe to Events](webhooks-api/subscribe-to-events).

## Existing API updates
* **Customers API**
	* [AddGroupToCustomer](${SQUARE_TECH_REF}/customers-api/add-group-to-customer) endpoint. Added to add customer memberships to a customer group.  
	* [RemoveGroupFromCustomer](${SQUARE_TECH_REF}/customers-api/remove-group-from-customer) endpoint. Added to remove customer memberships from a customer group.
	* [Customer](${SQUARE_TECH_REF}/obects/Customer) object. Updated as follows:
		* [`group_ids`](${SQUARE_TECH_REF}/obects/Customer#definition__property-group_ids) field. Added to designate groups the customer is in.
		* [`segment_ids`](${SQUARE_TECH_REF}/obects/Customer#definition__property-segment_ids) field. Added to designate segments the customer is in. 
		* [`groups`](${SQUARE_TECH_REF}/obects/Customer#definition__property-groups) field. Deprecated to be replaced by `group_ids` and `segment_ids`. It remains supported for one year from this release.
	* [CustomerQuery](${SQUARE_TECH_REF}/objects/CustomerQuery) object's `filter` parameter. Updated as follows:  
		*  `group_ids` filter. Added to search for customers based on whether they belong to any, all, or none of the specified groups.


* **Orders API**
  * [OrderFulfillmentPickupDetails](${SQUARE_TECH_REF}/objects/OrderFulfillmentPickupDetails) type updated to support curbside pickup:
    * `is_curbside_pickup`. This Boolean field indicates curbside pickup.
    * `CurbsidePickupDetails`. This type provides supporting information for curbside pickup, including a buyer description (for example, "buyer is in a red car") and a timestamp when the buyer arrived for the pickup.


* **OAuth API**
  * [RevokeToken](${SQUARE_TECH_REF}/oauth-api/revoke-token) endpoint. Added a new field called [revoke_only_access_token](${SQUARE_TECH_REF}/oauth-api/revoke-token#request__property-revoke_only_access_token). This field allows a client to revoke an access token but leave the parent authorization active.
  * [ObtainToken](${SQUARE_TECH_REF}/oauth-api/obtain-token) endpoint. Added a new field called [scopes](${SQUARE_TECH_REF}/oauth-api/obtain-token#request__property-scopes). This field lets a client change the set of permissions for an access token when making a request to refresh the token.


* **Catalog API**
  * [CatalogQuickAmountsSettings](${SQUARE_TECH_REF}/objects/CatalogQuickAmountsSettings) type. Added to support predefined custom payment amounts in the Square Register checkout dialog box.
  * ENUM`CatalogItemProductType`. The ENUM value `GIFT_CARD` is now deprecated.

* **Payments API.** See [Take Payments and Collect Fees](/payments-api/take-payments-and-collect-fees) for updated information about permission requirements, Square reporting of the application fee collected by an app, and how to collect fees internationally.

## Version 5.1.0.20200325 (2020-03-25)
## Existing API updates
* **[Payments API](${SQUARE_TECH_REF}/payments-api).** In support of the existing [Delayed capture](payments-api/take-payments) for payments, the following fields are added to the [Payment](${SQUARE_TECH_REF}/objects/Payment) type:
   * `delay_duration`. In a [CreatePayment](${SQUARE_TECH_REF}/payments-api/create-payment) request, you can set `autocomplete` to false to get  payment approval but not charge the payment source. You can now add this field to specify a time period to complete (or cancel) the payment. For more information, see [Delay capture](payments-api/take-payments).
   * `delay_action`. Defines the action that Square takes on the payment when the `delay_duration` elapses. In this release, the API supports only the cancel payment action.
   * `delayed_until`. Provides the date and time on Square servers when Square applies `delay_action` on the payment.

## Version 5.0.0.20200226 (2020-02-26)
## API releases
* **GA release**: All SDKs have been updated to support the new Bank Accounts and CashDrawerShifts APIs.

* **Beta release**: All SDKs have been updated to support the new Disputes API.


## Existing API updates

All SDKs have been updated to support the following changes:

* **Catalog API**    
  * Batch upsert catalog objects endpoint &mdash; The `batches` field is now required and the array must have at least one element.   
  * CatalogModifier &mdash; Two fields added:
     * `ordinal` to support custom ordering in a modifier list   
     * `modifier_list_id` to reference the parent modifier list
  * CatalogModifierList &mdash; New field added: `ordinal` to support custom ordering in a list of **CatalogModifierList** objects.

* **Customers API changes**
  * SearchCustomers endpoint &mdash; `limit` size reduced from 1000 to 100 to improve the endpoint performance. 

* **Orders API changes**
  * CreateOrderRequest &mdash; Previously these request fields were deprecated: `line_items`, `taxes`, `discounts`. These fields are no longer available. Instead you now use the `Order` object in the request. For example, `Order.line_items`, `Order.taxes`, and `Order.discounts`.
  * OrderLineItem type &mdash; There are two changes:
    * The `taxes` field that was previously deprecated is no longer available. Instead, you now use the `OrderLineItem.applied_taxes` field. This also now requires that you set the `OrderLineItemTax.scope` field. 
    * The `discounts` field that was previously deprecated is no longer available. Instead, you now use the `OrderLineItem.applied_discounts` field. This also now requires that you set the `OrderLineItemDiscount.scope` field. 

* **Shared object updates**
  * **Card object** &mdash; New fields added: `card_type`, `prepaid_type`. Currently, only the Payments API responses populate these fields. 

## Version 4.1.0.20200122 (2020-01-22)

* New field:  The **Employee** object now has an `is_owner` field.
* New enumeration:  The **CardBrand** enumeration has a new `SQUARE_CAPITAL_CARD` enum value to support a Square one-time Installments payment.

* New request body field constraint: The __Refund__ Payment request now requires a payment_id. 

## Version 4.0.0-20191217 (2019-12-17)
!!!important
Square is excited to announce the public release of customized SDKs for [Java](https://github.com/square/square-java-sdk) and [.NET](https://github.com/square/square-dotnet-sdk). For more information, see [Square SDKs](/sdks).
!!!

* __GA release:__ SDKs updated to support new `receipt_url` and `receipt_number` fields added to the  [Payment](${SQUARE_TECH_REF}/objects/Payment) type.  

* __Beta release:__ SDKs updated to support the new [CashDrawerShifts](cashdrawershift-api/reporting) API.

* Square now follows the semantic versioning scheme for all SDKs except PHP and Node.js. This versioning scheme uses three numbers to delineate MAJOR, MINOR, and PATCH versions of our SDK. In addition, the SDK version also includes the API version so you know what Square API version the SDK is related to. For more information, see [Versioning and SDKs](build-basics/versioning-overview#versioning-and-sdks).
* Java, .Net, Python, and Ruby SDKs are now version 4.0.0. Java and .Net SDKs have breaking changes in version 4.0.0. Ruby and Python do not have breaking changes.

## Version 3.20191120.0 (2019-11-20)
!!!important
Square has begun the retirement process for Connect v1 APIs. See the [Connect v1 Retirement](/migrate-from-v1) information page for details.
!!!

* __GA releases:__ SDKs now support the new `modify_tax_basis` field to Discounts and v2 Sandbox
* __BETA releases:__ SDKs now support the Shifts API webhooks for Labor shift created, updated, deleted, CreateLocation endpoint, and the ability to customize statement description in Payments API.
* **Deprecated**: Support for v1Items API and v1Locations API is fully deprecated.

## 3.20191023.0 (2019-10-23)
* **GA release**: Merchants.ListMerchant is GA for all SDKs.
* **Beta release**: All SDKs support exclusion strategies for pricing rules.

## 3.20190925.0 (2019-09-25)

* **GA release**: All SDKs have been updated to support the new Merchants API.

* **Beta release**: All SDKs have been updated to support the new endpoints (RetrieveLocation, UpdateLocation) added to the Locations API.

* **Beta release**: All SDKs have been updated to support the new field (`mcc`) added to the `Location` type. 

* **GA release**:  All SDKs have been updated to support the new field (`bin`) added to the `Card` type. 

* **GA release**: All SDKs have been updated to support the new `CardPaymentDetails` fields  (`verification_results`, `statement_description`, and `verification_method`). 

* **GA release**: All SDKs have been updated to support the new `Payment` field, (`employee_id`).
