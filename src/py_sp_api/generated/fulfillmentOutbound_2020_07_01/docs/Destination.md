# Destination

The destination for the delivery offer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_address** | [**VariablePrecisionAddress**](VariablePrecisionAddress.md) |  | [optional] 
**ip_address** | **str** | An IP Address. | [optional] 

## Example

```python
from py_sp_api.generated.fulfillmentOutbound_2020_07_01.models.destination import Destination

# TODO update the JSON string below
json = "{}"
# create an instance of Destination from a JSON string
destination_instance = Destination.from_json(json)
# print the JSON string representation of the object
print(Destination.to_json())

# convert the object into a dict
destination_dict = destination_instance.to_dict()
# create an instance of Destination from a dict
destination_from_dict = Destination.from_dict(destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


