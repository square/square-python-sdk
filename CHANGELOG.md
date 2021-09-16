# Change Log

## Version 14.1.0.20210915 (2021-09-15)
## API updates

* **Invoices API:** 
  * [Invoice](https://developer.squareup.com/reference/square_2021-09-15/objects/Invoice) object. Added a new, optional `sale_or_service_date` field used to specify the date of the sale or the date that the service is rendered. If specified, this date is displayed on the invoice.

* **Orders API:**
   * [CreateOrder](https://developer.squareup.com/reference/square_2021-09-15/orders-api/create-order). The endpoint now supports creating temporary, draft orders. For more information, see [Create a draft order.](https://developer.squareup.com/docs/orders-api/create-orders#create-a-draft-order)
   * [CloneOrder](https://developer.squareup.com/reference/square_2021-09-15/orders-api/clone-order). The Orders API supports this new endpoint to clone an existing order. For more information, see [Clone an order.](https://developer.squareup.com/docs/orders-api/create-orders#clone-an-order)
   * These fields have moved to the [general availability (GA)](https://developer.squareup.com/docs/build-basics/api-lifecycle#general-availability) state: [OrderLineItem.item_type](https://developer.squareup.com/reference/square_2021-09-15/objects/OrderLineItem#definition__property-item_type), [OrderServiceCharge.type](https://developer.squareup.com/reference/square_2021-09-15/objects/OrderServiceCharge#definition__property-type), and `catalog_version` field on every order type that contains this field.

* **Team API:**
  * [SearchTeamMembersFilter](https://developer.squareup.com/reference/square_2021-09-15/objects/SearchTeamMembersFilter) object now has an `is_owner` field that when set, causes a team member search to return only the seller who owns a Square account.

* **Terminal API:**
  * [TerminalCheckout](https://developer.squareup.com/reference/square_2021-09-15/objects/TerminalCheckout) object.   The `customer_id` field is now GA. 

## Documentation updates
* **OAuth API:**
  * Revised API descriptions for the ObtainToken and Authorize endpoints. Clarified that the Authorize endpoint is not a callable API but is used to direct the seller to the Square authorization page. For more information about the Authorize endpoint, see [Create the Redirect URL and Square Authorization Page URL.](https://developer.squareup.com/docs/oauth-api/create-urls-for-square-authorization)


## Version 12.0.0.20210616 (2021-06-16)
## New API releases
* **Gift Cards API and Gift Card Activities API.** Gift card support is integrated in the [Square Seller Dashboard](https://squareup.com/dashboard/) and the [Square Point of Sale](https://squareup.com/us/en/point-of-sale)  application. Sellers can sell, redeem, track, and reload Square gift cards. Now developers can use the [Gift Cards API](https://developer.squareup.com/reference/square_2021-06-16/gift-cards-api) and the [Gift Card Activities API](https://developer.squareup.com/reference/square_2021-06-16/gift-card-activities-api) to integrate Square gift cards into third-party applications. For more information, see [Gift Cards API Overview.](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api)

* **Cards API.** The [Cards API](https://developer.squareup.com/reference/square_2021-06-16/cards-api) replaces the deprecated `CreateCustomerCard` and `DeleteCustomerCard` endpoints and lets an application save a customer payment card on file along with other card management operations. For more information, see [Cards API Overview.](https://developer.squareup.com/docs/cards-api/overview) 

## API updates
* **Catalog API:**
  * [CatalogPricingRule](https://developer.squareup.com/reference/square_2021-06-16/objects/CatalogPricingRule). Support of the [customer group discount](https://developer.squareup.com/reference/square_2021-06-16/objects/CatalogPricingRule#definition__property-customer_group_ids_any) becomes GA. For more information, see [CreateCustomerGroupDiscounts.](https://developer.squareup.com/docs/catalog-api/configure-customer-group-discounts)
  * [CatalogItemVariation](https://developer.squareup.com/reference/square_2021-06-16/objects/CatalogItemVariation). Offers Beta support of the [stockable](https://developer.squareup.com/reference/square_2021-06-16/objects/CatalogItemVariation#definition__property-stockable) and [stockable_conversion](https://developer.squareup.com/reference/square_2021-06-16/objects/CatalogItemVariation#definition__property-stockable_conversion) attributes to enable sales of a product in multiple measurement units.  
  * [UpsertCatalogObject](https://developer.squareup.com/reference/square_2021-06-16/catalog-api/upsert-catalog-object) and [BatchUpsertCatalogObjects](https://developer.squareup.com/reference/square_2021-06-16/catalog-api/batch-upsert-catalog-objects). Support creating an item with stockable and non-stockable variations with a specified stock conversion between the two. For more information, see [Enable Stock Conversion.](https://developer.squareup.com/docs/inventory-api/enable-stock-conversion)
  * [UpsertCatalogObject](https://developer.squareup.com/reference/square_2021-06-16/catalog-api/upsert-catalog-object) and [BatchUpsertCatalogObjects](https://developer.squareup.com/reference/square_2021-06-16/catalog-api/batch-upsert-catalog-objects). Require that an item be created with at least one variation. Otherwise, an `INVALID_REQUEST` error is returned. 
  
* **Customers API:**
  * Using the Customers API to manage cards on file is deprecated:
    * The [CreateCustomerCard](https://developer.squareup.com/reference/square_2021-06-16/customers-api/create-customer-card) endpoint is deprecated and replaced by the [CreateCard](https://developer.squareup.com/reference/square_2021-06-16/cards-api/create-card) and [LinkCustomerToGiftCard](https://developer.squareup.com/reference/square_2021-06-16/gift-cards-api/link-customer-to-gift-card) endpoints.
    * The [DeleteCustomerCard](https://developer.squareup.com/reference/square_2021-06-16/customers-api/delete-customer-card) endpoint is deprecated and replaced by the [DisableCard](https://developer.squareup.com/reference/square_2021-06-16/cards-api/disable-card) and [UnlinkCustomerFromGiftCard](https://developer.squareup.com/reference/square_2021-06-16/gift-cards-api/unlink-customer-from-gift-card) endpoints.
    * The `cards` field in the [Customer](https://developer.squareup.com/reference/square_2021-06-16/objects/Customer) object is deprecated and replaced by the following endpoints:
      * [ListCards](https://developer.squareup.com/reference/square_2021-06-16/cards-api/list-cards) to retrieve credit and debit cards on file.
      * [ListGiftCards](https://developer.squareup.com/reference/square_2021-06-16/gift-cards-api/list-gift-cards) to retrieve gift cards on file.  

       For more information, see [Migrate to the Cards API and Gift Cards API.](https://developer.squareup.com/docs/customers-api/use-the-api/integrate-with-other-services#migrate-customer-cards)
     
     * [Customer](https://developer.squareup.com/reference/square_2021-06-16/objects/Customer) object. In the `cards` field, the IDs for gift cards now have a `gftc:` prefix followed by the card number. This is a service-level change that applies to all Square API versions.

* **Disputes API:** 
  * The Disputes API is now GA. 
  * `RemoveDisputeEvidence`. Renamed to [DeleteDisputeEvidence](https://developer.squareup.com/reference/square_2021-06-16/objects/DeleteDisputeEvidence).
  * [CreateDisputeEvidenceFile.](https://developer.squareup.com/reference/square_2021-06-16/objects/CreateDisputeEvidenceFile) The URL is changed from `/v2/disputes/{dispute_id}/evidence_file` to `/v2/disputes/{dispute_id}/evidence-files`.
  * [CreateDisputeEvidenceText.](https://developer.squareup.com/reference/square_2021-06-16/objects/CreateDisputeEvidenceText) The URL is changed from `/v2/disputes/{dispute_id}/evidence_text` to `/v2/disputes/{dispute_id}/evidence-text`.
  * [ListDisputeEvidence.](https://developer.squareup.com/reference/square_2021-06-16/objects/ListDisputeEvidence) The  endpoint now returns a pagination cursor and accepts a pagination cursor in requests.
  * `DISPUTES_READ` and `DISPUTES_WRITE` permissions are required for all Disputes API endpoints instead of `PAYMENTS_READ` and `PAYMENTS_WRITE`.
  * [DisputeEvidence.](https://developer.squareup.com/reference/square_2021-06-16/objects/DisputeEvidence) The `evidence_id` field is deprecated and replaced by the `id` field.
  * The `dispute.state.changed` webhook is renamed to `dispute.state.updated`.
  * [Dispute](https://developer.squareup.com/reference/square_2021-06-16/objects/Dispute) object. The following breaking changes are made: 
    * The `dispute_id` field is deprecated and replaced by the `id` field.
    * The `reported_date` field is deprecated and replaced by the `reported_at` field.
    * The `evidence_ids` field is deprecated with no replacement.

  For more information about the GA release of the Disputes API, see [Disputes Overview.](https://developer.squareup.com/docs/disputes-api/overview) 
  

* **Inventory API:**
  * [CatalogStockConversion](https://developer.squareup.com/docs/{SQUARE_TECH_REF}/objects/CatalogStockConversion) (Beta). Enables selling a product in multiple measurement units and lets Square sellers manage inventory counts of the product's stockable and a non-stockable variations in a self-consistent manner. For more information, see [Enable Stock Conversion.](https://developer.squareup.com/docs/inventory-api/enable-stock-conversion)

* **Invoices API:**
  * [CreateInvoice.](https://developer.squareup.com/reference/square_2021-06-16/invoices-api/create-invoice) The `location_id` field is now optional and defaults to the location ID of the associated order. If specified in the request, the value must match the location ID of the associated order. This is a service-level change that applies to all Square API versions.

* **Loyalty API:**
  * [LoyaltyProgramAccrualRule](https://developer.squareup.com/reference/square_2021-06-16/objects/LoyaltyProgramAccrualRule) object. New `excluded_category_ids` and `excluded_item_variation_ids` fields that represent any categories and items that are excluded from accruing points in spend-based loyalty programs.

* **Subscriptions API:**
  * [Subscription.](https://developer.squareup.com/reference/square_2021-06-16/objects/Subscription) The `paid_until_date` field is renamed to `charge_through_date`.
  * [UpdateSubscription.](https://developer.squareup.com/reference/square_2021-06-16/subscriptions-api/update-subscription) The `version` field is now optional because it can update only the latest version of a subscription.

  * [CreateSubscription.](https://developer.squareup.com/reference/square_2021-06-16/subscriptions-api/create-subscription) The `idempotency_key` field is now optional in the request. If you do not provide it, each `CreateSubscription` assumes a unique (never used before) value and creates a subscription for each call.

## Documentation updates
* [Order fee structure.](https://developer.squareup.com/docs/payments-pricing#orders-api-fee-structure) Documented the transaction fee related to using the Orders API with a non-Square payments provider.


## Version 11.0.0.20210513 (2021-05-13)
## New API releases

* **Sites API.** The [Sites API](https://developer.squareup.com/reference/square_2021-05-13/sites-api) lets you retrieve basic details about the Square Online sites that belong to a Square seller. For more information, see [Sites API Overview.](https://developer.squareup.com/docs/sites-api/overview)


* **Snippets API.** The [Snippets API](https://developer.squareup.com/reference/square_2021-05-13/snippets-api) lets you manage snippets that provide custom functionality on Square Online sites. A snippet is a script that is injected into all pages on a site, except for checkout pages. For more information, see [Snippets API Overview.](https://developer.squareup.com/docs/snippets-api/overview)

The Sites API and Snippets API are publicly available to all developers as part of an early access program (EAP). For more information, see [Early access program for Square Online APIs.](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis)

## API updates

* **Payments API.**
  * [CreatePayment.](https://developer.squareup.com/reference/square_2021-05-13/payments-api/create-payment) The endpoint now supports ACH bank transfer payments. For more information, see [ACH Payment](https://developer.squareup.com/docs/payments-api/take-payments/ach-payments).

* **Loyalty API:**
  * The [Loyalty API](https://developer.squareup.com/docs/loyalty-api/overview) has moved to the [general availability](https://developer.squareup.com/docs/build-basics/api-lifecycle#general-availability) (GA) state.
  
  * The [ListLoyaltyPrograms](https://developer.squareup.com/reference/square_2021-05-13/loyalty-api/list-loyalty-programs) endpoint is deprecated and replaced by the [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2021-05-13/loyalty-api/retrieve-loyalty-program) endpoint when used with the `main` keyword.
  
  * [LoyaltyAccount](https://developer.squareup.com/reference/square_2021-05-13/objects/LoyaltyAccount)  object. The `mappings` field is retired and replaced by `mapping`. 

  * [LoyaltyAccountMapping](https://developer.squareup.com/reference/square_2021-05-13/objects/LoyaltyAccountMapping) object. The `type` and `value` fields are retired and replaced by `phone_number`.  
    
    Starting in Square version 2021-05-13: 
    * `mappings` is not accepted in `CreateLoyaltyAccount` requests or returned in responses.  
    * `type` and `value` are not accepted in `CreateLoyaltyAccount` or `SearchLoyaltyAccounts` requests or returned in responses.
    
    For more information, see [Migration notes.](https://developer.squareup.com/docs/loyalty-api/overview#migration-notes)
  
## Documentation updates
* **Getting Started** Added step that shows how to use the API Logs to examine a transaction. 


## Version 10.0.0.20210421 (2021-04-21)
## New API releases

## Existing API updates

* **Subscriptions API:** 
  *  [ResumeSubscription.](https://developer.squareup.com/reference/square_2021-04-21/subscriptions-api/resume-subscription) This new endpoint enables applications to resume [deactivated subscriptions.](https://developer.squareup.com/docs/subscriptions-api/overview#deactivated-subscriptions) After a subscription is created, there are events that can make a subscription non-billable, causing Square to deactivate the subscription. A seller can also resume deactivated subscriptions in the Seller Dashboard. Applications can call  [ListSubscriptionEvents](https://developer.squareup.com/reference/square_2021-04-21/subscriptions-api/list-subscription-events) to determine why Square deactivated a subscription.
 
* **Customers API:**

  * [Customer](https://developer.squareup.com/reference/square_2021-04-21/objects/Customer) object:
    * New `version` field (beta). This field represents the current version of the customer profile. You can include it in your `UpdateCustomer` and `DeleteCustomer` requests to  enable optimistic concurrency. For more information, see [Customer profile versions and optimistic concurrency support.](https://developer.squareup.com/docs/customers-api/what-it-does#customer-profile-versions-and-optimistic-concurrency-support) 
    * The `groups` field and corresponding `CustomerGroupInfo` object are retired.
    
  * [Customer webhooks](https://developer.squareup.com/docs/customers-api/use-the-api/customer-webhooks) have moved to the [general availability](https://developer.squareup.com/docs/build-basics/api-lifecycle#general-availability) (GA) state. Event notifications now include the `version` field (beta).
  
* **Invoices API:**

  * The [Invoices API](https://developer.squareup.com/docs/invoices-api/overview) has moved to the GA state.

  * [Invoice](https://developer.squareup.com/reference/square_2021-04-21/objects/Invoice) object:
    * A new required `accepted_payment_methods` field that defines the methods of payment that customers can use to pay an invoice on the Square-hosted invoice page. Valid values are defined in the new [InvoiceAcceptedPaymentMethods](https://developer.squareup.com/reference/square_2021-04-21/objects/InvoiceAcceptedPaymentMethods) enum. For more information, see the [migration notes.](https://developer.squareup.com/docs/invoices-api/overview#migration-notes)
    * A new `subscription_id` field, which is included in invoices created for subscription billing.

* **Loyalty API:** (beta)
 
  * [RetrieveLoyaltyProgram](https://developer.squareup.com/reference/square_2021-04-21/loyalty-api/retrieve-loyalty-program) endpoint. This new endpoint accepts a program ID or the `main` keyword and returns the loyalty program in a seller's account. For more information, see [Retrieve a loyalty program.](https://developer.squareup.com/docs/loyalty-api/overview#retrieve-loyalty-program) This endpoint is preferred over the `ListLoyaltyPrograms` endpoint.

  * Introduced a new mapping implementation for loyalty accounts:
    * [LoyaltyAccount](https://developer.squareup.com/reference/square_2021-04-21/objects/LoyaltyAccount) object. Added the `mapping` field (of type `LoyaltyAccountMapping`), which is used to associate the loyalty account with a buyer. This field is recommended over the `mappings` field.
    * [LoyaltyAccountMapping](https://developer.squareup.com/reference/square_2021-04-21/objects/LoyaltyAccountMapping) object. Added the `phone_number` field to represent a phone number mapping. This field is recommended over the `type` and `value` fields.

  * A new [loyalty.program.created](https://developer.squareup.com/reference/square_2021-04-21/webhooks/loyalty.program.created) webhook. Square now publishes an event notification when a loyalty program is created in the Square Seller Dashboard.

* **Inventory API:** 
  * [InventoryChange](https://developer.squareup.com/reference/square_2021-04-21/objects/InventoryChange) can now have its own measurement unit.

* **Catalog API:** 
  * [CatalogItem](https://developer.squareup.com/reference/square_2021-04-21/objects/CatalogItem) introduces the  `sort_name` attribute that can take Japanese writing scripts to sort items by. When it is unspecified, the regular `name` attribute is used for sorting.
  * [CatalogPricingRule](https://developer.squareup.com/reference/square_2021-04-21/objects/CatalogCatalogPricingRule) has the new `customer_group_ids_any` attribute included to support automatic application of discounts to specified product set purchased by members of any of the customer groups identified by the `customer_group_ids_any` attribute values.
* **Team API**
  * New [Team webhooks](https://developer.squareup.com/reference/square_2021-04-21/team-api/webhooks): `team_member.created`, `team_member.updated`, `team_member.wage_setting.updated` to notify on created and updated team members and wage settings.




## Version 9.1.0.20210317 (2021-03-17)

## Existing API updates

* **Payments API:**
  * [CreatePayment](https://developer.squareup.com/reference/square_2021-03-17/payments-api/create-payment). Until now, the `CreatePayment` endpoint supported only taking card payments. In this release, the API now supports cash and external payments. For more information, see [Take Payments.](https://developer.squareup.com/docs/payments-api/take-payments)
  * [UpdatePayment](https://developer.squareup.com/reference/square_2021-03-17/payments-api/update-payment). This new  endpoint enables developers to change the payment amount and tip amount after a payment is created. For more information, see [Update Payments.](https://developer.squareup.com/docs/payments-api/update-payments)
 
* **Invoices API:**
  * [InvoiceDeliveryMethod](https://developer.squareup.com/reference/square_2021-03-17/enums/InvoiceDeliveryMethod) enum. Added the read-only `SMS` value.  
  * [InvoiceRequestMethod](https://developer.squareup.com/reference/square_2021-03-17/enums/InvoiceRequestMethod) enum (deprecated). Added the read-only `SMS`, `SMS_CHARGE_CARD_ON_FILE`, and `SMS_CHARGE_BANK_ON_FILE` values for backward compatibility.  
  
  These values direct Square to send invoices and receipts to customers using SMS (text message). SMS settings can be configured from first-party Square applications only; they cannot be configured from the Invoices API. Square does not send invoice reminders when using SMS to communicate with customers.


* **Terminal API:**
  * [TerminalCheckout](https://developer.squareup.com/reference/square_2021-03-17/objects/TerminalCheckout). Previously, `TerminalCheckout` only supported tapped, dipped, or swiped credit cards. It now supports manual card entry and e-money. Added the `payment_type` field to denote a request for a manually entered payment card or an e-money payment.
  * [TerminalCheckoutPaymentType.](https://developer.squareup.com/reference/square_2021-03-17enums/TerminalCheckoutPaymentType) A new enum for the Terminal checkout payment types that can be requested.
  * [E-money support](https://developer.squareup.com/docs/terminal-api/e-money-payments) is now available for Terminal checkout requests in Japan.


## SDKs
* **Square Java SDK:**
  * Updated the OkHttp dependency to version 4.9.0.
  * Fixed a `NullPointerException` when passing an empty order ID to the `UpdateOrder` method.

## Documentation updates

* **Multi-language code examples.** Previously, various topics showed only cURL examples for the REST API operations. These topics now show examples in multiple languages. You can use the language drop-down list to choose a language.
  
* [When to Use Connect V1.](https://developer.squareup.com/docs/build-basics/using-connect-v1) Content is revised to reflect the most current information about when to use the Connect V1 API.


## Version 9.0.0.20210226 (2021-02-26)
## Existing API updates

* **Customers API:**

  * [New webhooks](https://developer.squareup.com/docs/customers-api/use-the-api/customer-webhooks) (beta). Square now sends notifications for the following events:
     * [customer.created](https://developer.squareup.com/reference/square_2021-02-26/webhooks/customer.created)
     * [customer.deleted](https://developer.squareup.com/reference/square_2021-02-26/webhooks/customer.deleted)
     * [customer.updated](https://developer.squareup.com/reference/square_2021-02-26/webhooks/customer.updated)

* **Orders API:**
   * [CreateOrder](https://developer.squareup.com/reference/square_2021-02-26/orders-api/create-order). Removed the `location_id` field from the request. It was an unused field.

* **Payments API:**
   * [Payment](https://developer.squareup.com/reference/square_2021-02-26/objects/Payment). This type now returns the `card_payment_timeline` [(CardPaymentTimeline](https://developer.squareup.com/reference/square_2021-02-26/objects/CardPaymentTimeline)) as part of the `card_details` field.

* **v1 Items API:**
  * The following endpoints are [retired:](https://developer.squareup.com/docs/build-basics/api-lifecycle)
    * `AdjustInventory`: Use the Square Inventory API [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-02-26/inventory-api/batch-change-inventory) endpoint.
    * `ListInventory`: Use the Square Inventory API  [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-02-26/inventory-api/batch-retrieve-inventory-counts) endpoint.

* **v1 Employees.Timecards:**
  * The following endpoints are retired:
    * `CreateTimecard`: Use the Square Labor API [CreateShift](https://developer.squareup.com/reference/square_2021-02-26/labor-api/create-shift) endpoint.
    * `DeleteTimecard`: Use the Square Labor API [DeleteShift](https://developer.squareup.com/reference/square_2021-02-26/labor-api/delete-shift) endpoint.
    * `ListTimecards`: Use the Square Labor API [SearchShift](https://developer.squareup.com/reference/square_2021-02-26/labor-api/search-shift) endpoint.
    * `RetrieveTimecards`: Use the Square Labor API [GetShift](https://developer.squareup.com/reference/square_2021-02-26/labor-api/get-shift) endpoint.
    * `UpdateTimecard`: Use the Square Labor API [UpdateShift](https://developer.squareup.com/reference/square_2021-02-26/labor-api/update-shift) endpoint.
    * `ListTimecardEvents`: No direct replacement. To learn about replacing the v1 functionality, see the [migration guide.](https://developer.squareup.com/docs/migrate-from-v1/guides/v1-timecards#endpoints)

* **v1 Employees.CashDrawers:**
  * The following endpoints are retired:
    * `ListCashDrawerShifts`: Use the Square CashDrawerShifts API [ListCashDrawerShifts](https://developer.squareup.com/reference/square_2021-02-26/cash-drawers-api/list-cash-drawer-shifts) endpoint.
    * `RetrieveCashDrawerShift`: Use the Square CashDrawerShifts API [RetrieveCashDrawerShift](https://developer.squareup.com/reference/square_2021-02-26/cash-drawers-api/retrieve-cash-drawer-shift) endpoint.
* **v1 Transactions.BankAccounts:**
  * The following endpoints are retired:
    * `ListBankAccounts`: Use the Square Bank Accounts API [ListBankAccounts](https://developer.squareup.com/reference/square_2021-02-26/bank-accounts-api/list-bank-accounts) endpoint.
    * `RetrieveBankAccount`: Use the Square Bank Accounts API [GetBankAccount](https://developer.squareup.com/reference/square_2021-02-26/bank-accounts-api/get-bank-account) endpoint.

## SDKs

* **All Square SDKs:**

    By default, all SDKs send requests to Square's production (https://connect.squareup.com) or sandbox (https://connect.squareupsandbox.com) hosts based on the client's `environment` parameter.

    You now have the option to use a custom URL instead. To use a custom URL, follow the example for your language to set the `environment` parameter to `custom` and the `customUrl` parameter to your URL:

    - Java

      ```java
      new SquareClient.Builder()
        .environment(Environment.CUSTOM)
        .customUrl("https://example.com")
      ```

    - .NET

      ```csharp
      new Square.SquareClient.Builder()
        .Environment(Environment.Custom)
        .CustomUrl("https://example.com")
      ```

    - Node.js

      ```javascript
      new Client({
        environment: Environment.Custom,
        customUrl: 'https://example.com'
      });
      ```

    - PHP

      ```php
      new Square\SquareClient([
        'environment' => Environment::CUSTOM,
        'customUrl' => 'https://example.com',
      ]);
      ```

    - Python

      ```python
      Client(
        environment = 'custom',
        custom_url = 'https://example.com',)
      ```

    - Ruby

      ```ruby
      Square::Client.new(
        environment: 'custom',
        custom_url: 'https://example.com'
      });
      ```


* **Square .NET SDK:**

  Square has overridden the `Equals` and `GetHashCode` methods for models:

  * In the `Equals` override, Square has implemented a field-level comparison.
  * The Square `GetHashCode` override now ensures that hashes are deterministic and unique for each object.

* **Square Node.js SDK:**

  Endpoints that return 64-bit integers now return a `BigInt` object instead of a `Number` object.


* **Connect Node.js SDK:** (deprecated)

  The deprecated Connect Node.js SDK is in the security [maintenance state.](https://developer.squareup.com/docs/build-basics/api-lifecycle#maintenance) It does not receive any bug fixes or API updates from the Square version 2021-02-26 release. However, the SDK will receive support and security patches until it is retired (end of life) in the second quarter of 2021. For more information, including steps for migrating to the [Square Node.js SDK,](https://github.com/square/square-nodejs-sdk) see the [Connect SDK README.](https://github.com/square/connect-nodejs-sdk/blob/master/README.md)

## Documentation updates
* **Catalog API:**
  * [Update Catalog Objects.](https://developer.squareup.com/docs/catalog-api/update-catalog-objects) Provides programming guidance to update catalog objects.

* **Inventory API:**
  * [List or retrieve inventory.](https://developer.squareup.com/docs/migrate-from-v1/guides/v1-items#list-or-retrieve-inventory) Migrate the retired v1 endpoint of `ListInventory` to the v2 endpoint of `BatchRetrieveInventoryCounts`. Compare and contrast the programming patterns between the v1 endpoint of `ListInventory` and its v2 counterparts of [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-02-26/inventory-api/batch-retrieve-inventory-counts) or [RetrieveInventoryCount](https://developer.squareup.com/reference/square_2021-02-26/inventory-api/retrieve-inventory-count).
  * [Adjust or change inventory.](https://developer.squareup.com/docs/migrate-from-v1/guides/v1-items#adjust-or-change-inventory) Migrate the retired v1 endpoint of `AdjustInventory` to the v2 endpoint of `BatchChangeInventory`. Compare and contrast the programming patterns between the v1 endpoint of `AdjustInventory` and its v2 counterparts of [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-02-26/inventory-api/batch-change-inventory).

* **Get Started topic.** Revised the [Get Started](https://developer.squareup.com/docs/get-started) experience. In addition to clarifications, it now includes the use of the Square Sandbox and API Explorer. These are the tools and environments developers use to explore Square APIs.


## Version 8.1.0.20210121 (2021-01-21T00:00)
## Existing API updates

* **Invoices API:** (beta)

  The `InvoicePaymentRequest.request_method` field is deprecated, and its current options are separated into two new fields that better represent their scope:
  * `Invoice.delivery_method` specifies how Square should send invoices, reminders, and receipts to the customer.
  * `InvoicePaymentRequest.automatic_payment_source` specifies the payment method for an automatic payment.

  As part of this change, the [InvoiceDeliveryMethod](https://developer.squareup.com/reference/square_2021-01-21/enums/InvoiceDeliveryMethod) and [InvoiceAutomaticPaymentSource](https://developer.squareup.com/reference/square_2021-01-21/enums/InvoiceAutomaticPaymentSource) enums are added and the `InvoiceRequestMethod` enum is deprecated.

  The Invoices API will continue to accept `request_method` in create and update requests until the field is retired, but starting in this version, `request_method` is not included in returned `Invoice` objects. For more information, see the [migration notes.](https://developer.squareup.com/docs/invoices-api/overview#migrate-InvoicePaymentRequest.request_method)


* **Locations API:**
  * The [Locations.MCC](https://developer.squareup.com/reference/square_2021-01-21/objects/Location#definition__property-mcc) field is now updatable (beta). You can use the `UpdateLocation` endpoint to update the merchant category code (MCC) associated with a seller location. For more information, see [Initialize a merchant category code.](https://developer.squareup.com/docs/locations-api#initialize-a-merchant-category-code)




## SDKs
* **Connect Node.js SDK:** (deprecated)

  The deprecated Connect Node.js SDK is in the security [maintenance state.](https://developer.squareup.com/docs/build-basics/api-lifecycle#maintenance) It will not receive any bug fixes or API updates from the Square version 2021-01-21 release. However, the SDK will receive support and security patches until it is retired (EOL) in Q2, 2021. For more information, including steps for migrating to the [Square Node.js SDK,](https://github.com/square/square-nodejs-sdk) see the [Connect SDK README.](https://github.com/square/connect-nodejs-sdk/blob/master/README.md)

## Documentation updates
* **Catalog API:**
  * The [Use Item Options to Manage Item Variations](https://developer.squareup.com/docs/catalog-api/item-options-migration) topic is added. It demonstrates how item variations are usually used and how item options can be used to enable random access to item variations.

* **Inventory API:**
  * The [Inventory API](inventory-api/what-it-does) content is updated. It provides clearer guidance about how to use the API, with a task-oriented TOC and improved code examples.



## Version 8.0.0.20201216 (2020-12-16T00:00)
## Existing API updates

* **Orders API:**
  * [OrderLineItemPricingBlocklists.](https://developer.squareup.com/reference/square_2020-12-16/objects/OrderLineItemPricingBlocklists) You can explicitly specify taxes and discounts in an order or automatically apply preconfigured taxes and discounts to an order. In addition, you can now block applying these taxes and discounts to a specific [OrderLineItem](https://developer.squareup.com/reference/square_2020-12-16/objects/OrderLineItem) in an [order](https://developer.squareup.com/reference/square_2020-12-16/objects/Order). You add the `pricing_blocklists` attribute to individual line items and specify the `blocked_discounts` and `blocked_taxes` that you do not want to apply. For more information, see [Apply Taxes and Discounts.](https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts) For example walkthroughs, see [Automatically Apply Discounts](https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts/auto-apply-discounts) and [Automatically Apply Taxes.](https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts/auto-apply-taxes)
  * [OrderPricingOptions](https://developer.squareup.com/reference/square_2020-12-16/objects/OrderPricingOptions). Previously, the `pricing_options` field in an [order](https://developer.squareup.com/reference/square_2020-12-16/objects/OrderPricingOptions) supported only `auto_apply_discounts` to enable the automatic application of preconfigured discounts. Now it also supports `auto_apply_taxes` to enable the automatic application of preconfigured taxes. For more information, see [Automatically apply preconfigured catalog taxes or discounts.](https://developer.squareup.com/docs/orders-api/apply-taxes-and-discounts#automatically-apply-preconfigured-catalog-taxes-or-discounts)

  * [OrderLineItemTax](https://developer.squareup.com/reference/square_2020-12-16/objects/OrderLineItemTax). It now includes the new `auto_applied` field. It indicates whether the tax was automatically applied using a preconfigured [CatalogTax](https://developer.squareup.com/reference/square_2020-12-16/objects/CatalogTax).


* **Bookings API:**
  * The [CancelBooking](https://developer.squareup.com/reference/square_2020-12-16/bookings-api/cancel-booking) endpoint supports canceling an accepted or pending booking.
  * The [booking.created](https://developer.squareup.com/reference/square_2020-12-16/webhooks/booking.created) webhook event notifies when a new booking is created by calling the [CreateBooking](https://developer.squareup.com/reference/square_2020-12-16/bookings-api/cancel-booking) endpoint.
  * The [booking.updated](https://developer.squareup.com/reference/square_2020-12-16/webhooks/booking.updated) webhook event notifies when an existing booking is updated.

* **Catalog API:**
  * [ListCatalog](https://developer.squareup.com/reference/square_2020-12-16/catalog-api/list-catalog), [RetrieveCatalogObject](https://developer.squareup.com/reference/square_2020-12-16/catalog-api/retrieve-catalog-object), and [BatchRetrieveCatalogObjects](https://developer.squareup.com/reference/square_2020-12-16/catalog-api/batch-retrieve-catalog-objects) now support the `catalog_version` filter to return catalog objects of the specified version.

* **Customers API:**
  * [SearchCustomers](https://developer.squareup.com/reference/square_2020-12-16/customers-api/search-customers) endpoint. The `email_address`, `group_ids`, `phone_number`, and `reference_id` query filters are now generally available (GA).
  * The [Customer Groups](https://developer.squareup.com/reference/square_2020-12-16/customer-groups-api) API is now GA.
  * The [Customer Segments](https://developer.squareup.com/reference/square_2020-12-16/customer-segments-api) API is now GA.


* **Invoices API:** (beta)
  * [Invoice](https://developer.squareup.com/reference/square_2020-12-16/objects/Invoice) object. Added the  `custom_fields` field, which contains up to two customer-facing, seller-defined fields to display on the invoice. For more information, see [Custom fields.](https://developer.squareup.com/docs/invoices-api/overview#custom-fields)
    As part of this change, the following objects are added:
      * [InvoiceCustomField](https://developer.squareup.com/reference/square_2020-12-16/objects/InvoiceCustomField) object
      * [InvoiceCustomFieldPlacement](https://developer.squareup.com/reference/square_2020-12-16/enums/InvoiceCustomFieldPlacement) enum
  * [InvoiceRequestMethod](https://developer.squareup.com/reference/square_2020-12-16/enums/InvoiceRequestMethod) enum. Added the read-only CHARGE_BANK_ON_FILE value, which represents a bank transfer automatic payment method for a recurring invoice.


* **Loyalty API:** (beta)
  * [LoyaltyProgramRewardTier](https://developer.squareup.com/reference/square_2020-12-16/objects/LoyaltyProgramRewardTier) object. The `definition` field in this type is deprecated and replaced by the new `pricing_rule_reference` field. You can use `pricing_rule_reference` fields to retrieve catalog objects that define the discount details for the reward tier. For more information, see [Get discount details for a reward tier.](https://developer.squareup.com/docs/loyalty-api/overview#get-discount-details-for-a-reward-tier)
    As part of this change, the following APIs are deprecated:
      * [LoyaltyProgramRewardDefinition](https://developer.squareup.com/reference/square_2020-12-16/objects/LoyaltyProgramRewardDefinition) object
      * [LoyaltyProgramRewardDefinitionScope](https://developer.squareup.com/reference/square_2020-12-16/enums/LoyaltyProgramRewardDefinitionScope) enum
      * [LoyaltyProgramRewardDefinitionType](https://developer.squareup.com/reference/square_2020-12-16/enums/LoyaltyProgramRewardDefinitionType) enum

## New SDK release
* **Square Node.js SDK:**

  The new [Square Node.js SDK](https://github.com/square/square-nodejs-sdk) is now GA and replaces the deprecated Connect Node.js SDK. For migration information, see the [Connect SDK README.](https://github.com/square/connect-nodejs-sdk/blob/master/README.md)


## Documentation updates

* [Get Right-Sized Permissions with Down-Scoped OAuth Tokens.](https://developer.squareup.com/docs/oauth-api/cookbook/downscoped-access) This new OAuth API topic shows how to get an additional reduced-scope OAuth token with a 24-hour expiration by using the refresh token from the Square account authorization OAuth flow.


## Version 7.0.0.20201118 (2020-11-18T00:00)
## New API releases

* **Bookings API** (beta). This API enables you, as an application developer, to create applications to set up and manage bookings for appointments of fixed duration in which  selected staff members of a Square seller provide specified services in supported locations for particular customers.
  * For an overview, see [Manage Bookings for Square Sellers](https://developer.squareup.com/docs/bookings-api/what-it-is).
  * For technical reference, see [Bookings API](https://developer.squareup.com/reference/square_2020-11-18/bookings-api).

## Existing API updates

*  **Payments API:**
   *  [Payment.](https://developer.squareup.com/reference/square_2020-11-18/objects/Payment) The object now includes the `risk_evaluation` field to identify the Square-assigned risk level associated with the payment. Sellers can use this information to provide the goods and services or refund the payment.

## New SDK release
* **New Square Node.js SDK (beta)**

  The new [Square Node.js SDK](https://github.com/square/square-nodejs-sdk) is available in beta and will eventually replace the deprecated Connect Node.js SDK. For migration information, see the [Connect SDK README.](https://github.com/square/connect-nodejs-sdk/blob/master/README.md) The following topics are updated to use the new SDK:
   * [Walkthrough: Integrate Square Payments in a Website](https://developer.squareup.com/docs/payment-form/payment-form-walkthrough)
   * [Verify the Buyer When Using a Nonce for an Online Payment](https://developer.squareup.com/docs/payment-form/cookbook/verify-buyer-on-card-charge)
   * [Create a Gift Card Payment Endpoint](https://developer.squareup.com/docs/payment-form/gift-cards/part-2)


## Documentation Updates

* The **Testing** topics are moved from the end of the table of contents to the top, in the **Home** section under [Testing your App](https://developer.squareup.com/docs/testing-your-app).
* [Pay for orders.]](https://developer.squareup.com/docs/orders-api/pay-for-order) Topic revised to add clarity when to use Payments API and Orders API to pay for an order. The [Orders Integration]](https://developer.squareup.com/docs/payments-api/take-payments?preview=true#orders-integration) topic in Payments API simplified accordingly.


## Version 6.5.0.20201028 (2020-10-28T00:00)

## Existing API updates

* **Terminal API.** New endpoints to enable sellers in Canada refund Interac payments.
    *  New endpoints:

       * [CreateTerminalRefund](https://developer.squareup.com/reference/square_2020-10-28/terminal-api/create-terminal-refund)
        * [GetTerminalRefund](https://developer.squareup.com/reference/square_2020-10-28/terminal-api/get-terminal-refund)
       * [CancelTerminalRefund](https://developer.squareup.com/reference/square_2020-10-28/terminal-api/cancel-terminal-refund)
       * [SearchTerminalRefunds](https://developer.squareup.com/reference/square_2020-10-28/terminal-api/search-terminal-refunds)

  * New webhooks:
     * `terminal.refund.created`. Notification of a new Terminal refund request.
     * `terminal.refund.updated`. Notification that a Terminal refund request state is changed.

  * New topic [Refund Interac Payments.](https://developer.squareup.com/docs/terminal-api/square-terminal-refunds). Describes how to refund Interac payments.

*  **Loyalty API (beta):**
   *  [SearchLoyaltyAccounts.](https://developer.squareup.com/reference/square_2020-10-28/loyalty-api/search-loyalty-accounts) The endpoint supports a new query parameter to search by customer ID.

* **Locations API:**
  * [Location](https://developer.squareup.com/reference/square_2020-10-28/objects/Location) object. Has a new read-only field,[full_format_logo_url](https://developer.squareup.com/reference/square_2020-10-28/objects/Location#definition__property-full_format_logo_url), which provides URL of a full-format logo image for the location.
  * [Webhooks](https://developer.squareup.com/docs/webhooks-api/subscribe-to-events#locations) The Locations API now supports notifications for when a location is created and when a location is updated.

* **Orders API:**
  * [RetrieveOrder](https://developer.squareup.com/reference/square_2020-10-28/orders-api/retrieve-order), new endpoint. For more information, see the [Retrieve Orders](https://developer.squareup.com/docs/orders-api/manage-orders#retrieve-orders) overview.

* **Invoices API (beta):**
  * [Invoice](https://developer.squareup.com/reference/square_2020-10-28/objects/Invoice) object. The [payment_requests](https://developer.squareup.com/reference/square_2020-10-28/objects/Invoice#definition__property-payment_requests) field can now contain up to 13 payment requests, with a maximum of 12 `INSTALLMENT` request types. This is a service-level change that applies to all Square API versions. For more information, see [Payment requests.](https://developer.squareup.com/docs/invoices-api/overview#payment-requests)

## Version 6.4.0.20200923 (2020-09-23)
## Existing API updates
* Invoices API (beta)
  * [InvoiceStatus](https://developer.squareup.com/reference/square_2020-09-23/enums/InvoiceStatus) enum. Added the `PAYMENT_PENDING` value. Previously, the Invoices API returned a `PAID` or `PARTIALLY_PAID` status for invoices in a payment pending state. Now, the Invoices API returns a `PAYMENT_PENDING` status for all invoices in a payment pending state, including those previously returned as `PAID` or `PARTIALLY_PAID`.
* Payments API
  * [ListPayment](https://developer.squareup.com/reference/square_2020-09-23/payments-api/list-payments). The endpoint now supports the `limit` parameter.
* Refunds API
  * [ListPaymentRefunds](https://developer.squareup.com/reference/square_2020-09-23/refunds-api/list-payment-refunds). The endpoint now supports the `limit` parameter.
* [DeviceDetails](https://developer.squareup.com/reference/square_2020-09-23/objects/DeviceDetails#definition__property-device_installation_id). The object now includes the `device_installation_id` field.
## Documentation updates
* [Payment status.](https://developer.squareup.com/docs/payments-api/take-payments#payment-status) Added details about the `Payment.status` changes and how the status relates to the seller receiving the funds.
* [Refund status.](https://developer.squareup.com/docs/payments-api/refund-payments#refund-status) Added details about the `PaymentRefund.status` changes and how the status relates to the cardholder receiving the funds.
* [CreateRefund errors.](https://developer.squareup.com/docs/payments-api/error-codes#createrefund-errors) Added documentation for the `REFUND_DECLINED` error code.

## Version 6.3.0.20200826 (2020-08-26)
## Existing API updates
* Orders API
  * [Order](https://developer.squareup.com/reference/square_2020-08-26/objects/Order) object. The `total_tip_money` field is now GA.
  * [CreateOrder](https://developer.squareup.com/reference/square_2020-08-26/orders-api/create-order), [UpdateOrder](https://developer.squareup.com/reference/square_2020-08-26/orders-api/update-order), and [BatchRetrieveOrders](https://developer.squareup.com/reference/square_2020-08-26/orders-api/batch-retrieve-orders). These APIs now support merchant-scoped endpoints (for example, the `CreateOrder` endpoint `POST /v2/orders`). The location-scoped variants of these endpoints (for example, the `CreateOrder` endpoint `POST /v2/locations/{location_id}/orders`) continue to work, but these endpoints are now deprecated. You should use the merchant-scoped endpoints (you provide the location information in the request body).
* Labor API
	* [Migrate from Employees to Team Members.](https://developer.squareup.com/docs/labor-api/migrate-to-teams) The Employees API is now deprecated in this release. Accordingly, update references to the  `Shift.employee_id` field to the `Shift.team_member_id` field of the Labor API.
* v2 Employees API (deprecated)
	* [Migrate from the Square Employees API.](https://developer.squareup.com/docs/team/migrate-from-v2-employees) The v2 Employees API is now deprecated. This topic provides information to migrate to the Team API.
* v1 Employees API (deprecated)
	* [Migrate from the v1 Employees API.](https://developer.squareup.com/docs/migrate-from-v1/guides/v1-employees) The v1 Employees API is now deprecated. This topic provides information to migrate to the Team API.

## Documentation updates
* Point of Sale API
	* [Build on iOS.](https://developer.squareup.com/docs/pos-api/build-on-ios) Corrected the Swift example code in step 7.
* Team API
	* [Team API Overview.](https://developer.squareup.com/docs/team/overview) Documented the limitation related to creating a team member in the Square Sandbox.

## All SDKs

SDK technical reference documentation:

* Nulls in SDK documentation example code are replaced with example values.

## .NET SDK

Bug fixes:

* The `APIException.Errors` property was not set on instantiation. Behavior is now corrected to instantiate the class with an empty `Errors` list.

## Version 6.2.0.20200812 (2020-08-12)
## API releases
* Subscriptions API (beta):
  * For an overview, see [Square Subscriptions.](https://developer.squareup.com/docs/subscriptions/overview)
  * For technical reference, see [Subscriptions API.](https://developer.squareup.com/reference/square_2020-08-12/subscriptions-api)

## Existing API updates
* Catalog API
	* [CatalogSubscriptionPlan](https://developer.squareup.com/reference/square_2020-08-12/objects/CatalogSubscriptionPlan) (beta). This catalog type is added in support of the Subscriptions API. Subscription plans are stored as catalog object of the `SUBSCRIPTION_PLAN` type. For more information, see [Set Up and Manage a Subscription Plan.](https://developer.squareup.com/docs/subscriptions-api/setup-plan)

## SqPaymentForm SDK updates
* [SqPaymentForm.masterpassImageURL.](https://developer.squareup.com/docs/api/paymentform#masterpassimageurl) This function is updated to return a Secure Remote Commerce background image URL.

## Documentation updates
* Locations API
	* [About the main location.](https://developer.squareup.com/docs/locations-api#about-the-main-location) Added  clarifying information about the main location concept.
* OAuth API
	* [Migrate to the Square API OAuth Flow.](https://developer.squareup.com/docs/oauth-api/migrate-to-square-oauth-flow) Added a new topic to document migration from a v1 location-scoped OAuth access token to the Square seller-scoped OAuth access token.
* Payment Form SDK
  * Renamed the Add a Masterpass Button topic to [Add a Secure Remote Commerce Button.](https://developer.squareup.com/docs/payment-form/add-digital-wallets/masterpass) Updated the instructions to add a Secure Remote Commerce button to replace a legacy Masterpass button.
  * [Payment form technical reference.](https://developer.squareup.com/docs/api/paymentform) Updated the reference to show code examples for adding a Secure Remote Commerce button.

## Version 6.1.0.20200722 (2020-07-22)
## API releases

* Invoices API (beta):
  * For an overview, see [Manage Invoices Using the Invoices API](https://developer.squareup.com/docs/invoices-api/overview).
  * For technical reference, see [Invoices API](https://developer.squareup.com/reference/square_2020-07-22/invoices-api).

## Existing API updates

* Catalog API
	* [SearchCatalogItems](https://developer.squareup.com/reference/square_2020-07-22/catalog-api/search-catalog-items). You can now call the new search endpoint to [search for catalog items or item variations](https://developer.squareup.com/docs/catalog-api/search-catalog-items), with simplified programming experiences, using one or more of the supported query filters, including the custom attribute value filter.
* Locations API
  * [Locations API Overview](https://developer.squareup.com/docs/locations-api). Introduced the "main" location concept.
  * [RetrieveLocation](https://developer.squareup.com/reference/square_2020-07-22/locations-api/retrieve-location). You can now specify "main" as the location ID to retrieve the main location information.

* Merchants API
  * [RetrieveMerchant](https://developer.squareup.com/reference/square_2020-07-22/merchants-api/retrieve-merchant) and [ListMerchants](https://developer.squareup.com/reference/square_2020-07-22/merchants-api/retrieve-merchant). These endpoints now return a new field, `main_location_id`.

* Orders API
  * [PricingOptions](https://developer.squareup.com/reference/square_2020-07-22/objects/Order#definition__property-pricing_options). You can now enable the `auto_apply_discounts` of the options to have rule-based discounts automatically applied to an [Order](https://developer.squareup.com/reference/square_2020-07-22/objects/Order) that is pre-configured with a [pricing rule](https://developer.squareup.com/reference/square_2020-07-22/objects/CatalogPricingRule).

* [Inventory API](https://developer.squareup.com/reference/square_2020-07-22/inventory-api)
	* Replaced 500 error on max string length exceeded with a max length error message. Max length attribute added to string type fields.

* Terminal API (beta)
	* [TerminalCheckout](https://developer.squareup.com/reference/square_2020-07-22/objects/TerminalCheckout) object. The `TerminalCheckoutCancelReason` field is renamed to `ActionCancelReason`.

## Documentation updates

* Catalog API
	* [Search a catalog](https://developer.squareup.com/docs/catalog-api/search-catalog). New topics added to provide actionable guides to using the existing [SearchCatalogObjects](https://developer.squareup.com/reference/square_2020-07-22/catalog-api/search-catalog-objects) endpoint, in addition to the [SearchCatalogItems](https://developer.squareup.com/reference/square_2020-07-22/catalog-api/search-catalog-items) endpoints.

* Orders API
	* [Create Orders](https://developer.squareup.com/docs/orders-api/create-orders). Updated existing content with the new pricing option for the automatic application of rule-based discounts.


## Version 6.0.0.20200625 (2020-06-25)

## New API release
* Team API generally available (GA)
  * For an overview, see [Team API Overview](https://developer.squareup.com/docs/team/overview).
  * For technical reference, see [Team API](https://developer.squareup.com/reference/square_2020-06-25/team-api).

## Existing API updates
* Catalog API
  * [Pricing](https://developer.squareup.com/reference/square_2020-06-25/objects/CatalogPricingRule) is now GA. It allows an application to configure catalog item pricing rules for the specified discounts to apply automatically.
* Payments API
  * The [CardPaymentDetails](https://developer.squareup.com/reference/square_2020-06-25/objects/CardPaymentDetails) type now supports a new field, [refund_requires_card_presence](https://developer.squareup.com/reference/square_2020-06-25/objects/CardPaymentDetails#definition__property-refund_requires_card_presence). When set to true, the payment card must be physically present to refund a payment.

## Version 5.3.0.20200528 (2020-05-28)

## API releases

* Loyalty API (beta):
  * For an overview, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview?train=2020-05-28).
  * For technical reference, see [Loyalty API](https://developer.squareup.com/reference/square/loyalty-api).

## Existing API updates

* Orders API
  * [CalculateOrder (beta)](https://developer.squareup.com/reference/square/orders-api/calculate-order) endpoint. Use the endpoint to calculate adjustments (for example, taxes and discounts) to an order for preview purposes. In response, the endpoint returns the order showing the calculated totals. You can use this endpoint with an existing order or an order that has not been created.

  The endpoint does not update an existing order. It only returns a calculated view of the order that you provided in the request. To create or update an order, use the [CreateOrder](https://developer.squareup.com/reference/square/orders-api/create-order) and [UpdateOrder](https://developer.squareup.com/reference/square/orders-api/update-order) endpoints, respectively.
  * [Order](https://developer.squareup.com/reference/square_2020-05-28/objects/Order?train=2020-05-28) type. Two fields are added in support of the Loyalty API integration. For more information, see [Deferred reward creation](https://developer.squareup.com/docs/loyalty-api/overview?train=2020-05-28#deferred-reward-creation). For an example, see [Redeem Points](https://developer.squareup.com/docs/loyalty-api/walkthrough1/redeem-points?train=2020-05-28).
    * `Order.rewards` represents rewards added to an order by calling the [CreateLoyaltyReward](https://developer.squareup.com/reference/square/loyalty-api/create-loyalty-reward) endpoint.
    * `Order.discount.reward_ids` indicates that a discount is the result of the specified rewards that were added to an order using the `CreateLoyaltyReward` endpoint.

* Customers API

  * The [Search Customers](https://developer.squareup.com/reference/square/customers-api/search-customers) endpoint supports search by email address, phone number, and reference ID with the following additional query filters:

    * The [`email_address` query filter](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#search-by-email-address) (beta) supports an [exact](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#exact-search-by-email-address) or [fuzzy](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#fuzzy-search-by-email-address) search for customer profiles by their email addresses.

    * The [`phone_number` query filter](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#search-by-phone-number) (beta) supports an [exact](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#exact-search-by-phone-number) or [fuzzy](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#fuzzy-search-by-phone-number) search for customer profiles by their phone numbers.

    * The [`reference_id` query filter](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#search-by-reference-id) (beta) supports an [exact](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#exact-search-by-reference-id) or [fuzzy](https://developer.squareup.com/docs/customers-api/cookbook/search-customers?train=2020-05-28#fuzzy-search-by-reference-id) search for customer profiles by their reference IDs.

  * The [`created_at`](https://developer.squareup.com/reference/square/objects/Customer#definition__property-created_at), [`updated_at`](https://developer.squareup.com/reference/square/objects/Customer#definition__property-updated_at), and [`id`](https://developer.squareup.com/reference/square/objects/Customer#definition__property-id) attributes on the [Customer](https://developer.squareup.com/docs/S%7BSQUARE_TECH_REF%7D/objects/customers?train=2020-05-28) resource are updated to be optional. As a result, they no longer are required input parameters when you call the Square SDKs to create a `Customer` object. You might need to update the dependent SDKs to the latest version to mediate breaking your existing code.

## Square Webhooks

* [Square Webhooks](https://developer.squareup.com/reference/square/webhooks) (formerly v2 Webhooks). The status is changed from beta to general availability (GA).

* [v1 Webhooks](https://developer.squareup.com/docs/webhooks-api/v1-tech-ref?train=2020-05-28). The v1 Inventory and Timecards webooks are now deprecated and replaced by [inventory.count.updated](https://developer.squareup.com/reference/square/webhooks/inventory.count.updated) and [labor.shift.updated](https://developer.squareup.com/reference/square/webhooks/inventory.count.updated).

## Version 5.2.2.20200422 (2020-04-25)
## Existing API updates

* **OAuth API**
  * [Obtain Token](https://developer.squareup.com/reference/square/oauth-api/revoke-token) endpoint: Removed the `scopes` property from the request body.

## Version 5.2.1.20200422 (2020-04-22)
## API releases
* **Customer Segments API (beta).** `limit` field removed from **ListCustomerSegments** endpoint.


**Note:** This release fixes a bug introduced on the [April 22, 2020](changelog/connect-logs/2020-04-22) release of the Square API.

## Version 5.2.0.20200422 (2020-04-22)
## API releases
* **Terminal API.** The new Terminal API lets a custom third-party POS app integrate with the Square Terminal to send terminal checkout requests to collect payments.
  * For an overview, see [Overview](https://developer.squareup.com/docs/terminal-api/overview).
  * For technical reference, see [Terminal API](https://developer.squareup.com/reference/square/terminal-api).

* **Devices API.** The new Devices API lets a custom third-party POS app generate a code used to sign in to a Square Terminal to create a pairing that lets the POS app send terminal checkout requests. For technical reference, see [Devices API](https://developer.squareup.com/reference/square/devices-api).

* **Customer Groups API (beta).** The new Customer Groups API (Beta) enables full CRUD management of customer groups, including the ability to list, retrieve, create, update, and delete customer groups. Previously, this functionality was only available through the Square dashboard and point-of-sale product interfaces.
  * For an overview, see [Overview](https://developer.squareup.com/docs/customer-groups-api/what-it-does)
  * For technical reference, see [Customer Groups](https://developer.squareup.com/reference/square/customer-groups-api).

* **Customer Segments API (beta).** The new Customer Segments API (Beta) lets you list and retrieve customer segment (also called smart groups) information. Coupled with the new `segment_ids` field on the customer resource, this API lets you better understand and track the customer segments to which a customer belongs.
  * For an overview, see [Overview](https://developer.squareup.com/docs/customer-segmentss-api/what-it-does)
  * For technical reference, see [Customer Segments]( https://developer.squareup.com/reference/square/customer-segments-api).


* **New webhooks** v2 Webhooks (beta) now supports webhooks for the following APIs:
  * Orders API. `order.created`, `order.updated`, and `order.fulfillment.updated`
  * Terminal API. `terminal.checkout.created` and `terminal.checkout.updated`
  * Devices API. `device.code.paired`

  For more information, see [Subscribe to Events](webhooks-api/subscribe-to-events).

## Existing API updates
* **Customers API**
	* [AddGroupToCustomer](https://developer.squareup.com/reference/square/customers-api/add-group-to-customer) endpoint. Added to add customer memberships to a customer group.
	* [RemoveGroupFromCustomer](https://developer.squareup.com/reference/square/customers-api/remove-group-from-customer) endpoint. Added to remove customer memberships from a customer group.
	* [Customer](https://developer.squareup.com/reference/square/obects/Customer) object. Updated as follows:
		* [`group_ids`](https://developer.squareup.com/reference/square/obects/Customer#definition__property-group_ids) field. Added to designate groups the customer is in.
		* [`segment_ids`](https://developer.squareup.com/reference/square/obects/Customer#definition__property-segment_ids) field. Added to designate segments the customer is in.
		* [`groups`](https://developer.squareup.com/reference/square/obects/Customer#definition__property-groups) field. Deprecated to be replaced by `group_ids` and `segment_ids`. It remains supported for one year from this release.
	* [CustomerQuery](https://developer.squareup.com/reference/square/objects/CustomerQuery) object's `filter` parameter. Updated as follows:
		*  `group_ids` filter. Added to search for customers based on whether they belong to any, all, or none of the specified groups.


* **Orders API**
  * [OrderFulfillmentPickupDetails](https://developer.squareup.com/reference/square/objects/OrderFulfillmentPickupDetails) type updated to support curbside pickup:
    * `is_curbside_pickup`. This Boolean field indicates curbside pickup.
    * `CurbsidePickupDetails`. This type provides supporting information for curbside pickup, including a buyer description (for example, "buyer is in a red car") and a timestamp when the buyer arrived for the pickup.


* **OAuth API**
  * [RevokeToken](https://developer.squareup.com/reference/square/oauth-api/revoke-token) endpoint. Added a new field called [revoke_only_access_token](https://developer.squareup.com/reference/square/oauth-api/revoke-token#request__property-revoke_only_access_token). This field allows a client to revoke an access token but leave the parent authorization active.
  * [ObtainToken](https://developer.squareup.com/reference/square/oauth-api/obtain-token) endpoint. Added a new field called [scopes](https://developer.squareup.com/reference/square/oauth-api/obtain-token#request__property-scopes). This field lets a client change the set of permissions for an access token when making a request to refresh the token.


* **Catalog API**
  * [CatalogQuickAmountsSettings](https://developer.squareup.com/reference/square/objects/CatalogQuickAmountsSettings) type. Added to support predefined custom payment amounts in the Square Register checkout dialog box.
  * ENUM`CatalogItemProductType`. The ENUM value `GIFT_CARD` is now deprecated.

* **Payments API.** See [Take Payments and Collect Fees](https://developer.squareup.com/docs/payments-api/take-payments-and-collect-fees) for updated information about permission requirements, Square reporting of the application fee collected by an app, and how to collect fees internationally.

## Version 5.1.0.20200325 (2020-03-25)
## Existing API updates
* **[Payments API](https://developer.squareup.com/reference/square/payments-api).** In support of the existing [Delayed capture]](https://developer.squareup.com/docs/payments-api/take-payments) for payments, the following fields are added to the [Payment](https://developer.squareup.com/reference/square/objects/Payment) type:
   * `delay_duration`. In a [CreatePayment](https://developer.squareup.com/reference/square/payments-api/create-payment) request, you can set `autocomplete` to false to get  payment approval but not charge the payment source. You can now add this field to specify a time period to complete (or cancel) the payment. For more information, see [Delay capture]](https://developer.squareup.com/docs/payments-api/take-payments).
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
Square is excited to announce the public release of customized SDKs for [Java](https://github.com/square/square-java-sdk) and [.NET](https://github.com/square/square-dotnet-sdk). For more information, see [Square SDKs](https://developer.squareup.com/docs/sdks).
!!!

* __GA release:__ SDKs updated to support new `receipt_url` and `receipt_number` fields added to the  [Payment](https://developer.squareup.com/reference/square/objects/Payment) type.

* __Beta release:__ SDKs updated to support the new [CashDrawerShifts](cashdrawershift-api/reporting) API.

* Square now follows the semantic versioning scheme for all SDKs except PHP and Node.js. This versioning scheme uses three numbers to delineate MAJOR, MINOR, and PATCH versions of our SDK. In addition, the SDK version also includes the API version so you know what Square API version the SDK is related to. For more information, see [Versioning and SDKs](https://developer.squareup.com/docs/build-basics/versioning-overview#versioning-and-sdks).
* Java, .Net, Python, and Ruby SDKs are now version 4.0.0. Java and .Net SDKs have breaking changes in version 4.0.0. Ruby and Python do not have breaking changes.

## Version 3.20191120.0 (2019-11-20)
!!!important
Square has begun the retirement process for Connect v1 APIs. See the [Connect v1 Retirement](https://developer.squareup.com/docs/migrate-from-v1) information page for details.
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
