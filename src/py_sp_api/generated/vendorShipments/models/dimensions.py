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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class Dimensions(BaseModel):
    """
    Physical dimensional measurements of a container.
    """ # noqa: E501
    length: StrictStr = Field(description="A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.")
    width: StrictStr = Field(description="A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.")
    height: StrictStr = Field(description="A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.")
    unit_of_measure: StrictStr = Field(description="The unit of measure for dimensions.", alias="unitOfMeasure")
    __properties: ClassVar[List[str]] = ["length", "width", "height", "unitOfMeasure"]

    @field_validator('unit_of_measure')
    def unit_of_measure_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['In', 'Ft', 'Meter', 'Yard']):
            raise ValueError("must be one of enum values ('In', 'Ft', 'Meter', 'Yard')")
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
        """Create an instance of Dimensions from a JSON string"""
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
        """Create an instance of Dimensions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "length": obj.get("length"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "unitOfMeasure": obj.get("unitOfMeasure")
        })
        return _obj


