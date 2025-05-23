# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.unchecked_base_model import UncheckedBaseModel
from .catalog_category import CatalogCategory
from .catalog_object_category import CatalogObjectCategory
import typing
import pydantic
from .catalog_item_modifier_list_info import CatalogItemModifierListInfo
from .catalog_item_product_type import CatalogItemProductType
from .catalog_item_option_for_item import CatalogItemOptionForItem
from .catalog_ecom_seo_data import CatalogEcomSeoData
from .catalog_item_food_and_beverage_details import CatalogItemFoodAndBeverageDetails
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class CatalogItem(UncheckedBaseModel):
    """
    A [CatalogObject](entity:CatalogObject) instance of the `ITEM` type, also referred to as an item, in the catalog.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item's name. This is a searchable attribute for use in applicable query filters, its value must not be empty, and the length is of Unicode code points.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item's description. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points.
    
    Deprecated at 2022-07-20, this field is planned to retire in 6 months. You should migrate to use `description_html` to set the description
    of the [CatalogItem](entity:CatalogItem) instance.  The `description` and `description_html` field values are kept in sync. If you try to
    set the both fields, the `description_html` text value overwrites the `description` value. Updates in one field are also reflected in the other,
    except for when you use an early version before Square API 2022-07-20 and `description_html` is set to blank, setting the `description` value to null
    does not nullify `description_html`.
    """

    abbreviation: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the item's display label in the Square Point of Sale app. Only up to the first five characters of the string are used.
    This attribute is searchable, and its value length is of Unicode code points.
    """

    label_color: typing.Optional[str] = pydantic.Field(default=None)
    """
    The color of the item's display label in the Square Point of Sale app. This must be a valid hex color code.
    """

    is_taxable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the item is taxable (`true`) or non-taxable (`false`). Default is `true`.
    """

    category_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the item's category, if any. Deprecated since 2023-12-13. Use `CatalogItem.categories`, instead.
    """

    tax_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A set of IDs indicating the taxes enabled for
    this item. When updating an item, any taxes listed here will be added to the item.
    Taxes may also be added to or deleted from an item using `UpdateItemTaxes`.
    """

    modifier_list_info: typing.Optional[typing.List[CatalogItemModifierListInfo]] = pydantic.Field(default=None)
    """
    A set of `CatalogItemModifierListInfo` objects
    representing the modifier lists that apply to this item, along with the overrides and min
    and max limits that are specific to this item. Modifier lists
    may also be added to or deleted from an item using `UpdateItemModifierLists`.
    """

    variations: typing.Optional[typing.List["CatalogObject"]] = pydantic.Field(default=None)
    """
    A list of [CatalogItemVariation](entity:CatalogItemVariation) objects for this item. An item must have
    at least one variation.
    """

    product_type: typing.Optional[CatalogItemProductType] = pydantic.Field(default=None)
    """
    The product type of the item. Once set, the `product_type` value cannot be modified.
    
    Items of the `LEGACY_SQUARE_ONLINE_SERVICE` and `LEGACY_SQUARE_ONLINE_MEMBERSHIP` product types can be updated
    but cannot be created using the API.
    See [CatalogItemProductType](#type-catalogitemproducttype) for possible values
    """

    skip_modifier_screen: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If `false`, the Square Point of Sale app will present the `CatalogItem`'s
    details screen immediately, allowing the merchant to choose `CatalogModifier`s
    before adding the item to the cart.  This is the default behavior.
    
    If `true`, the Square Point of Sale app will immediately add the item to the cart with the pre-selected
    modifiers, and merchants can edit modifiers by drilling down onto the item's details.
    
    Third-party clients are encouraged to implement similar behaviors.
    """

    item_options: typing.Optional[typing.List[CatalogItemOptionForItem]] = pydantic.Field(default=None)
    """
    List of item options IDs for this item. Used to manage and group item
    variations in a specified order.
    
    Maximum: 6 item options.
    """

    ecom_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated. A URI pointing to a published e-commerce product page for the Item.
    """

    ecom_image_uris: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Deprecated. A comma-separated list of encoded URIs pointing to a set of published e-commerce images for the Item.
    """

    image_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of images associated with this `CatalogItem` instance.
    These images will be shown to customers in Square Online Store.
    The first image will show up as the icon for this item in POS.
    """

    sort_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A name to sort the item by. If this name is unspecified, namely, the `sort_name` field is absent, the regular `name` field is used for sorting.
    Its value must not be empty.
    
    It is currently supported for sellers of the Japanese locale only.
    """

    categories: typing.Optional[typing.List[CatalogObjectCategory]] = pydantic.Field(default=None)
    """
    The list of categories.
    """

    description_html: typing.Optional[str] = pydantic.Field(default=None)
    """
    The item's description as expressed in valid HTML elements. The length of this field value, including those of HTML tags,
    is of Unicode points. With application query filters, the text values of the HTML elements and attributes are searchable. Invalid or
    unsupported HTML elements or attributes are ignored.
    
    Supported HTML elements include:
    - `a`: Link. Supports linking to website URLs, email address, and telephone numbers.
    - `b`, `strong`:  Bold text
    - `br`: Line break
    - `code`: Computer code
    - `div`: Section
    - `h1-h6`: Headings
    - `i`, `em`: Italics
    - `li`: List element
    - `ol`: Numbered list
    - `p`: Paragraph
    - `ul`: Bullet list
    - `u`: Underline
    
    
    Supported HTML attributes include:
    - `align`: Alignment of the text content
    - `href`: Link destination
    - `rel`: Relationship between link's target and source
    - `target`: Place to open the linked document
    """

    description_plaintext: typing.Optional[str] = pydantic.Field(default=None)
    """
    A server-generated plaintext version of the `description_html` field, without formatting tags.
    """

    channels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of IDs representing channels, such as a Square Online site, where the item can be made visible or available.
    This field is read only and cannot be edited.
    """

    is_archived: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether this item is archived (`true`) or not (`false`).
    """

    ecom_seo_data: typing.Optional[CatalogEcomSeoData] = pydantic.Field(default=None)
    """
    The SEO data for a seller's Square Online store.
    """

    food_and_beverage_details: typing.Optional[CatalogItemFoodAndBeverageDetails] = pydantic.Field(default=None)
    """
    The food and beverage-specific details for the `FOOD_AND_BEV` item.
    """

    reporting_category: typing.Optional[CatalogObjectCategory] = pydantic.Field(default=None)
    """
    The item's reporting category.
    """

    is_alcoholic: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether this item is alcoholic (`true`) or not (`false`).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .catalog_item_option import CatalogItemOption  # noqa: E402
from .catalog_modifier_list import CatalogModifierList  # noqa: E402
from .catalog_object_item import CatalogObjectItem  # noqa: E402
from .catalog_object_item_option import CatalogObjectItemOption  # noqa: E402
from .catalog_object_modifier_list import CatalogObjectModifierList  # noqa: E402
from .catalog_object_subscription_plan import CatalogObjectSubscriptionPlan  # noqa: E402
from .catalog_subscription_plan import CatalogSubscriptionPlan  # noqa: E402
from .catalog_object import CatalogObject  # noqa: E402

update_forward_refs(CatalogItem)
