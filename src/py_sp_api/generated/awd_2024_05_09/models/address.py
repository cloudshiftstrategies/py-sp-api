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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Shipping address that represents the origin or destination location.
    """ # noqa: E501
    address_line1: StrictStr = Field(description="First line of the address text.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="Optional second line of the address text.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="Optional third line of the address text.", alias="addressLine3")
    city: Optional[StrictStr] = Field(default=None, description="Optional city where this address is located.")
    country_code: StrictStr = Field(description="Two-digit, ISO 3166-1 alpha-2 formatted country code where this address is located.", alias="countryCode")
    county: Optional[StrictStr] = Field(default=None, description="Optional county where this address is located.")
    district: Optional[StrictStr] = Field(default=None, description="Optional district where this address is located.")
    name: StrictStr = Field(description="Name of the person, business, or institution at this address.")
    phone_number: Optional[StrictStr] = Field(default=None, description="Optional E.164-formatted phone number for an available contact at this address.", alias="phoneNumber")
    postal_code: Optional[StrictStr] = Field(default=None, description="Optional postal code where this address is located.", alias="postalCode")
    state_or_region: StrictStr = Field(description="State or region where this address is located. Note that this is contextual to the specified country code.", alias="stateOrRegion")
    __properties: ClassVar[List[str]] = ["addressLine1", "addressLine2", "addressLine3", "city", "countryCode", "county", "district", "name", "phoneNumber", "postalCode", "stateOrRegion"]

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
        """Create an instance of Address from a JSON string"""
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
        """Create an instance of Address from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "city": obj.get("city"),
            "countryCode": obj.get("countryCode"),
            "county": obj.get("county"),
            "district": obj.get("district"),
            "name": obj.get("name"),
            "phoneNumber": obj.get("phoneNumber"),
            "postalCode": obj.get("postalCode"),
            "stateOrRegion": obj.get("stateOrRegion")
        })
        return _obj


