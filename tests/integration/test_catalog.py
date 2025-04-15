import time
import uuid

from square.core.request_options import RequestOptions
from square.types.catalog_item import CatalogItem
from square.types.catalog_item_variation import CatalogItemVariation
from square.types.catalog_modifier import CatalogModifier
from square.types.catalog_modifier_list import CatalogModifierList
from square.types.catalog_object_batch import CatalogObjectBatch
from square.types.catalog_object_item import CatalogObjectItem
from square.types.catalog_object_modifier import CatalogObjectModifier
from square.types.catalog_object_modifier_list import CatalogObjectModifierList
from square.types.catalog_object_tax import CatalogObjectTax
from square.types.catalog_tax import CatalogTax

from . import helpers

MAX_RETRIES = 5
MAX_TIMEOUT = 120


def test_upload_catalog_image():
    # Wait to kick off the first test to avoid being rate limited.
    time.sleep(3)

    client = helpers.test_client()

    # Setup: Create a catalog object to associate the image with
    catalog_object = helpers.create_test_catalog_item(
        helpers.CreateCatalogItemOptions()
    )
    create_catalog_resp = client.catalog.batch_upsert(
        idempotency_key=str(uuid.uuid4()),
        batches=[CatalogObjectBatch(objects=[catalog_object])],
    )

    objects = create_catalog_resp.objects
    assert objects is not None
    assert 1 == len(objects)
    created_catalog_object = objects[0]
    assert isinstance(created_catalog_object, CatalogObjectItem)
    assert created_catalog_object.id is not None

    # Create a new catalog image
    image_name = "Test Image " + str(uuid.uuid4())
    create_catalog_image_resp = client.catalog.images.create(
        image_file=helpers.get_test_file(),
        request={
            "idempotency_key": str(uuid.uuid4()),
            "image": {
                "type": "IMAGE",
                "id": helpers.new_test_square_id(),
                "image_data": {"name": image_name},
            },
            "object_id": created_catalog_object.id,
        },
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )
    image = create_catalog_image_resp.image
    assert image is not None
    assert isinstance(image, CatalogObjectItem)

    # Cleanup
    client.catalog.batch_delete(
        object_ids=[created_catalog_object.id, image.id],
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )


def test_upsert_catalog_object():
    client = helpers.test_client()

    coffee_variation_opts = helpers.CreateCatalogItemVariationOptions()
    coffee_variation_opts.price_money = helpers.new_test_money(100)
    coffee_variation_opts.name = "Colombian Fair Trade"

    coffee_opts = helpers.CreateCatalogItemOptions()
    coffee_opts.name = "Coffee"
    coffee_opts.description = "Strong coffee"
    coffee_opts.abbreviation = "C"
    coffee_opts.variation_opts = [coffee_variation_opts]

    coffee = helpers.create_test_catalog_item(coffee_opts)

    response = client.catalog.object.upsert(
        idempotency_key=str(uuid.uuid4()),
        object=coffee,
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )

    catalog_object = response.catalog_object
    assert catalog_object is not None
    assert isinstance(catalog_object, CatalogObjectItem)
    item = catalog_object.item_data
    assert item is not None
    assert isinstance(item, CatalogItem)
    variations = item.variations
    assert variations is not None
    assert 1 == len(variations)

    variation_object = variations[0]
    item_variation_data = variation_object.item_variation_data
    assert item_variation_data is not None
    assert isinstance(item_variation_data, CatalogItemVariation)
    assert "Colombian Fair Trade" == item_variation_data.name


def test_catalog_info():
    client = helpers.test_client()
    response = client.catalog.search(
        limit=1, request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT)
    )

    assert response.objects is not None
    assert len(response.objects) > 0


def test_search_catalog_items():
    client = helpers.test_client()
    response = client.catalog.search_items(
        limit=1, request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT)
    )
    assert response is not None


