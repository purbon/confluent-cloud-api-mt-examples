# NotificationsV1SubscriptionMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.notifications_v1_subscription_metadata import NotificationsV1SubscriptionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1SubscriptionMetadata from a JSON string
notifications_v1_subscription_metadata_instance = NotificationsV1SubscriptionMetadata.from_json(json)
# print the JSON string representation of the object
print NotificationsV1SubscriptionMetadata.to_json()

# convert the object into a dict
notifications_v1_subscription_metadata_dict = notifications_v1_subscription_metadata_instance.to_dict()
# create an instance of NotificationsV1SubscriptionMetadata from a dict
notifications_v1_subscription_metadata_form_dict = notifications_v1_subscription_metadata.from_dict(notifications_v1_subscription_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


