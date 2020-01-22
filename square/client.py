# -*- coding: utf-8 -*-

from square.decorators import lazy_property
from square.configuration import Configuration
from square.api.mobile_authorization_api import MobileAuthorizationApi
from square.api.o_auth_api import OAuthApi
from square.api.v1_locations_api import V1LocationsApi
from square.api.v1_employees_api import V1EmployeesApi
from square.api.v1_transactions_api import V1TransactionsApi
from square.api.v1_items_api import V1ItemsApi
from square.api.apple_pay_api import ApplePayApi
from square.api.cash_drawers_api import CashDrawersApi
from square.api.catalog_api import CatalogApi
from square.api.customers_api import CustomersApi
from square.api.employees_api import EmployeesApi
from square.api.inventory_api import InventoryApi
from square.api.labor_api import LaborApi
from square.api.locations_api import LocationsApi
from square.api.reporting_api import ReportingApi
from square.api.checkout_api import CheckoutApi
from square.api.orders_api import OrdersApi
from square.api.transactions_api import TransactionsApi
from square.api.merchants_api import MerchantsApi
from square.api.payments_api import PaymentsApi
from square.api.refunds_api import RefundsApi


class Client(object):

    @staticmethod
    def sdk_version():
        return '4.1.0.20200122'

    @staticmethod
    def square_version():
        return '2020-01-22'

    @lazy_property
    def mobile_authorization(self):
        return MobileAuthorizationApi(self.config)

    @lazy_property
    def o_auth(self):
        return OAuthApi(self.config)

    @lazy_property
    def v1_locations(self):
        return V1LocationsApi(self.config)

    @lazy_property
    def v1_employees(self):
        return V1EmployeesApi(self.config)

    @lazy_property
    def v1_transactions(self):
        return V1TransactionsApi(self.config)

    @lazy_property
    def v1_items(self):
        return V1ItemsApi(self.config)

    @lazy_property
    def apple_pay(self):
        return ApplePayApi(self.config)

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
    def employees(self):
        return EmployeesApi(self.config)

    @lazy_property
    def inventory(self):
        return InventoryApi(self.config)

    @lazy_property
    def labor(self):
        return LaborApi(self.config)

    @lazy_property
    def locations(self):
        return LocationsApi(self.config)

    @lazy_property
    def reporting(self):
        return ReportingApi(self.config)

    @lazy_property
    def checkout(self):
        return CheckoutApi(self.config)

    @lazy_property
    def orders(self):
        return OrdersApi(self.config)

    @lazy_property
    def transactions(self):
        return TransactionsApi(self.config)

    @lazy_property
    def merchants(self):
        return MerchantsApi(self.config)

    @lazy_property
    def payments(self):
        return PaymentsApi(self.config)

    @lazy_property
    def refunds(self):
        return RefundsApi(self.config)

    def __init__(self, timeout=60, max_retries=3, backoff_factor=0,
                 environment='production', access_token='TODO: Replace',
                 additional_headers={}, config=None):
        if config is None:
            self.config = Configuration(timeout=timeout,
                                        max_retries=max_retries,
                                        backoff_factor=backoff_factor,
                                        environment=environment,
                                        access_token=access_token,
                                        additional_headers=additional_headers)
        else:
            self.config = config
