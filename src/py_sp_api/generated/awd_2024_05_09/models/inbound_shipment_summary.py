# coding: utf-8

"""
    The Selling Partner API for Amazon Warehousing and Distribution

    The Selling Partner API for Amazon Warehousing and Distribution (AWD) provides programmatic access to information about AWD shipments and inventory. 

    The version of the OpenAPI document: 2024-05-09
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_sp_api.generated.awd_2024_05_09.models.inbound_shipment_status import InboundShipmentStatus
from typing import Optional, Set
from typing_extensions import Self

class InboundShipmentSummary(BaseModel):
    """
    Summary for an AWD inbound shipment containing the shipment ID, which can be used to retrieve the actual shipment.
    """ # noqa: E501
    created_at: Optional[datetime] = Field(default=None, description="Timestamp when the shipment was created.", alias="createdAt")
    external_reference_id: Optional[StrictStr] = Field(default=None, description="Optional client-provided reference ID that can be used to correlate this shipment with client resources. For example, to map this shipment to an internal bookkeeping order record.", alias="externalReferenceId")
    order_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="The AWD inbound order ID that this inbound shipment belongs to.", alias="orderId")
    shipment_id: Annotated[str, Field(min_length=1, strict=True)] = Field(description="A unique shipment ID.", alias="shipmentId")
    shipment_status: InboundShipmentStatus = Field(alias="shipmentStatus")
    updated_at: Optional[datetime] = Field(default=None, description="Timestamp when the shipment was updated.", alias="updatedAt")
    __properties: ClassVar[List[str]] = ["createdAt", "externalReferenceId", "orderId", "shipmentId", "shipmentStatus", "updatedAt"]

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
        """Create an instance of InboundShipmentSummary from a JSON string"""
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
        """Create an instance of InboundShipmentSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "createdAt": obj.get("createdAt"),
            "externalReferenceId": obj.get("externalReferenceId"),
            "orderId": obj.get("orderId"),
            "shipmentId": obj.get("shipmentId"),
            "shipmentStatus": obj.get("shipmentStatus"),
            "updatedAt": obj.get("updatedAt")
        })
        return _obj


