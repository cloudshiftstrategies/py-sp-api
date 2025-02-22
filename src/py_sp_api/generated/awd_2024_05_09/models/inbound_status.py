# coding: utf-8

"""
    The Selling Partner API for Amazon Warehousing and Distribution

    The Selling Partner API for Amazon Warehousing and Distribution (AWD) provides programmatic access to information about AWD shipments and inventory. 

    The version of the OpenAPI document: 2024-05-09
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class InboundStatus(str, Enum):
    """
    The supported statuses for an inbound order.
    """

    """
    allowed enum values
    """
    DRAFT = 'DRAFT'
    VALIDATING = 'VALIDATING'
    CONFIRMED = 'CONFIRMED'
    CLOSED = 'CLOSED'
    EXPIRED = 'EXPIRED'
    CANCELLED = 'CANCELLED'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of InboundStatus from a JSON string"""
        return cls(json.loads(json_str))


