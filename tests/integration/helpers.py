import os
import uuid
from datetime import datetime
from typing import List

from square import Square
from square.core import File
from square.environment import SquareEnvironment
from square.types.address import Address
from square.types.catalog_item import CatalogItem
from square.types.catalog_item_variation import CatalogItemVariation
from square.types.catalog_object import (
    CatalogObject,
    CatalogObject_Item,
    CatalogObject_ItemVariation,
)
from square.types.location import Location
from square.types.money import Money


class CreateCatalogItemVariationOptions:
    name: str
    price_money: Money

    def __init__(self):
        self.name = "Variation " + str(uuid.uuid4())
        self.price_money = new_test_money(1000)

    def variation(self) -> CatalogItemVariation:
        return CatalogItemVariation(
            name=self.name,
            track_inventory=True,
            pricing_type="FIXED_PRICING",
            price_money=self.price_money,
        )


class CreateCatalogItemOptions:
    name: str
    description: str
    abbreviation: str
    variation_opts: List[CreateCatalogItemVariationOptions]

    def __init__(self):
        self.name = "Item " + str(uuid.uuid4())
        self.description = "Test item description"
        self.abbreviation = "TST"
        self.variation_opts = [CreateCatalogItemVariationOptions()]

    def variations(self) -> List[CatalogObject]:
        return [
            CatalogObject_ItemVariation(
                type="ITEM_VARIATION",
                id="#variation" + str(uuid.uuid4()),
                present_at_all_locations=True,
                item_variation_data=opts.variation(),
            )
            for opts in self.variation_opts
        ]


def test_client() -> Square:
    return Square(
        token=os.getenv("TEST_SQUARE_TOKEN"),
        environment=SquareEnvironment.SANDBOX,
    )


def new_test_money(amount: int) -> Money:
    return Money(amount=amount, currency="USD")


def create_test_catalog_item(opts: CreateCatalogItemOptions) -> CatalogObject:
    return CatalogObject_Item(
        type="ITEM",
        id="#" + str(uuid.uuid4()),
        present_at_all_locations=True,
        item_data=CatalogItem(
            name=opts.name,
            description=opts.description,
            abbreviation=opts.abbreviation,
            variations=opts.variations(),
        ),
    )


def get_test_file() -> File:
    with open("tests/integration/testdata/image.jpeg", "rb") as file:
        return file.read()


def create_location(client: Square) -> str:
    locations_response = client.locations.create(
        location={"name": "Test location " + str(uuid.uuid4())}
    )

    location = locations_response.location
    if location is None or not isinstance(location, Location):
        raise Exception("Could not get location.")
    location_id = location.id
    if location_id is None:
        raise Exception("Could not get location ID.")
    return location_id


def create_test_customer(client: Square) -> str:
    address = test_address()
    response = client.customers.create(
        idempotency_key=str(uuid.uuid4()),
        given_name="Amelia",
        family_name="Earhart",
        phone_number="1-212-555-4240",
        note="test customer",
        address={
            "address_line1": address.address_line1,
            "address_line2": address.address_line2,
            "locality": address.locality,
            "administrative_district_level1": address.administrative_district_level1,
            "postal_code": address.postal_code,
            "country": address.country,
        },
    )
    customer = response.customer
    if customer is None:
        raise Exception("Could not get customer.")
    customer_id = customer.id
    if customer_id is None:
        raise Exception("Could not get customer ID.")
    return customer_id


def test_address() -> Address:
    return Address(
        address_line1="500 Electric Ave",
        address_line2="Suite 600A",
        locality="New York",
        administrative_district_level1="NY",
        postal_code="10003",
        country="US",
    )


def get_default_location_id(client: Square) -> str:
    response = client.locations.list()
    locations = response.locations
    if locations is None or len(locations) == 0:
        raise Exception("Could not get locations.")
    location_id = locations[0].id
    if location_id is None:
        raise Exception("Could not get location ID.")
    return location_id


def new_test_square_id() -> str:
    return "#" + str(uuid.uuid4())


def format_date_string(date: datetime) -> str:
    return date.isoformat()[:19] + "Z"
