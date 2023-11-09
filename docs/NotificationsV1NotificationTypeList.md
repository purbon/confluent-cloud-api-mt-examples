# NotificationsV1NotificationTypeList

The type of notifications (and their corresponding metadata) supported by Confluent.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Notification Types Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.NotificationType\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NotificationsV1NotificationTypeListMetadata**](NotificationsV1NotificationTypeListMetadata.md) |  | 
**data** | [**List[NotificationsV1NotificationTypeListDataInner]**](NotificationsV1NotificationTypeListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.notifications_v1_notification_type_list import NotificationsV1NotificationTypeList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1NotificationTypeList from a JSON string
notifications_v1_notification_type_list_instance = NotificationsV1NotificationTypeList.from_json(json)
# print the JSON string representation of the object
print NotificationsV1NotificationTypeList.to_json()

# convert the object into a dict
notifications_v1_notification_type_list_dict = notifications_v1_notification_type_list_instance.to_dict()
# create an instance of NotificationsV1NotificationTypeList from a dict
notifications_v1_notification_type_list_form_dict = notifications_v1_notification_type_list.from_dict(notifications_v1_notification_type_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


