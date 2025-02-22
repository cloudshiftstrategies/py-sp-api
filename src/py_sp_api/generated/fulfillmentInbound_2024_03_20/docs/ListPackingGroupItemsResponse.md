# ListPackingGroupItemsResponse

The `listPackingGroupItems` response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[Item]**](Item.md) | Provides the information about the list of items in the packing group. | 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from py_sp_api.generated.fulfillmentInbound_2024_03_20.models.list_packing_group_items_response import ListPackingGroupItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListPackingGroupItemsResponse from a JSON string
list_packing_group_items_response_instance = ListPackingGroupItemsResponse.from_json(json)
# print the JSON string representation of the object
print(ListPackingGroupItemsResponse.to_json())

# convert the object into a dict
list_packing_group_items_response_dict = list_packing_group_items_response_instance.to_dict()
# create an instance of ListPackingGroupItemsResponse from a dict
list_packing_group_items_response_from_dict = ListPackingGroupItemsResponse.from_dict(list_packing_group_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


