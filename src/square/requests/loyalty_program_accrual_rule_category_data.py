# This file was auto-generated by Fern from our API Definition.

import typing_extensions


class LoyaltyProgramAccrualRuleCategoryDataParams(typing_extensions.TypedDict):
    """
    Represents additional data for rules with the `CATEGORY` accrual type.
    """

    category_id: str
    """
    The ID of the `CATEGORY` [catalog object](entity:CatalogObject) that buyers can purchase to earn
    points.
    """
