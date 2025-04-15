# -*- coding: utf-8 -*-

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from square_legacy.configuration import Configuration
from square_legacy.api.base_api import BaseApi
from square_legacy.http.auth.o_auth_2 import OAuth2
from square_legacy.api.mobile_authorization_api import MobileAuthorizationApi
from square_legacy.api.o_auth_api import OAuthApi
from square_legacy.api.v1_transactions_api import V1TransactionsApi
from square_legacy.api.apple_pay_api import ApplePayApi
from square_legacy.api.bank_accounts_api import BankAccountsApi
from square_legacy.api.bookings_api import BookingsApi
from square_legacy.api.booking_custom_attributes_api import BookingCustomAttributesApi
from square_legacy.api.cards_api import CardsApi
from square_legacy.api.cash_drawers_api import CashDrawersApi
from square_legacy.api.catalog_api import CatalogApi
from square_legacy.api.customers_api import CustomersApi
from square_legacy.api.customer_custom_attributes_api\
    import CustomerCustomAttributesApi
from square_legacy.api.customer_groups_api import CustomerGroupsApi
from square_legacy.api.customer_segments_api import CustomerSegmentsApi
from square_legacy.api.devices_api import DevicesApi
from square_legacy.api.disputes_api import DisputesApi
from square_legacy.api.employees_api import EmployeesApi
from square_legacy.api.events_api import EventsApi
from square_legacy.api.gift_cards_api import GiftCardsApi
from square_legacy.api.gift_card_activities_api import GiftCardActivitiesApi
from square_legacy.api.inventory_api import InventoryApi
from square_legacy.api.invoices_api import InvoicesApi
from square_legacy.api.labor_api import LaborApi
from square_legacy.api.locations_api import LocationsApi
from square_legacy.api.location_custom_attributes_api\
    import LocationCustomAttributesApi
from square_legacy.api.checkout_api import CheckoutApi
from square_legacy.api.transactions_api import TransactionsApi
from square_legacy.api.loyalty_api import LoyaltyApi
from square_legacy.api.merchants_api import MerchantsApi
from square_legacy.api.merchant_custom_attributes_api\
    import MerchantCustomAttributesApi
from square_legacy.api.orders_api import OrdersApi
from square_legacy.api.order_custom_attributes_api import OrderCustomAttributesApi
from square_legacy.api.payments_api import PaymentsApi
from square_legacy.api.payouts_api import PayoutsApi
from square_legacy.api.refunds_api import RefundsApi
from square_legacy.api.sites_api import SitesApi
from square_legacy.api.snippets_api import SnippetsApi
from square_legacy.api.subscriptions_api import SubscriptionsApi
from square_legacy.api.team_api import TeamApi
from square_legacy.api.terminal_api import TerminalApi
from square_legacy.api.vendors_api import VendorsApi
from square_legacy.api.webhook_subscriptions_api import WebhookSubscriptionsApi


