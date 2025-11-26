import uuid
import time
import pytest
from datetime import datetime, timedelta
from typing import Optional

from square.core.api_error import ApiError
from square.requests.catalog_item import CatalogItemParams
from square.requests.catalog_item_variation import CatalogItemVariationParams
from square.requests.catalog_object_item_variation import (
    CatalogObjectItemVariationParams,
)
from square.types.catalog_item import CatalogItem
from square.types.catalog_object_item import CatalogObjectItem
from square.types.inventory_adjustment import InventoryAdjustment
from square.types.inventory_physical_count import InventoryPhysicalCount

from . import helpers


def retry_on_rate_limit(func):
    """Decorator to retry functions on rate limit errors"""
    def wrapper(*args, **kwargs):
        max_retries = 5
        base_delay = 2  # seconds
        
        for attempt in range(max_retries):
            try:
                return func(*args, **kwargs)
            except ApiError as e:
                if e.status_code == 429 and attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)  # exponential backoff
                    print(f"Rate limited. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    continue
                raise
        return None
    return wrapper


@retry_on_rate_limit
def create_catalog_item_variation() -> str:
    client = helpers.test_client()

    variation_data: CatalogItemVariationParams = {
        "name": "Colombian Fair Trade",
        "track_inventory": True,
        "pricing_type": "FIXED_PRICING",
        "price_money": {"amount": 100, "currency": "USD"},
    }

    variation: CatalogObjectItemVariationParams = {
        "type": "ITEM_VARIATION",
        "id": "#colombian-coffee",
        "present_at_all_locations": True,
        "item_variation_data": variation_data,
    }

    item_data: CatalogItemParams = {
        "name": "Coffee",
        "description": "Strong coffee",
        "abbreviation": "C",
        "variations": [variation],
    }

    catalog_response = client.catalog.object.upsert(
        idempotency_key=str(uuid.uuid4()),
        object={
            "type": "ITEM",
            "id": "#single-item",
            "present_at_all_locations": True,
            "item_data": item_data,
        },
    )

    assert catalog_response.catalog_object is not None
    assert isinstance(catalog_response.catalog_object, CatalogObjectItem)
    item = catalog_response.catalog_object.item_data
    assert item is not None
    assert isinstance(item, CatalogItem)
    variations = item.variations
    assert variations is not None
    assert len(variations) > 0
    assert catalog_response.id_mappings is not None
    item_variation_ids = [
        mapping.object_id
        for mapping in catalog_response.id_mappings
        if mapping.object_id == variations[0].id
    ]
    assert len(item_variation_ids) > 0
    assert item_variation_ids[0] is not None
    return item_variation_ids[0]


@retry_on_rate_limit
@pytest.mark.skip(reason="Temporarily skipping create_initial_adjustment")
def create_initial_adjustment(item_variation_id: str) -> Optional[str]:
    """
    Create an initial inventory adjustment and return the physical count ID
    """
    client = helpers.test_client()
    response = client.inventory.batch_create_changes(
        idempotency_key=str(uuid.uuid4()),
        changes=[
            {
                "type": "ADJUSTMENT",
                "adjustment": {
                    "from_state": "NONE",
                    "to_state": "IN_STOCK",
                    "location_id": helpers.get_default_location_id(client),
                    "catalog_object_id": item_variation_id,
                    "quantity": "100",
                    "occurred_at": helpers.format_date_string(
                        datetime.now() - timedelta(hours=8)
                    ),
                },
            }
        ],
    )

    # Add delay after the first operation
    time.sleep(2)

    changes = response.changes
    assert changes is not None
    assert len(changes) > 0
    assert changes[0].adjustment is not None
    assert isinstance(changes[0].adjustment, InventoryAdjustment)
    adjustment_id = changes[0].adjustment.id
    assert adjustment_id is not None

    client.inventory.batch_create_changes(
        idempotency_key=str(uuid.uuid4()),
        changes=[
            {
                "type": "PHYSICAL_COUNT",
                "physical_count": {
                    "catalog_object_id": item_variation_id,
                    "location_id": helpers.get_default_location_id(client),
                    "quantity": "1",
                    "state": "IN_STOCK",
                    "occurred_at": helpers.format_date_string(datetime.now()),
                },
            }
        ],
    )

    # Add delay after the second operation
    time.sleep(2)

    physical_changes_response = client.inventory.batch_get_changes(
        types=["PHYSICAL_COUNT"],
        catalog_object_ids=[item_variation_id],
        location_ids=[helpers.get_default_location_id(client)],
    )
    physical_changes = physical_changes_response.items
    assert physical_changes is not None
    assert len(physical_changes) > 0
    physical_change = physical_changes[0]
    assert physical_change.physical_count is not None
    assert isinstance(physical_change.physical_count, InventoryPhysicalCount)
    assert physical_change.physical_count.id is not None
    return physical_change.physical_count.id


@pytest.mark.skip(reason="Temporarily skipping test_batch_change_inventory")
def test_batch_change_inventory():
    client = helpers.test_client()
    item_variation_id = create_catalog_item_variation()
    time.sleep(2)  # Add delay after catalog operation
    create_initial_adjustment(item_variation_id)
    time.sleep(2)  # Add delay after adjustment

    response = client.inventory.batch_create_changes(
        idempotency_key=str(uuid.uuid4()),
        changes=[
            {
                "type": "ADJUSTMENT",
                "adjustment": {
                    "from_state": "NONE",
                    "to_state": "IN_STOCK",
                    "location_id": helpers.get_default_location_id(client),
                    "catalog_object_id": item_variation_id,
                    "quantity": "50",
                    "occurred_at": helpers.format_date_string(datetime.now()),
                },
            }
        ],
    )

    assert response.changes is not None
    assert len(response.changes) > 0
    assert response.changes[0].adjustment is not None
    assert isinstance(response.changes[0].adjustment, InventoryAdjustment)
    assert "IN_STOCK" == response.changes[0].adjustment.to_state
    assert "50" == response.changes[0].adjustment.quantity


@pytest.mark.skip(reason="Temporarily skipping test_batch_retrieve_inventory_changes")
def test_batch_retrieve_inventory_changes():
    client = helpers.test_client()
    item_variation_id = create_catalog_item_variation()
    time.sleep(2)  # Add delay after catalog operation
    create_initial_adjustment(item_variation_id)
    time.sleep(2)  # Add delay after adjustment

    response = client.inventory.batch_get_changes(
        catalog_object_ids=[item_variation_id]
    )
    assert response.items is not None
    assert len(response.items) > 0


@pytest.mark.skip(reason="Temporarily skipping test_batch_retrieve_inventory_counts")
def test_batch_retrieve_inventory_counts():
    client = helpers.test_client()
    item_variation_id = create_catalog_item_variation()
    time.sleep(2)  # Add delay after catalog operation
    create_initial_adjustment(item_variation_id)
    time.sleep(2)  # Add delay after adjustment

    response = client.inventory.batch_get_counts(catalog_object_ids=[item_variation_id])
    assert response.items is not None
    assert len(response.items) > 0


@pytest.mark.skip(reason="Temporarily skipping test_retrieve_inventory_changes")
def test_retrieve_inventory_changes():
    client = helpers.test_client()
    item_variation_id = create_catalog_item_variation()
    time.sleep(2)  # Add delay after catalog operation
    create_initial_adjustment(item_variation_id)
    time.sleep(2)  # Add delay after adjustment

    response = client.inventory.get(catalog_object_id=item_variation_id)
    assert response.items is not None
    assert len(response.items) > 0


@pytest.mark.skip(reason="Temporarily skipping test_retrieve_inventory_counts")
def test_retrieve_inventory_counts():
    client = helpers.test_client()
    item_variation_id = create_catalog_item_variation()
    time.sleep(2)  # Add delay after catalog operation
    physical_count_id = create_initial_adjustment(item_variation_id)
    time.sleep(2)  # Add delay after adjustment

    response = client.inventory.get_physical_count(physical_count_id=physical_count_id)
    assert response.count is not None


@pytest.mark.skip(reason="Temporarily skipping test_retrieve_inventory_adjustments")
def test_retrieve_inventory_adjustments():
    client = helpers.test_client()
    item_variation_id = create_catalog_item_variation()
    time.sleep(2)  # Add delay after catalog operation
    create_initial_adjustment(item_variation_id)
    time.sleep(2)  # Add delay after adjustment

    response = client.inventory.batch_create_changes(
        idempotency_key=str(uuid.uuid4()),
        changes=[
            {
                "type": "ADJUSTMENT",
                "adjustment": {
                    "from_state": "NONE",
                    "to_state": "IN_STOCK",
                    "location_id": helpers.get_default_location_id(client),
                    "catalog_object_id": item_variation_id,
                    "quantity": "10",
                    "occurred_at": helpers.format_date_string(datetime.now()),
                },
            }
        ],
    )

    changes = response.changes
    assert changes is not None
    assert len(changes) > 0
    assert changes[0].adjustment is not None
    assert isinstance(changes[0].adjustment, InventoryAdjustment)
    assert changes[0].adjustment.id is not None
    adjustment_id = changes[0].adjustment.id
    
    time.sleep(2)  # Add delay before retrieve
    
    retrieve_response = client.inventory.get_adjustment(adjustment_id=adjustment_id)
    retrieve_adjustment = retrieve_response.adjustment
    assert retrieve_adjustment is not None
    assert isinstance(retrieve_adjustment, InventoryAdjustment)
    retrieve_adjustment_id = retrieve_adjustment.id
    assert retrieve_adjustment_id is not None

    assert retrieve_response.adjustment is not None
    assert adjustment_id == retrieve_adjustment_id