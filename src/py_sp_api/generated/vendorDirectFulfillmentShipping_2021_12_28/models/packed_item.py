# coding: utf-8

"""
    Selling Partner API for Direct Fulfillment Shipping

    Use the Selling Partner API for Direct Fulfillment Shipping to access a direct fulfillment vendor's shipping data.

    The version of the OpenAPI document: 2021-12-28
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorDirectFulfillmentShipping_2021_12_28.models.item_quantity import ItemQuantity
from typing import Optional, Set
from typing_extensions import Self

class PackedItem(BaseModel):
    """
    An item that has been packed into a container for shipping.
    """ # noqa: E501
    item_sequence_number: StrictInt = Field(description="The sequence number of the item. The number must be the same as the order number of the item.", alias="itemSequenceNumber")
    buyer_product_identifier: Optional[StrictStr] = Field(default=None, description="The buyer's Amazon Standard Identification Number (ASIN) of an item. Either `buyerProductIdentifier` or `vendorProductIdentifier` is required.", alias="buyerProductIdentifier")
    piece_number: Optional[StrictInt] = Field(default=None, description="The piece number of the item in this container. This is required when the item is split across different containers.", alias="pieceNumber")
    vendor_product_identifier: Optional[StrictStr] = Field(default=None, description="An item's product identifier, which the vendor selects. This identifier should be the same as the identifier, such as a SKU, in the purchase order.", alias="vendorProductIdentifier")
    packed_quantity: ItemQuantity = Field(alias="packedQuantity")
    __properties: ClassVar[List[str]] = ["itemSequenceNumber", "buyerProductIdentifier", "pieceNumber", "vendorProductIdentifier", "packedQuantity"]

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
        """Create an instance of PackedItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of packed_quantity
        if self.packed_quantity:
            _dict['packedQuantity'] = self.packed_quantity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PackedItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemSequenceNumber": obj.get("itemSequenceNumber"),
            "buyerProductIdentifier": obj.get("buyerProductIdentifier"),
            "pieceNumber": obj.get("pieceNumber"),
            "vendorProductIdentifier": obj.get("vendorProductIdentifier"),
            "packedQuantity": ItemQuantity.from_dict(obj["packedQuantity"]) if obj.get("packedQuantity") is not None else None
        })
        return _obj


