# coding: utf-8

"""
    Selling Partner API for Product Fees

    The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.productFeesV0.models.optional_fulfillment_program import OptionalFulfillmentProgram
from py_sp_api.generated.productFeesV0.models.price_to_estimate_fees import PriceToEstimateFees
from typing import Optional, Set
from typing_extensions import Self

class FeesEstimateRequest(BaseModel):
    """
    A product, marketplace, and proposed price used to request estimated fees.
    """ # noqa: E501
    marketplace_id: StrictStr = Field(description="A marketplace identifier.", alias="MarketplaceId")
    is_amazon_fulfilled: Optional[StrictBool] = Field(default=None, description="When true, the offer is fulfilled by Amazon.", alias="IsAmazonFulfilled")
    price_to_estimate_fees: PriceToEstimateFees = Field(alias="PriceToEstimateFees")
    identifier: StrictStr = Field(description="A unique identifier provided by the caller to track this request.", alias="Identifier")
    optional_fulfillment_program: Optional[OptionalFulfillmentProgram] = Field(default=None, alias="OptionalFulfillmentProgram")
    __properties: ClassVar[List[str]] = ["MarketplaceId", "IsAmazonFulfilled", "PriceToEstimateFees", "Identifier", "OptionalFulfillmentProgram"]

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
        """Create an instance of FeesEstimateRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price_to_estimate_fees
        if self.price_to_estimate_fees:
            _dict['PriceToEstimateFees'] = self.price_to_estimate_fees.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeesEstimateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "MarketplaceId": obj.get("MarketplaceId"),
            "IsAmazonFulfilled": obj.get("IsAmazonFulfilled"),
            "PriceToEstimateFees": PriceToEstimateFees.from_dict(obj["PriceToEstimateFees"]) if obj.get("PriceToEstimateFees") is not None else None,
            "Identifier": obj.get("Identifier"),
            "OptionalFulfillmentProgram": obj.get("OptionalFulfillmentProgram")
        })
        return _obj


