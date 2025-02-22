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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class CreateFulfillmentOrderItem(BaseModel):
    """
    Item information for creating a fulfillment order.
    """ # noqa: E501
    seller_sku: Annotated[str, Field(strict=True, max_length=50)] = Field(description="The seller SKU of the item.", alias="sellerSku")
    seller_fulfillment_order_item_id: Annotated[str, Field(strict=True, max_length=50)] = Field(description="A fulfillment order item identifier that the seller creates to track fulfillment order items. Used to disambiguate multiple fulfillment items that have the same `SellerSKU`. For example, the seller might assign different `SellerFulfillmentOrderItemId` values to two items in a fulfillment order that share the same `SellerSKU` but have different `GiftMessage` values.", alias="sellerFulfillmentOrderItemId")
    quantity: StrictInt = Field(description="The item quantity.")
    gift_message: Optional[Annotated[str, Field(strict=True, max_length=512)]] = Field(default=None, description="A message to the gift recipient, if applicable.", alias="giftMessage")
    displayable_comment: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.", alias="displayableComment")
    fulfillment_network_sku: Optional[StrictStr] = Field(default=None, description="Amazon's fulfillment network SKU of the item.", alias="fulfillmentNetworkSku")
    per_unit_declared_value: Optional[Money] = Field(default=None, alias="perUnitDeclaredValue")
    per_unit_price: Optional[Money] = Field(default=None, alias="perUnitPrice")
    per_unit_tax: Optional[Money] = Field(default=None, alias="perUnitTax")
    __properties: ClassVar[List[str]] = ["sellerSku", "sellerFulfillmentOrderItemId", "quantity", "giftMessage", "displayableComment", "fulfillmentNetworkSku", "perUnitDeclaredValue", "perUnitPrice", "perUnitTax"]

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
        """Create an instance of CreateFulfillmentOrderItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of per_unit_declared_value
        if self.per_unit_declared_value:
            _dict['perUnitDeclaredValue'] = self.per_unit_declared_value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of per_unit_price
        if self.per_unit_price:
            _dict['perUnitPrice'] = self.per_unit_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of per_unit_tax
        if self.per_unit_tax:
            _dict['perUnitTax'] = self.per_unit_tax.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateFulfillmentOrderItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sellerSku": obj.get("sellerSku"),
            "sellerFulfillmentOrderItemId": obj.get("sellerFulfillmentOrderItemId"),
            "quantity": obj.get("quantity"),
            "giftMessage": obj.get("giftMessage"),
            "displayableComment": obj.get("displayableComment"),
            "fulfillmentNetworkSku": obj.get("fulfillmentNetworkSku"),
            "perUnitDeclaredValue": Money.from_dict(obj["perUnitDeclaredValue"]) if obj.get("perUnitDeclaredValue") is not None else None,
            "perUnitPrice": Money.from_dict(obj["perUnitPrice"]) if obj.get("perUnitPrice") is not None else None,
            "perUnitTax": Money.from_dict(obj["perUnitTax"]) if obj.get("perUnitTax") is not None else None
        })
        return _obj


