# coding: utf-8

"""
    Selling Partner API for Services

    With the Services API, you can build applications that help service providers get and modify their service orders and manage their resources.

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from py_sp_api.generated.services.models.service_job import ServiceJob
from typing import Optional, Set
from typing_extensions import Self

class JobListing(BaseModel):
    """
    The payload for the `getServiceJobs` operation.
    """ # noqa: E501
    total_result_size: Optional[StrictInt] = Field(default=None, description="Total result size of the query result.", alias="totalResultSize")
    next_page_token: Optional[StrictStr] = Field(default=None, description="A generated string used to pass information to your next request. If `nextPageToken` is returned, pass the value of `nextPageToken` to the `pageToken` to get next results.", alias="nextPageToken")
    previous_page_token: Optional[StrictStr] = Field(default=None, description="A generated string used to pass information to your next request. If `previousPageToken` is returned, pass the value of `previousPageToken` to the `pageToken` to get previous page results.", alias="previousPageToken")
    jobs: Optional[List[ServiceJob]] = Field(default=None, description="List of job details for the given input.")
    __properties: ClassVar[List[str]] = ["totalResultSize", "nextPageToken", "previousPageToken", "jobs"]

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
        """Create an instance of JobListing from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item_jobs in self.jobs:
                if _item_jobs:
                    _items.append(_item_jobs.to_dict())
            _dict['jobs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobListing from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalResultSize": obj.get("totalResultSize"),
            "nextPageToken": obj.get("nextPageToken"),
            "previousPageToken": obj.get("previousPageToken"),
            "jobs": [ServiceJob.from_dict(_item) for _item in obj["jobs"]] if obj.get("jobs") is not None else None
        })
        return _obj


