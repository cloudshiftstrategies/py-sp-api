# CancelFulfillmentOrderResponse

The response schema for the `cancelFulfillmentOrder` operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[Error]**](Error.md) | A list of error responses returned when a request is unsuccessful. | [optional] 

## Example

```python
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.cancel_fulfillment_order_response import CancelFulfillmentOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CancelFulfillmentOrderResponse from a JSON string
cancel_fulfillment_order_response_instance = CancelFulfillmentOrderResponse.from_json(json)
# print the JSON string representation of the object
print(CancelFulfillmentOrderResponse.to_json())

# convert the object into a dict
cancel_fulfillment_order_response_dict = cancel_fulfillment_order_response_instance.to_dict()
# create an instance of CancelFulfillmentOrderResponse from a dict
cancel_fulfillment_order_response_from_dict = CancelFulfillmentOrderResponse.from_dict(cancel_fulfillment_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


