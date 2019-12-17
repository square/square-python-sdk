# Change Log

## Version 2.3.0-20191217 (2019-12-17)
!!!important
Square is excited to announce the public release of customized SDKs for [Java](https://github.com/square/square-java-sdk) and [.NET](https://github.com/square/square-dotnet-sdk). For more information, see [Square SDKs](/sdks).
!!!

* __GA release:__ SDKs updated to support new `receipt_url` and `receipt_number` fields added to the  [Payment](${SQUARE_TECH_REF}/objects/Payment) type.  

* __Beta release:__ SDKs updated to support the new [CashDrawerShifts](cashdrawershift-api/reporting) API.

* Square now follows the semantic versioning scheme that uses three numbers to delineate MAJOR, MINOR, and PATCH versions of our SDK. In addition, the SDK version also includes the API version so you know what Square API version the SDK is related to. For more information, see [Versioning and SDKs](build-basics/versioning-overview#versioning-and-sdks).


## Version 2.20191120.0 (2019-11-20)
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
