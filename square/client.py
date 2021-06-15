# -*- coding: utf-8 -*-

from square.decorators import lazy_property
from square.configuration import Configuration
from square.api.mobile_authorization_api import MobileAuthorizationApi
from square.api.o_auth_api import OAuthApi
from square.api.v1_employees_api import V1EmployeesApi
from square.api.v1_transactions_api import V1TransactionsApi
from square.api.apple_pay_api import ApplePayApi
from square.api.bank_accounts_api import BankAccountsApi
from square.api.bookings_api import BookingsApi
from square.api.cards_api import CardsApi
from square.api.cash_drawers_api import CashDrawersApi
from square.api.catalog_api import CatalogApi
from square.api.customers_api import CustomersApi
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
from square.api.refunds_api import RefundsApi
from square.api.sites_api import SitesApi
from square.api.snippets_api import SnippetsApi
from square.api.subscriptions_api import SubscriptionsApi
from square.api.team_api import TeamApi
from square.api.terminal_api import TerminalApi


class Client(object):

    @staticmethod
    def sdk_version():
        return '12.0.0.20210616'

    @staticmethod
    def square_version():
        return '2021-06-16'

    @lazy_property
    def mobile_authorization(self):
        return MobileAuthorizationApi(self.config)

    @lazy_property
    def o_auth(self):
        return OAuthApi(self.config)

    @lazy_property
    def v1_employees(self):
        return V1EmployeesApi(self.config)

    @lazy_property
    def v1_transactions(self):
        return V1TransactionsApi(self.config)

    @lazy_property
    def apple_pay(self):
        return ApplePayApi(self.config)

    @lazy_property
    def bank_accounts(self):
        return BankAccountsApi(self.config)

    @lazy_property
    def bookings(self):
        return BookingsApi(self.config)

    @lazy_property
    def cards(self):
        return CardsApi(self.config)

    @lazy_property
    def cash_drawers(self):
        return CashDrawersApi(self.config)

    @lazy_property
    def catalog(self):
        return CatalogApi(self.config)

    @lazy_property
    def customers(self):
        return CustomersApi(self.config)

    @lazy_property
    def customer_groups(self):
        return CustomerGroupsApi(self.config)

    @lazy_property
    def customer_segments(self):
        return CustomerSegmentsApi(self.config)

    @lazy_property
    def devices(self):
        return DevicesApi(self.config)

    @lazy_property
    def disputes(self):
        return DisputesApi(self.config)

    @lazy_property
    def employees(self):
        return EmployeesApi(self.config)

    @lazy_property
    def gift_cards(self):
        return GiftCardsApi(self.config)

    @lazy_property
    def gift_card_activities(self):
        return GiftCardActivitiesApi(self.config)

    @lazy_property
    def inventory(self):
        return InventoryApi(self.config)

    @lazy_property
    def invoices(self):
        return InvoicesApi(self.config)

    @lazy_property
    def labor(self):
        return LaborApi(self.config)

    @lazy_property
    def locations(self):
        return LocationsApi(self.config)

    @lazy_property
    def checkout(self):
        return CheckoutApi(self.config)

    @lazy_property
    def transactions(self):
        return TransactionsApi(self.config)

    @lazy_property
    def loyalty(self):
        return LoyaltyApi(self.config)

    @lazy_property
    def merchants(self):
        return MerchantsApi(self.config)

    @lazy_property
    def orders(self):
        return OrdersApi(self.config)

    @lazy_property
    def payments(self):
        return PaymentsApi(self.config)

    @lazy_property
    def refunds(self):
        return RefundsApi(self.config)

    @lazy_property
    def sites(self):
        return SitesApi(self.config)

    @lazy_property
    def snippets(self):
        return SnippetsApi(self.config)

    @lazy_property
    def subscriptions(self):
        return SubscriptionsApi(self.config)

    @lazy_property
    def team(self):
        return TeamApi(self.config)

    @lazy_property
    def terminal(self):
        return TerminalApi(self.config)

    def __init__(self, timeout=60, max_retries=0, backoff_factor=2,
                 retry_statuses=[408, 413, 429, 500, 502, 503, 504, 521, 522, 524],
                 retry_methods=['GET', 'PUT'], environment='production',
                 custom_url='https://connect.squareup.com',
                 square_version='2021-06-16', access_token='TODO: Replace',
                 additional_headers={}, config=None):
        if config is None:
            self.config = Configuration(timeout=timeout,
                                        max_retries=max_retries,
                                        backoff_factor=backoff_factor,
                                        retry_statuses=retry_statuses,
                                        retry_methods=retry_methods,
                                        environment=environment,
                                        custom_url=custom_url,
                                        square_version=square_version,
                                        access_token=access_token,
                                        additional_headers=additional_headers)
        else:
            self.config = config
