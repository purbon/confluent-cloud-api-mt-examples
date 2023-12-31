# NotificationsV1NotificationType

The type of notifications (and their corresponding metadata) supported by Confluent.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Notification Types Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.NotificationType\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NotificationsV1NotificationTypeMetadata**](NotificationsV1NotificationTypeMetadata.md) |  | [optional] 
**display_name** | **str** | Human readable display name of the notification type  | [optional] 
**category** | **str** | Represents the group with which the notification is associated. Notifications are grouped under certain categories for better organization. - BILLING_LICENSING: All billing, payments or licensing related notifications are grouped here. - SECURITY: All Confluent Cloud and Platform security related notifications are grouped here. - SERVICE: All Confluent services (eg. Kafka, Schema Registry, Connect etc.) related notifications are   grouped here. - ACCOUNT: All Confluent account related notifications are grouped here. For example: Billing, payment or license related notifications are grouped in BILLING_LICENSING category.  | [optional] 
**description** | **str** | Human readable description of the notification type  | [optional] 
**subscription_priority** | **str** | Indicates whether the notification is auto-subscribed and if the user can opt-out. - REQUIRED: the user is auto-subscribed to this notification and can&#39;t opt-out. - RECOMMENDED: the user is auto-subscribed to this notification and can opt-out. - OPTIONAL: the user is not auto-subscribed to this notification but can explicitly subscribe to it.  | [optional] 
**is_included_in_plan** | **bool** | Whether this notification is available to subscribe or not as per the user&#39;s current billing plan.  | [optional] 
**severity** | **str** | Severity indicates the impact of this notification. - CRITICAL: a high impact notification which needs immediate attention. - WARN: a warning notification which can be addressed now or later. - INFO: an informational notification.  | [optional] 

## Example

```python
from openapi_client.models.notifications_v1_notification_type import NotificationsV1NotificationType

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1NotificationType from a JSON string
notifications_v1_notification_type_instance = NotificationsV1NotificationType.from_json(json)
# print the JSON string representation of the object
print NotificationsV1NotificationType.to_json()

# convert the object into a dict
notifications_v1_notification_type_dict = notifications_v1_notification_type_instance.to_dict()
# create an instance of NotificationsV1NotificationType from a dict
notifications_v1_notification_type_form_dict = notifications_v1_notification_type.from_dict(notifications_v1_notification_type_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


