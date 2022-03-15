# -*- coding: utf-8 -*-

import json
import dateutil.parser

from tests.api.api_test_base import ApiTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from square.api_helper import APIHelper
from square.api.catalog_api import CatalogApi


class CatalogApiTests(ApiTestBase):

    @classmethod
    def setUpClass(cls):
        super(CatalogApiTests, cls).setUpClass()
        cls.controller = cls.client.catalog
        cls.response_catcher = cls.controller.http_call_back

    # Returns information about the Square Catalog API, such as batch size
    #limits for `BatchUpsertCatalogObjects`.
    def test_test_catalog_info(self):

        # Perform the API call through the SDK function
        result = self.controller.catalog_info()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Returns a list of [CatalogObject](#type-catalogobject)s that includes
    #all objects of a set of desired types (for example, all [CatalogItem](#type-catalogitem)
    #and [CatalogTax](#type-catalogtax) objects) in the catalog. The `types` parameter
    #is specified as a comma-separated list of valid [CatalogObject](#type-catalogobject) types:
    #`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`.
    #
    #__Important:__ ListCatalog does not return deleted catalog items. To retrieve
    #deleted catalog items, use SearchCatalogObjects and set `include_deleted_objects`
    #to `true`.
    def test_test_list_catalog(self):
        # Parameters for the API call
        cursor = None
        types = None

        # Perform the API call through the SDK function
        result = self.controller.list_catalog(cursor, types)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


