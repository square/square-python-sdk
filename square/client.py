# -*- coding: utf-8 -*-

from square.decorators import lazy_property
from square.configuration import Configuration
from square.http.auth.o_auth_2 import OAuth2
from square.api.mobile_authorization_api import MobileAuthorizationApi
from square.api.o_auth_api import OAuthApi
from square.api.v1_transactions_api import V1TransactionsApi
from square.api.apple_pay_api import ApplePayApi
from square.api.bank_accounts_api import BankAccountsApi
from square.api.bookings_api import BookingsApi
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
from square.api.checkout_api import CheckoutApi
from square.api.transactions_api import TransactionsApi
from square.api.loyalty_api import LoyaltyApi
from square.api.merchants_api import MerchantsApi
from square.api.orders_api import OrdersApi
from square.api.payments_api import PaymentsApi
from square.api.payouts_api import PayoutsApi
from square.api.refunds_api import RefundsApi
from square.api.sites_api import SitesApi
from square.api.snippets_api import SnippetsApi
from square.api.subscriptions_api import SubscriptionsApi
from square.api.team_api import TeamApi
from square.api.terminal_api import TerminalApi
from square.api.vendors_api import VendorsApi


class Client(object):

    @staticmethod
    def sdk_version():
        return '20.1.0.20220720'

    @staticmethod
    def square_version():
        return '2022-07-20'

    def user_agent_detail(self):
        return self.config.user_agent_detail

    @lazy_property
    def mobile_authorization(self):
        return MobileAuthorizationApi(self.config, self.auth_managers)

    @lazy_property
    def o_auth(self):
        return OAuthApi(self.config, self.auth_managers)

    @lazy_property
    def v1_transactions(self):
        return V1TransactionsApi(self.config, self.auth_managers)

    @lazy_property
    def apple_pay(self):
        return ApplePayApi(self.config, self.auth_managers)

    @lazy_property
    def bank_accounts(self):
        return BankAccountsApi(self.config, self.auth_managers)

    @lazy_property
    def bookings(self):
        return BookingsApi(self.config, self.auth_managers)

    @lazy_property
    def cards(self):
        return CardsApi(self.config, self.auth_managers)

    @lazy_property
    def cash_drawers(self):
        return CashDrawersApi(self.config, self.auth_managers)

    @lazy_property
    def catalog(self):
        return CatalogApi(self.config, self.auth_managers)

    @lazy_property
    def customers(self):
        return CustomersApi(self.config, self.auth_managers)

    @lazy_property
    def customer_custom_attributes(self):
        return CustomerCustomAttributesApi(self.config, self.auth_managers)

    @lazy_property
    def customer_groups(self):
        return CustomerGroupsApi(self.config, self.auth_managers)

    @lazy_property
    def customer_segments(self):
        return CustomerSegmentsApi(self.config, self.auth_managers)

    @lazy_property
    def devices(self):
        return DevicesApi(self.config, self.auth_managers)

    @lazy_property
    def disputes(self):
        return DisputesApi(self.config, self.auth_managers)

    @lazy_property
    def employees(self):
        return EmployeesApi(self.config, self.auth_managers)

    @lazy_property
    def gift_cards(self):
        return GiftCardsApi(self.config, self.auth_managers)

    @lazy_property
    def gift_card_activities(self):
        return GiftCardActivitiesApi(self.config, self.auth_managers)

    @lazy_property
    def inventory(self):
        return InventoryApi(self.config, self.auth_managers)

    @lazy_property
    def invoices(self):
        return InvoicesApi(self.config, self.auth_managers)

    @lazy_property
    def labor(self):
        return LaborApi(self.config, self.auth_managers)

    @lazy_property
    def locations(self):
        return LocationsApi(self.config, self.auth_managers)

    @lazy_property
    def checkout(self):
        return CheckoutApi(self.config, self.auth_managers)

    @lazy_property
    def transactions(self):
        return TransactionsApi(self.config, self.auth_managers)

    @lazy_property
    def loyalty(self):
        return LoyaltyApi(self.config, self.auth_managers)

    @lazy_property
    def merchants(self):
        return MerchantsApi(self.config, self.auth_managers)

    @lazy_property
    def orders(self):
        return OrdersApi(self.config, self.auth_managers)

    @lazy_property
    def payments(self):
        return PaymentsApi(self.config, self.auth_managers)

    @lazy_property
    def payouts(self):
        return PayoutsApi(self.config, self.auth_managers)

    @lazy_property
    def refunds(self):
        return RefundsApi(self.config, self.auth_managers)

    @lazy_property
    def sites(self):
        return SitesApi(self.config, self.auth_managers)

    @lazy_property
    def snippets(self):
        return SnippetsApi(self.config, self.auth_managers)

    @lazy_property
    def subscriptions(self):
        return SubscriptionsApi(self.config, self.auth_managers)

    @lazy_property
    def team(self):
        return TeamApi(self.config, self.auth_managers)

    @lazy_property
    def terminal(self):
        return TerminalApi(self.config, self.auth_managers)

    @lazy_property
    def vendors(self):
        return VendorsApi(self.config, self.auth_managers)

    def __init__(self, http_client_instance=None,
                 override_http_client_configuration=False, http_call_back=None,
                 timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'], environment='production',
                 custom_url='https://connect.squareup.com', access_token='',
                 square_version='2022-07-20', additional_headers={},
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
        self.initialize_auth_managers(self.config)

    def initialize_auth_managers(self, config):
        self.auth_managers = { key: None for key in ['global']}
        self.auth_managers['global'] = OAuth2(config.access_token)
        return self.auth_managers
