# coding: utf-8

"""
    Selling Partner APIs for Fulfillment Outbound

    The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.

    The version of the OpenAPI document: 2020-07-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.invalid_return_item import InvalidReturnItem
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.return_authorization import ReturnAuthorization
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.return_item import ReturnItem
from typing import Optional, Set
from typing_extensions import Self

class CreateFulfillmentReturnResult(BaseModel):
    """
    The result for the createFulfillmentReturn operation.
    """ # noqa: E501
    return_items: Optional[List[ReturnItem]] = Field(default=None, description="An array of items that Amazon accepted for return. Returns empty if no items were accepted for return.", alias="returnItems")
    invalid_return_items: Optional[List[InvalidReturnItem]] = Field(default=None, description="An array of invalid return item information.", alias="invalidReturnItems")
    return_authorizations: Optional[List[ReturnAuthorization]] = Field(default=None, description="An array of return authorization information.", alias="returnAuthorizations")
    __properties: ClassVar[List[str]] = ["returnItems", "invalidReturnItems", "returnAuthorizations"]

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
        """Create an instance of CreateFulfillmentReturnResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in return_items (list)
        _items = []
        if self.return_items:
            for _item_return_items in self.return_items:
                if _item_return_items:
                    _items.append(_item_return_items.to_dict())
            _dict['returnItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in invalid_return_items (list)
        _items = []
        if self.invalid_return_items:
            for _item_invalid_return_items in self.invalid_return_items:
                if _item_invalid_return_items:
                    _items.append(_item_invalid_return_items.to_dict())
            _dict['invalidReturnItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in return_authorizations (list)
        _items = []
        if self.return_authorizations:
            for _item_return_authorizations in self.return_authorizations:
                if _item_return_authorizations:
                    _items.append(_item_return_authorizations.to_dict())
            _dict['returnAuthorizations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateFulfillmentReturnResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "returnItems": [ReturnItem.from_dict(_item) for _item in obj["returnItems"]] if obj.get("returnItems") is not None else None,
            "invalidReturnItems": [InvalidReturnItem.from_dict(_item) for _item in obj["invalidReturnItems"]] if obj.get("invalidReturnItems") is not None else None,
            "returnAuthorizations": [ReturnAuthorization.from_dict(_item) for _item in obj["returnAuthorizations"]] if obj.get("returnAuthorizations") is not None else None
        })
        return _obj