def test_batch_upsert_catalog_objects():
    # Wait to kick off this test to avoid being rate limited.
    time.sleep(3)

    client = helpers.test_client()

    modifier = CatalogObjectModifier(
        type="MODIFIER",
        id="#temp-modifier-id",
        modifier_data=CatalogModifier(
            name="Limited Time Only Price", price_money=helpers.new_test_money(200)
        ),
    )

    modifier_list = CatalogObjectModifierList(
        type="MODIFIER_LIST",
        id="#temp-modifier-list-id",
        modifier_list_data=CatalogModifierList(
            name="Special weekend deals", modifiers=[modifier]
        ),
    )

    tax = CatalogObjectTax(
        type="TAX",
        id="#temp-tax-id",
        tax_data=CatalogTax(
            name="Online only Tax",
            calculation_phase="TAX_SUBTOTAL_PHASE",
            inclusion_type="ADDITIVE",
            percentage="5.0",
            applies_to_custom_amounts=True,
            enabled=True,
        ),
    )

    response = client.catalog.batch_upsert(
        idempotency_key=str(uuid.uuid4()),
        batches=[
            {
                "objects": [
                    {
                        "type": tax.type,
                        "id": tax.id,
                        "tax_data": {
                            "name": tax.tax_data.name,
                            "calculation_phase": tax.tax_data.calculation_phase,
                            "inclusion_type": tax.tax_data.inclusion_type,
                            "percentage": tax.tax_data.percentage,
                            "applies_to_custom_amounts": tax.tax_data.applies_to_custom_amounts,
                            "enabled": tax.tax_data.enabled,
                        },
                    },
                    {
                        "type": modifier_list.type,
                        "id": modifier_list.id,
                        "modifier_list_data": {
                            "name": modifier_list.modifier_list_data.name,
                            "modifiers": [modifier],
                        },
                    },
                ]
            }
        ],
    )

    objects = response.objects
    assert objects is not None
    assert 2 == len(objects)

    id_mappings = response.id_mappings
    assert id_mappings is not None

    catalog_tax_ids = [
        mapping.object_id
        for mapping in id_mappings
        if mapping.client_object_id == "#temp-tax-id"
    ]
    assert len(catalog_tax_ids) > 0
    catalog_tax_id = catalog_tax_ids[0]

    catalog_modifier_ids = [
        mapping.object_id
        for mapping in id_mappings
        if mapping.client_object_id == "#temp-modifier-id"
    ]
    assert len(catalog_modifier_ids) > 0
    catalog_modifier_id = catalog_modifier_ids[0]

    catalog_modifier_list_ids = [
        mapping.object_id
        for mapping in id_mappings
        if mapping.client_object_id == "#temp-modifier-list-id"
    ]
    assert len(catalog_modifier_list_ids) > 0
    catalog_modifier_list_id = catalog_modifier_list_ids[0]

    response = client.catalog.batch_get(
        object_ids=[catalog_modifier_id, catalog_modifier_list_id, catalog_tax_id],
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )

    assert response.objects is not None
    assert 3 == len(response.objects)
    resp_objects = response.objects
    resp_object_ids = [obj.id for obj in resp_objects if obj.id is not None]
    assert set(resp_object_ids) == {
        catalog_modifier_id,
        catalog_modifier_list_id,
        catalog_tax_id,
    }

    catalog_item = helpers.create_test_catalog_item(helpers.CreateCatalogItemOptions())
    catalog_response = client.catalog.object.upsert(
        idempotency_key=str(uuid.uuid4()), object=catalog_item
    )
    catalog_object = catalog_response.catalog_object
    assert catalog_object is not None
    assert isinstance(catalog_object, CatalogObjectItem)
    catalog_object_id = catalog_object.id

    response = client.catalog.update_item_taxes(
        item_ids=[catalog_object_id],
        taxes_to_enable=[catalog_tax_id],
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )

    assert response.updated_at is not None
    assert response.errors is None

    response = client.catalog.update_item_modifier_lists(
        item_ids=[catalog_object_id],
        modifier_lists_to_enable=[catalog_modifier_list_id],
        request_options=RequestOptions(timeout_in_seconds=MAX_TIMEOUT),
    )

    assert response.updated_at is not None
    assert response.errors is None


def test_delete_catalog_object():
    client = helpers.test_client()

    catalog_item = helpers.create_test_catalog_item(helpers.CreateCatalogItemOptions())
    catalog_response = client.catalog.object.upsert(
        idempotency_key=str(uuid.uuid4()), object=catalog_item
    )
    catalog_object = catalog_response.catalog_object
    assert catalog_object is not None
    assert isinstance(catalog_object, CatalogObjectItem)
    catalog_object_id = catalog_object.id

    response = client.catalog.object.delete(object_id=catalog_object_id)

    assert response is not None
