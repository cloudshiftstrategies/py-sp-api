# coding: utf-8

"""
    Vendor Invoices v1

    The Selling Partner API for Retail Procurement Payments provides programmatic access to vendors payments data.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.vendorInvoices.models.money import Money
from typing import Optional, Set
from typing_extensions import Self

class TaxDetails(BaseModel):
    """
    Details of tax amount applied.
    """ # noqa: E501
    tax_type: StrictStr = Field(description="Type of the tax applied.", alias="taxType")
    tax_rate: Optional[StrictStr] = Field(default=None, description="A decimal number with no loss of precision. Useful when precision loss is unacceptable, as with currencies. Follows RFC7159 for number representation. <br>**Pattern** : `^-?(0|([1-9]\\d*))(\\.\\d+)?([eE][+-]?\\d+)?$`.", alias="taxRate")
    tax_amount: Money = Field(alias="taxAmount")
    taxable_amount: Optional[Money] = Field(default=None, alias="taxableAmount")
    __properties: ClassVar[List[str]] = ["taxType", "taxRate", "taxAmount", "taxableAmount"]

    @field_validator('tax_type')
    def tax_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['CGST', 'SGST', 'CESS', 'UTGST', 'IGST', 'MwSt.', 'PST', 'TVA', 'VAT', 'GST', 'ST', 'Consumption', 'MutuallyDefined', 'DomesticVAT']):
            raise ValueError("must be one of enum values ('CGST', 'SGST', 'CESS', 'UTGST', 'IGST', 'MwSt.', 'PST', 'TVA', 'VAT', 'GST', 'ST', 'Consumption', 'MutuallyDefined', 'DomesticVAT')")
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
        """Create an instance of TaxDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tax_amount
        if self.tax_amount:
            _dict['taxAmount'] = self.tax_amount.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taxable_amount
        if self.taxable_amount:
            _dict['taxableAmount'] = self.taxable_amount.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TaxDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taxType": obj.get("taxType"),
            "taxRate": obj.get("taxRate"),
            "taxAmount": Money.from_dict(obj["taxAmount"]) if obj.get("taxAmount") is not None else None,
            "taxableAmount": Money.from_dict(obj["taxableAmount"]) if obj.get("taxableAmount") is not None else None
        })
        return _obj


