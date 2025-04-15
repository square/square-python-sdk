# This file was auto-generated by Fern from our API Definition.

import typing_extensions
import typing_extensions
import typing


class CatalogInfoResponseLimitsParams(typing_extensions.TypedDict):
    batch_upsert_max_objects_per_batch: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of objects that may appear within a single batch in a
    `/v2/catalog/batch-upsert` request.
    """

    batch_upsert_max_total_objects: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of objects that may appear across all batches in a
    `/v2/catalog/batch-upsert` request.
    """

    batch_retrieve_max_object_ids: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of object IDs that may appear in a `/v2/catalog/batch-retrieve`
    request.
    """

    search_max_page_limit: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of results that may be returned in a page of a
    `/v2/catalog/search` response.
    """

    batch_delete_max_object_ids: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of object IDs that may be included in a single
    `/v2/catalog/batch-delete` request.
    """

    update_item_taxes_max_item_ids: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of item IDs that may be included in a single
    `/v2/catalog/update-item-taxes` request.
    """

    update_item_taxes_max_taxes_to_enable: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of tax IDs to be enabled that may be included in a single
    `/v2/catalog/update-item-taxes` request.
    """

    update_item_taxes_max_taxes_to_disable: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of tax IDs to be disabled that may be included in a single
    `/v2/catalog/update-item-taxes` request.
    """

    update_item_modifier_lists_max_item_ids: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of item IDs that may be included in a single
    `/v2/catalog/update-item-modifier-lists` request.
    """

    update_item_modifier_lists_max_modifier_lists_to_enable: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of modifier list IDs to be enabled that may be included in
    a single `/v2/catalog/update-item-modifier-lists` request.
    """

    update_item_modifier_lists_max_modifier_lists_to_disable: typing_extensions.NotRequired[typing.Optional[int]]
    """
    The maximum number of modifier list IDs to be disabled that may be included in
    a single `/v2/catalog/update-item-modifier-lists` request.
    """
