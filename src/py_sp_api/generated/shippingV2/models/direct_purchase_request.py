# coding: utf-8

"""
    Amazon Shipping API

    The Amazon Shipping API is designed to support outbound shipping use cases both for orders originating on Amazon-owned marketplaces as well as external channels/marketplaces. With these APIs, you can request shipping rates, create shipments, cancel shipments, and track shipments.

    The version of the OpenAPI document: v2
    Contact: swa-api-core@amazon.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.shippingV2.models.address import Address
from py_sp_api.generated.shippingV2.models.channel_details import ChannelDetails
from py_sp_api.generated.shippingV2.models.package import Package
from py_sp_api.generated.shippingV2.models.requested_document_specification import RequestedDocumentSpecification
from typing import Optional, Set
from typing_extensions import Self

class DirectPurchaseRequest(BaseModel):
    """
    The request schema for the directPurchaseShipment operation. When the channel type is Amazon, the shipTo address is not required and will be ignored.
    """ # noqa: E501
    ship_to: Optional[Address] = Field(default=None, alias="shipTo")
    ship_from: Optional[Address] = Field(default=None, alias="shipFrom")
    return_to: Optional[Address] = Field(default=None, alias="returnTo")
    packages: Optional[List[Package]] = Field(default=None, description="A list of packages to be shipped through a shipping service offering.")
    channel_details: ChannelDetails = Field(alias="channelDetails")
    label_specifications: Optional[RequestedDocumentSpecification] = Field(default=None, alias="labelSpecifications")
    __properties: ClassVar[List[str]] = ["shipTo", "shipFrom", "returnTo", "packages", "channelDetails", "labelSpecifications"]

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
        """Create an instance of DirectPurchaseRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ship_to
        if self.ship_to:
            _dict['shipTo'] = self.ship_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_from
        if self.ship_from:
            _dict['shipFrom'] = self.ship_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of return_to
        if self.return_to:
            _dict['returnTo'] = self.return_to.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in packages (list)
        _items = []
        if self.packages:
            for _item_packages in self.packages:
                if _item_packages:
                    _items.append(_item_packages.to_dict())
            _dict['packages'] = _items
        # override the default output from pydantic by calling `to_dict()` of channel_details
        if self.channel_details:
            _dict['channelDetails'] = self.channel_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of label_specifications
        if self.label_specifications:
            _dict['labelSpecifications'] = self.label_specifications.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DirectPurchaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shipTo": Address.from_dict(obj["shipTo"]) if obj.get("shipTo") is not None else None,
            "shipFrom": Address.from_dict(obj["shipFrom"]) if obj.get("shipFrom") is not None else None,
            "returnTo": Address.from_dict(obj["returnTo"]) if obj.get("returnTo") is not None else None,
            "packages": [Package.from_dict(_item) for _item in obj["packages"]] if obj.get("packages") is not None else None,
            "channelDetails": ChannelDetails.from_dict(obj["channelDetails"]) if obj.get("channelDetails") is not None else None,
            "labelSpecifications": RequestedDocumentSpecification.from_dict(obj["labelSpecifications"]) if obj.get("labelSpecifications") is not None else None
        })
        return _obj


