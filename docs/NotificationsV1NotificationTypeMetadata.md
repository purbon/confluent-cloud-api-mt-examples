# NotificationsV1NotificationTypeMetadata


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
from openapi_client.models.notifications_v1_notification_type_metadata import NotificationsV1NotificationTypeMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1NotificationTypeMetadata from a JSON string
notifications_v1_notification_type_metadata_instance = NotificationsV1NotificationTypeMetadata.from_json(json)
# print the JSON string representation of the object
print NotificationsV1NotificationTypeMetadata.to_json()

# convert the object into a dict
notifications_v1_notification_type_metadata_dict = notifications_v1_notification_type_metadata_instance.to_dict()
# create an instance of NotificationsV1NotificationTypeMetadata from a dict
notifications_v1_notification_type_metadata_form_dict = notifications_v1_notification_type_metadata.from_dict(notifications_v1_notification_type_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


