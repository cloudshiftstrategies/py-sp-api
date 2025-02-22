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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.shippingV2.models.address import Address
from py_sp_api.generated.shippingV2.models.generation_status import GenerationStatus
from typing import Optional, Set
from typing_extensions import Self

class CollectionFormsHistoryRecord(BaseModel):
    """
    Active Account Details
    """ # noqa: E501
    carrier_name: Optional[StrictStr] = Field(default=None, description="The carrier name for the offering.", alias="carrierName")
    creation_date: Optional[StrictStr] = Field(default=None, description="Creation Time for this account.", alias="creationDate")
    generation_status: Optional[GenerationStatus] = Field(default=None, alias="generationStatus")
    collection_form_id: Optional[StrictStr] = Field(default=None, description="Collection Form Id for Reprint .", alias="collectionFormId")
    ship_from_address: Optional[Address] = Field(default=None, alias="shipFromAddress")
    __properties: ClassVar[List[str]] = ["carrierName", "creationDate", "generationStatus", "collectionFormId", "shipFromAddress"]

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
        """Create an instance of CollectionFormsHistoryRecord from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ship_from_address
        if self.ship_from_address:
            _dict['shipFromAddress'] = self.ship_from_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CollectionFormsHistoryRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "carrierName": obj.get("carrierName"),
            "creationDate": obj.get("creationDate"),
            "generationStatus": obj.get("generationStatus"),
            "collectionFormId": obj.get("collectionFormId"),
            "shipFromAddress": Address.from_dict(obj["shipFromAddress"]) if obj.get("shipFromAddress") is not None else None
        })
        return _obj


