# coding: utf-8

# flake8: noqa

"""
    Selling Partner API for Product Fees

    The Selling Partner API for Product Fees lets you programmatically retrieve estimated fees for a product. You can then account for those fees in your pricing.

    The version of the OpenAPI document: v0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from py_sp_api.generated.productFeesV0.api.fees_api import FeesApi

# import ApiClient
from py_sp_api.generated.productFeesV0.api_response import ApiResponse
from py_sp_api.generated.productFeesV0.api_client import ApiClient
from py_sp_api.generated.productFeesV0.configuration import Configuration
from py_sp_api.generated.productFeesV0.exceptions import OpenApiException
from py_sp_api.generated.productFeesV0.exceptions import ApiTypeError
from py_sp_api.generated.productFeesV0.exceptions import ApiValueError
from py_sp_api.generated.productFeesV0.exceptions import ApiKeyError
from py_sp_api.generated.productFeesV0.exceptions import ApiAttributeError
from py_sp_api.generated.productFeesV0.exceptions import ApiException

# import models into sdk package
from py_sp_api.generated.productFeesV0.models.error import Error
from py_sp_api.generated.productFeesV0.models.fee_detail import FeeDetail
from py_sp_api.generated.productFeesV0.models.fees_estimate import FeesEstimate
from py_sp_api.generated.productFeesV0.models.fees_estimate_by_id_request import FeesEstimateByIdRequest
from py_sp_api.generated.productFeesV0.models.fees_estimate_error import FeesEstimateError
from py_sp_api.generated.productFeesV0.models.fees_estimate_identifier import FeesEstimateIdentifier
from py_sp_api.generated.productFeesV0.models.fees_estimate_request import FeesEstimateRequest
from py_sp_api.generated.productFeesV0.models.fees_estimate_result import FeesEstimateResult
from py_sp_api.generated.productFeesV0.models.get_my_fees_estimate_request import GetMyFeesEstimateRequest
from py_sp_api.generated.productFeesV0.models.get_my_fees_estimate_response import GetMyFeesEstimateResponse
from py_sp_api.generated.productFeesV0.models.get_my_fees_estimate_result import GetMyFeesEstimateResult
from py_sp_api.generated.productFeesV0.models.get_my_fees_estimates_error_list import GetMyFeesEstimatesErrorList
from py_sp_api.generated.productFeesV0.models.id_type import IdType
from py_sp_api.generated.productFeesV0.models.included_fee_detail import IncludedFeeDetail
from py_sp_api.generated.productFeesV0.models.money_type import MoneyType
from py_sp_api.generated.productFeesV0.models.optional_fulfillment_program import OptionalFulfillmentProgram
from py_sp_api.generated.productFeesV0.models.points import Points
from py_sp_api.generated.productFeesV0.models.price_to_estimate_fees import PriceToEstimateFees

from .base_client import SPAPIClient
