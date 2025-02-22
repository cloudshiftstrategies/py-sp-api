# coding: utf-8

"""
    Selling Partner API for Fulfillment Inbound

    The Selling Partner API for Fulfillment Inbound lets you create applications that create and update inbound shipments of inventory to Amazon's fulfillment network.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PrepOwner(str, Enum):
    """
    Indicates who will prepare the item.
    """

    """
    allowed enum values
    """
    AMAZON = 'AMAZON'
    SELLER = 'SELLER'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PrepOwner from a JSON string"""
        return cls(json.loads(json_str))


