# coding: utf-8

"""
    Selling Partner API for FBA Inventory

    The Selling Partner API for FBA Inventory lets you programmatically retrieve information about inventory in Amazon's fulfillment network.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.fbaInventory.models.inventory_item import InventoryItem
from typing import Optional, Set
from typing_extensions import Self

class AddInventoryRequest(BaseModel):
    """
    The object with the list of Inventory to be added
    """ # noqa: E501
    inventory_items: Optional[List[InventoryItem]] = Field(default=None, description="List of Inventory to be added", alias="inventoryItems")
    __properties: ClassVar[List[str]] = ["inventoryItems"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AddInventoryRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in inventory_items (list)
        _items = []
        if self.inventory_items:
            for _item_inventory_items in self.inventory_items:
                if _item_inventory_items:
                    _items.append(_item_inventory_items.to_dict())
            _dict['inventoryItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AddInventoryRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "inventoryItems": [InventoryItem.from_dict(_item) for _item in obj["inventoryItems"]] if obj.get("inventoryItems") is not None else None
        })
        return _obj


