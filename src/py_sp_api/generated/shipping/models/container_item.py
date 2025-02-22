# coding: utf-8

"""
    Selling Partner API for Shipping

    Provides programmatic access to Amazon Shipping APIs.   **Note:** If you are new to the Amazon Shipping API, refer to the latest version of <a href=\"https://developer-docs.amazon.com/amazon-shipping/docs/shipping-api-v2-reference\">Amazon Shipping API (v2)</a> on the <a href=\"https://developer-docs.amazon.com/amazon-shipping/\">Amazon Shipping Developer Documentation</a> site.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from py_sp_api.generated.shipping.models.currency import Currency
from py_sp_api.generated.shipping.models.weight import Weight
from typing import Optional, Set
from typing_extensions import Self

class ContainerItem(BaseModel):
    """
    Item in the container.
    """ # noqa: E501
    quantity: Union[StrictFloat, StrictInt] = Field(description="The quantity of the items of this type in the container.")
    unit_price: Currency = Field(alias="unitPrice")
    unit_weight: Weight = Field(alias="unitWeight")
    title: Annotated[str, Field(strict=True, max_length=30)] = Field(description="A descriptive title of the item.")
    __properties: ClassVar[List[str]] = ["quantity", "unitPrice", "unitWeight", "title"]

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
        """Create an instance of ContainerItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of unit_price
        if self.unit_price:
            _dict['unitPrice'] = self.unit_price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unit_weight
        if self.unit_weight:
            _dict['unitWeight'] = self.unit_weight.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContainerItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "unitPrice": Currency.from_dict(obj["unitPrice"]) if obj.get("unitPrice") is not None else None,
            "unitWeight": Weight.from_dict(obj["unitWeight"]) if obj.get("unitWeight") is not None else None,
            "title": obj.get("title")
        })
        return _obj


