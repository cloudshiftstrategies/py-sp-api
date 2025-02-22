# GetFulfillmentOrderResponse

The response schema for the `getFulfillmentOrder` operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | [**GetFulfillmentOrderResult**](GetFulfillmentOrderResult.md) |  | [optional] 
**errors** | [**List[Error]**](Error.md) | A list of error responses returned when a request is unsuccessful. | [optional] 

## Example

```python
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.get_fulfillment_order_response import GetFulfillmentOrderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetFulfillmentOrderResponse from a JSON string
get_fulfillment_order_response_instance = GetFulfillmentOrderResponse.from_json(json)
# print the JSON string representation of the object
print(GetFulfillmentOrderResponse.to_json())

# convert the object into a dict
get_fulfillment_order_response_dict = get_fulfillment_order_response_instance.to_dict()
# create an instance of GetFulfillmentOrderResponse from a dict
get_fulfillment_order_response_from_dict = GetFulfillmentOrderResponse.from_dict(get_fulfillment_order_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


