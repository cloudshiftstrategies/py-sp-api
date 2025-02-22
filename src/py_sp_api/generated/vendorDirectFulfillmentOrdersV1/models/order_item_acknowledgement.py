# coding: utf-8

"""
    Selling Partner API for Direct Fulfillment Orders

    The Selling Partner API for Direct Fulfillment Orders provides programmatic access to a direct fulfillment vendor's order data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorDirectFulfillmentOrdersV1.models.item_quantity import ItemQuantity
from typing import Optional, Set
from typing_extensions import Self

class OrderItemAcknowledgement(BaseModel):
    """
    Details of an individual item within the order being acknowledged.
    """ # noqa: E501
    item_sequence_number: StrictStr = Field(description="Line item sequence number for the item.", alias="itemSequenceNumber")
    buyer_product_identifier: Optional[StrictStr] = Field(default=None, description="Buyer's standard identification number (ASIN) of an item.", alias="buyerProductIdentifier")
    vendor_product_identifier: Optional[StrictStr] = Field(default=None, description="The vendor selected product identification of the item. Should be the same as was provided in the purchase order.", alias="vendorProductIdentifier")
    acknowledged_quantity: ItemQuantity = Field(alias="acknowledgedQuantity")
    __properties: ClassVar[List[str]] = ["itemSequenceNumber", "buyerProductIdentifier", "vendorProductIdentifier", "acknowledgedQuantity"]

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
        """Create an instance of OrderItemAcknowledgement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of acknowledged_quantity
        if self.acknowledged_quantity:
            _dict['acknowledgedQuantity'] = self.acknowledged_quantity.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderItemAcknowledgement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "itemSequenceNumber": obj.get("itemSequenceNumber"),
            "buyerProductIdentifier": obj.get("buyerProductIdentifier"),
            "vendorProductIdentifier": obj.get("vendorProductIdentifier"),
            "acknowledgedQuantity": ItemQuantity.from_dict(obj["acknowledgedQuantity"]) if obj.get("acknowledgedQuantity") is not None else None
        })
        return _obj


