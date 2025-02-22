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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Address(BaseModel):
    """
    Address of the party.
    """ # noqa: E501
    name: StrictStr = Field(description="The name of the person, business or institution at that address.")
    address_line1: StrictStr = Field(description="First line of the address.", alias="addressLine1")
    address_line2: Optional[StrictStr] = Field(default=None, description="Additional street address information, if required.", alias="addressLine2")
    address_line3: Optional[StrictStr] = Field(default=None, description="Additional street address information, if required.", alias="addressLine3")
    city: Optional[StrictStr] = Field(default=None, description="The city where the person, business or institution is located.")
    county: Optional[StrictStr] = Field(default=None, description="The county where person, business or institution is located.")
    district: Optional[StrictStr] = Field(default=None, description="The district where person, business or institution is located.")
    state_or_region: Optional[StrictStr] = Field(default=None, description="The state or region where person, business or institution is located.", alias="stateOrRegion")
    postal_code: Optional[StrictStr] = Field(default=None, description="The postal code of that address. It contains a series of letters or digits or both, sometimes including spaces or punctuation.", alias="postalCode")
    country_code: StrictStr = Field(description="The two-letter country code in [ISO 3166-1 alpha-2](https://www.iban.com/country-codes) format.", alias="countryCode")
    phone: Optional[StrictStr] = Field(default=None, description="The phone number of the person, business or institution located at that address.")
    __properties: ClassVar[List[str]] = ["name", "addressLine1", "addressLine2", "addressLine3", "city", "county", "district", "stateOrRegion", "postalCode", "countryCode", "phone"]

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
            "name": obj.get("name"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "addressLine3": obj.get("addressLine3"),
            "city": obj.get("city"),
            "county": obj.get("county"),
            "district": obj.get("district"),
            "stateOrRegion": obj.get("stateOrRegion"),
            "postalCode": obj.get("postalCode"),
            "countryCode": obj.get("countryCode"),
            "phone": obj.get("phone")
        })
        return _obj


