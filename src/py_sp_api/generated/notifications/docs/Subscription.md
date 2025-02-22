# Subscription

Information about the subscription.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | The subscription identifier generated when the subscription is created. | 
**payload_version** | **str** | The version of the payload object to be used in the notification. | 
**destination_id** | **str** | The identifier for the destination where notifications will be delivered. | 
**processing_directive** | [**ProcessingDirective**](ProcessingDirective.md) |  | [optional] 

## Example

```python
from py_sp_api.generated.notifications.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


