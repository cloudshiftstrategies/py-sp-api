# coding: utf-8

"""
    Selling Partner API for Retail Procurement Shipments

    The Selling Partner API for Retail Procurement Shipments provides programmatic access to retail shipping data for vendors.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorShipments.models.party_identification import PartyIdentification
from py_sp_api.generated.vendorShipments.models.vendor_details import VendorDetails
from typing import Optional, Set
from typing_extensions import Self

class ShipmentInformation(BaseModel):
    """
    Shipment Information details for Label request.
    """ # noqa: E501
    vendor_details: Optional[VendorDetails] = Field(default=None, alias="vendorDetails")
    buyer_reference_number: Optional[StrictStr] = Field(default=None, description="The buyer reference number is a unique identifier generated by the buyer for all Collect and WePay shipments.", alias="buyerReferenceNumber")
    ship_to_party: Optional[PartyIdentification] = Field(default=None, alias="shipToParty")
    ship_from_party: Optional[PartyIdentification] = Field(default=None, alias="shipFromParty")
    warehouse_id: Optional[StrictStr] = Field(default=None, description="Vendor Warehouse ID from where the shipment is scheduled to be picked up by buyer / Carrier.", alias="warehouseId")
    master_tracking_id: Optional[StrictStr] = Field(default=None, description="Unique Id with  which  the shipment can be tracked for Small Parcels.", alias="masterTrackingId")
    total_label_count: Optional[StrictInt] = Field(default=None, description="Number of Labels that are created as part of this shipment.", alias="totalLabelCount")
    ship_mode: Optional[StrictStr] = Field(default=None, description="Type of shipment whether it is Small Parcel", alias="shipMode")
    __properties: ClassVar[List[str]] = ["vendorDetails", "buyerReferenceNumber", "shipToParty", "shipFromParty", "warehouseId", "masterTrackingId", "totalLabelCount", "shipMode"]

    @field_validator('ship_mode')
    def ship_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['SmallParcel', 'LTL']):
            raise ValueError("must be one of enum values ('SmallParcel', 'LTL')")
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
        """Create an instance of ShipmentInformation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of vendor_details
        if self.vendor_details:
            _dict['vendorDetails'] = self.vendor_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_to_party
        if self.ship_to_party:
            _dict['shipToParty'] = self.ship_to_party.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ship_from_party
        if self.ship_from_party:
            _dict['shipFromParty'] = self.ship_from_party.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShipmentInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "vendorDetails": VendorDetails.from_dict(obj["vendorDetails"]) if obj.get("vendorDetails") is not None else None,
            "buyerReferenceNumber": obj.get("buyerReferenceNumber"),
            "shipToParty": PartyIdentification.from_dict(obj["shipToParty"]) if obj.get("shipToParty") is not None else None,
            "shipFromParty": PartyIdentification.from_dict(obj["shipFromParty"]) if obj.get("shipFromParty") is not None else None,
            "warehouseId": obj.get("warehouseId"),
            "masterTrackingId": obj.get("masterTrackingId"),
            "totalLabelCount": obj.get("totalLabelCount"),
            "shipMode": obj.get("shipMode")
        })
        return _obj