class Client(object):
    @staticmethod
    def sdk_version():
        return '41.0.0.20250319'

    @staticmethod
    def square_version():
        return '2025-03-19'

    def user_agent_detail(self):
        return self.config.user_agent_detail

    @LazyProperty
    def mobile_authorization(self):
        return MobileAuthorizationApi(self.global_configuration)

    @LazyProperty
    def o_auth(self):
        return OAuthApi(self.global_configuration)

    @LazyProperty
    def v1_transactions(self):
        return V1TransactionsApi(self.global_configuration)

    @LazyProperty
    def apple_pay(self):
        return ApplePayApi(self.global_configuration)

    @LazyProperty
    def bank_accounts(self):
        return BankAccountsApi(self.global_configuration)

    @LazyProperty
    def bookings(self):
        return BookingsApi(self.global_configuration)

    @LazyProperty
    def booking_custom_attributes(self):
        return BookingCustomAttributesApi(self.global_configuration)

    @LazyProperty
    def cards(self):
        return CardsApi(self.global_configuration)

    @LazyProperty
    def cash_drawers(self):
        return CashDrawersApi(self.global_configuration)

    @LazyProperty
    def catalog(self):
        return CatalogApi(self.global_configuration)

    @LazyProperty
    def customers(self):
        return CustomersApi(self.global_configuration)

    @LazyProperty
    def customer_custom_attributes(self):
        return CustomerCustomAttributesApi(self.global_configuration)

    @LazyProperty
    def customer_groups(self):
        return CustomerGroupsApi(self.global_configuration)

    @LazyProperty
    def customer_segments(self):
        return CustomerSegmentsApi(self.global_configuration)

    @LazyProperty
    def devices(self):
        return DevicesApi(self.global_configuration)

    @LazyProperty
    def disputes(self):
        return DisputesApi(self.global_configuration)

    @LazyProperty
    def employees(self):
        return EmployeesApi(self.global_configuration)

    @LazyProperty
    def events(self):
        return EventsApi(self.global_configuration)

    @LazyProperty
    def gift_cards(self):
        return GiftCardsApi(self.global_configuration)

    @LazyProperty
    def gift_card_activities(self):
        return GiftCardActivitiesApi(self.global_configuration)

    @LazyProperty
    def inventory(self):
        return InventoryApi(self.global_configuration)

    @LazyProperty
    def invoices(self):
        return InvoicesApi(self.global_configuration)

    @LazyProperty
    def labor(self):
        return LaborApi(self.global_configuration)

    @LazyProperty
    def locations(self):
        return LocationsApi(self.global_configuration)

    @LazyProperty
    def location_custom_attributes(self):
        return LocationCustomAttributesApi(self.global_configuration)

    @LazyProperty
    def checkout(self):
        return CheckoutApi(self.global_configuration)

    @LazyProperty
    def transactions(self):
        return TransactionsApi(self.global_configuration)

    @LazyProperty
    def loyalty(self):
        return LoyaltyApi(self.global_configuration)

    @LazyProperty
    def merchants(self):
        return MerchantsApi(self.global_configuration)

    @LazyProperty
    def merchant_custom_attributes(self):
        return MerchantCustomAttributesApi(self.global_configuration)

    @LazyProperty
    def orders(self):
        return OrdersApi(self.global_configuration)

    @LazyProperty
    def order_custom_attributes(self):
        return OrderCustomAttributesApi(self.global_configuration)

    @LazyProperty
    def payments(self):
        return PaymentsApi(self.global_configuration)

    @LazyProperty
    def payouts(self):
        return PayoutsApi(self.global_configuration)

    @LazyProperty
    def refunds(self):
        return RefundsApi(self.global_configuration)

    @LazyProperty
    def sites(self):
        return SitesApi(self.global_configuration)

    @LazyProperty
    def snippets(self):
        return SnippetsApi(self.global_configuration)

    @LazyProperty
    def subscriptions(self):
        return SubscriptionsApi(self.global_configuration)

    @LazyProperty
    def team(self):
        return TeamApi(self.global_configuration)

    @LazyProperty
    def terminal(self):
        return TerminalApi(self.global_configuration)

    @LazyProperty
    def vendors(self):
        return VendorsApi(self.global_configuration)

    @LazyProperty
    def webhook_subscriptions(self):
        return WebhookSubscriptionsApi(self.global_configuration)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=None, retry_methods=None,
                 environment='production',
                 custom_url='https://connect.squareup.com', access_token=None,
                 bearer_auth_credentials=None, square_version='2025-03-19',
                 additional_headers={}, user_agent_detail='', config=None):
        self.config = config or Configuration(
            http_client_instance=http_client_instance,
            override_http_client_configuration=override_http_client_configuration,
            http_call_back=http_call_back, timeout=timeout,
            max_retries=max_retries, backoff_factor=backoff_factor,
            retry_statuses=retry_statuses, retry_methods=retry_methods,
            environment=environment, custom_url=custom_url,
            access_token=access_token,
            bearer_auth_credentials=bearer_auth_credentials,
            square_version=square_version,
            additional_headers=additional_headers,
            user_agent_detail=user_agent_detail)

        additional_user_agent_parameters = { 
                'api-version': {'value': self.config.square_version, 'encode': False},
                'detail': {'value': self.config.user_agent_detail, 'encode': True}} 
        self.global_configuration = GlobalConfiguration(self.config)\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseApi.user_agent(), 
                        {** BaseApi.user_agent_parameters(), **additional_user_agent_parameters})\
            .additional_headers(self.config.additional_headers)\
            .global_header('Square-Version', self.config.square_version)

        self.auth_managers = {key: None for key in ['global']}
        self.auth_managers['global'] = OAuth2(
            self.config.bearer_auth_credentials)
        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

