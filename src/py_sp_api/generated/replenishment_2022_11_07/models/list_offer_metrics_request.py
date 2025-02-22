# coding: utf-8

"""
    Selling Partner API for Replenishment

    The Selling Partner API for Replenishment (Replenishment API) provides programmatic access to replenishment program metrics and offers. These programs provide recurring delivery of any replenishable item at a frequency chosen by the customer.  The Replenishment API is available worldwide wherever Amazon Subscribe & Save is available or is supported. The API is available to vendors and FBA selling partners.

    The version of the OpenAPI document: 2022-11-07
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.replenishment_2022_11_07.models.list_offer_metrics_request_filters import ListOfferMetricsRequestFilters
from py_sp_api.generated.replenishment_2022_11_07.models.list_offer_metrics_request_pagination import ListOfferMetricsRequestPagination
from py_sp_api.generated.replenishment_2022_11_07.models.list_offer_metrics_request_sort import ListOfferMetricsRequestSort
from typing import Optional, Set
from typing_extensions import Self

class ListOfferMetricsRequest(BaseModel):
    """
    The request body for the `listOfferMetrics` operation.
    """ # noqa: E501
    pagination: ListOfferMetricsRequestPagination
    sort: Optional[ListOfferMetricsRequestSort] = None
    filters: ListOfferMetricsRequestFilters
    __properties: ClassVar[List[str]] = ["pagination", "sort", "filters"]

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
        """Create an instance of ListOfferMetricsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pagination
        if self.pagination:
            _dict['pagination'] = self.pagination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of sort
        if self.sort:
            _dict['sort'] = self.sort.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListOfferMetricsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pagination": ListOfferMetricsRequestPagination.from_dict(obj["pagination"]) if obj.get("pagination") is not None else None,
            "sort": ListOfferMetricsRequestSort.from_dict(obj["sort"]) if obj.get("sort") is not None else None,
            "filters": ListOfferMetricsRequestFilters.from_dict(obj["filters"]) if obj.get("filters") is not None else None
        })
        return _obj


