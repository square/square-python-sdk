# -*- coding: utf-8 -*-

from apimatic_core.configurations.global_configuration import GlobalConfiguration
from apimatic_core.decorators.lazy_property import LazyProperty
from square.configuration import Configuration
from square.api.base_api import BaseApi
from square.http.auth.o_auth_2 import OAuth2
from square.api.mobile_authorization_api import MobileAuthorizationApi
from square.api.o_auth_api import OAuthApi
from square.api.v1_transactions_api import V1TransactionsApi
from square.api.apple_pay_api import ApplePayApi
from square.api.bank_accounts_api import BankAccountsApi
from square.api.bookings_api import BookingsApi
from square.api.booking_custom_attributes_api import BookingCustomAttributesApi
from square.api.cards_api import CardsApi
from square.api.cash_drawers_api import CashDrawersApi
from square.api.catalog_api import CatalogApi
from square.api.customers_api import CustomersApi
from square.api.customer_custom_attributes_api\
    import CustomerCustomAttributesApi
from square.api.customer_groups_api import CustomerGroupsApi
from square.api.customer_segments_api import CustomerSegmentsApi
from square.api.devices_api import DevicesApi
from square.api.disputes_api import DisputesApi
from square.api.employees_api import EmployeesApi
from square.api.gift_cards_api import GiftCardsApi
from square.api.gift_card_activities_api import GiftCardActivitiesApi
from square.api.inventory_api import InventoryApi
from square.api.invoices_api import InvoicesApi
from square.api.labor_api import LaborApi
from square.api.locations_api import LocationsApi
from square.api.location_custom_attributes_api\
    import LocationCustomAttributesApi
from square.api.checkout_api import CheckoutApi
from square.api.transactions_api import TransactionsApi
from square.api.loyalty_api import LoyaltyApi
from square.api.merchants_api import MerchantsApi
from square.api.merchant_custom_attributes_api\
    import MerchantCustomAttributesApi
from square.api.orders_api import OrdersApi
from square.api.order_custom_attributes_api import OrderCustomAttributesApi
from square.api.payments_api import PaymentsApi
from square.api.payouts_api import PayoutsApi
from square.api.refunds_api import RefundsApi
from square.api.sites_api import SitesApi
from square.api.snippets_api import SnippetsApi
from square.api.subscriptions_api import SubscriptionsApi
from square.api.team_api import TeamApi
from square.api.terminal_api import TerminalApi
from square.api.vendors_api import VendorsApi
from square.api.webhook_subscriptions_api import WebhookSubscriptionsApi


class Client(object):

    @staticmethod
    def sdk_version():
        return '33.1.0.20231213'

    @staticmethod
    def square_version():
        return '2023-12-13'

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
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'], environment='production',
                 custom_url='https://connect.squareup.com', access_token='',
                 square_version='2023-12-13', additional_headers={},
                 user_agent_detail='', config=None):
        if config is None:
            self.config = Configuration(
                                         http_client_instance=http_client_instance,
                                         override_http_client_configuration=override_http_client_configuration,
                                         http_call_back=http_call_back,
                                         timeout=timeout,
                                         max_retries=max_retries,
                                         backoff_factor=backoff_factor,
                                         retry_statuses=retry_statuses,
                                         retry_methods=retry_methods,
                                         environment=environment,
                                         custom_url=custom_url,
                                         access_token=access_token,
                                         square_version=square_version,
                                         additional_headers=additional_headers,
                                         user_agent_detail=user_agent_detail)
        else:
            self.config = config

        additional_user_agent_parameters = { 
                'api-version': {'value': self.config.square_version, 'encode': False},
                'detail': {'value': self.config.user_agent_detail, 'encode': True}} 
        self.global_configuration = GlobalConfiguration(self.config)\
            .base_uri_executor(self.config.get_base_uri)\
            .user_agent(BaseApi.user_agent(), 
                        {** BaseApi.user_agent_parameters(), **additional_user_agent_parameters})\
            .additional_headers(self.config.additional_headers)\
            .global_header('Square-Version', self.config.square_version)

        self.initialize_auth_managers(self.global_configuration)

        self.global_configuration = self.global_configuration.auth_managers(self.auth_managers)

    def initialize_auth_managers(self, global_config):
        http_client_config = global_config.get_http_client_configuration()
        self.auth_managers = { key: None for key in ['global']}
        self.auth_managers['global'] = OAuth2(http_client_config.access_token)
        return self.auth_managers
