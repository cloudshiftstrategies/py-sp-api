# coding: utf-8

"""
    Selling Partner APIs for Fulfillment Outbound

    The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.

    The version of the OpenAPI document: 2020-07-01
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class EventCode(str, Enum):
    """
    The event code for the delivery event.
    """

    """
    allowed enum values
    """
    EVENT_101 = 'EVENT_101'
    EVENT_102 = 'EVENT_102'
    EVENT_201 = 'EVENT_201'
    EVENT_202 = 'EVENT_202'
    EVENT_203 = 'EVENT_203'
    EVENT_204 = 'EVENT_204'
    EVENT_205 = 'EVENT_205'
    EVENT_206 = 'EVENT_206'
    EVENT_301 = 'EVENT_301'
    EVENT_302 = 'EVENT_302'
    EVENT_304 = 'EVENT_304'
    EVENT_306 = 'EVENT_306'
    EVENT_307 = 'EVENT_307'
    EVENT_308 = 'EVENT_308'
    EVENT_309 = 'EVENT_309'
    EVENT_401 = 'EVENT_401'
    EVENT_402 = 'EVENT_402'
    EVENT_403 = 'EVENT_403'
    EVENT_404 = 'EVENT_404'
    EVENT_405 = 'EVENT_405'
    EVENT_406 = 'EVENT_406'
    EVENT_407 = 'EVENT_407'
    EVENT_408 = 'EVENT_408'
    EVENT_409 = 'EVENT_409'
    EVENT_411 = 'EVENT_411'
    EVENT_412 = 'EVENT_412'
    EVENT_413 = 'EVENT_413'
    EVENT_414 = 'EVENT_414'
    EVENT_415 = 'EVENT_415'
    EVENT_416 = 'EVENT_416'
    EVENT_417 = 'EVENT_417'
    EVENT_418 = 'EVENT_418'
    EVENT_419 = 'EVENT_419'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EventCode from a JSON string"""
        return cls(json.loads(json_str))


