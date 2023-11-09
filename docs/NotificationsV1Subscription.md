# NotificationsV1Subscription

`Subscription` objects represent the intent of the customers to get notifications of particular types. A subscription is created for a particular `NotificationType` and the user will get notifications on the `Integrations` that are provided while creating the subscription.  This API allows you to create, retrieve, and update subscriptions, as well as to view the list of all your subscriptions. You can also delete subscriptions with RECOMMENDED or OPTIONAL notification types. Subscriptions with REQUIRED notification types cannot be deleted.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Subscriptions Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.Subscription\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NotificationsV1SubscriptionMetadata**](NotificationsV1SubscriptionMetadata.md) |  | [optional] 
**current_state** | **str** | Denotes the state of the subscription. When the subscription is ENABLED, the user will receive notification on the configured Integrations. If the subscription is DISABLED, the user will not recieve any notification for the configured notification type. Note that, you cannot disable a subscription for &#x60;REQUIRED&#x60; notification type.  | [optional] 
**notification_type** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 
**integrations** | [**List[GlobalObjectReference]**](GlobalObjectReference.md) | Integrations to which notifications are to be sent. | [optional] 

## Example

```python
from openapi_client.models.notifications_v1_subscription import NotificationsV1Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1Subscription from a JSON string
notifications_v1_subscription_instance = NotificationsV1Subscription.from_json(json)
# print the JSON string representation of the object
print NotificationsV1Subscription.to_json()

# convert the object into a dict
notifications_v1_subscription_dict = notifications_v1_subscription_instance.to_dict()
# create an instance of NotificationsV1Subscription from a dict
notifications_v1_subscription_form_dict = notifications_v1_subscription.from_dict(notifications_v1_subscription_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


