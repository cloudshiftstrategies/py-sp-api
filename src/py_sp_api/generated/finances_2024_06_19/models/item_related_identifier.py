# coding: utf-8

"""
    The Selling Partner API for Finances

    The Selling Partner API for Finances provides financial information relevant to a seller's business. You can obtain financial events for a given order or date range without having to wait until a statement period closes.

    The version of the OpenAPI document: 2024-06-19
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ItemRelatedIdentifier(BaseModel):
    """
    Related business identifiers of the item.
    """ # noqa: E501
    item_related_identifier_name: Optional[StrictStr] = Field(default=None, description="Enumerated set of related item identifier names for the item.", alias="itemRelatedIdentifierName")
    item_related_identifier_value: Optional[StrictStr] = Field(default=None, description="Corresponding value to `ItemRelatedIdentifierName`.", alias="itemRelatedIdentifierValue")
    __properties: ClassVar[List[str]] = ["itemRelatedIdentifierName", "itemRelatedIdentifierValue"]

    @field_validator('item_related_identifier_name')
    def item_related_identifier_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ORDER_ADJUSTMENT_ITEM_ID', 'COUPON_ID', 'REMOVAL_SHIPMENT_ITEM_ID', 'TRANSACTION_ID']):
            raise ValueError("must be one of enum values ('ORDER_ADJUSTMENT_ITEM_ID', 'COUPON_ID', 'REMOVAL_SHIPMENT_ITEM_ID', 'TRANSACTION_ID')")
        return value

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
        """Create an instance of ItemRelatedIdentifier from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ItemRelatedIdentifier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemRelatedIdentifierName": obj.get("itemRelatedIdentifierName"),
            "itemRelatedIdentifierValue": obj.get("itemRelatedIdentifierValue")
        })
        return _obj


