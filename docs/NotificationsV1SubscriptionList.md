# NotificationsV1SubscriptionList

`Subscription` objects represent the intent of the customers to get notifications of particular types. A subscription is created for a particular `NotificationType` and the user will get notifications on the `Integrations` that are provided while creating the subscription.  This API allows you to create, retrieve, and update subscriptions, as well as to view the list of all your subscriptions. You can also delete subscriptions with RECOMMENDED or OPTIONAL notification types. Subscriptions with REQUIRED notification types cannot be deleted.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Subscriptions Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.Subscription\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NotificationsV1SubscriptionListMetadata**](NotificationsV1SubscriptionListMetadata.md) |  | 
**data** | [**List[NotificationsV1SubscriptionListDataInner]**](NotificationsV1SubscriptionListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.notifications_v1_subscription_list import NotificationsV1SubscriptionList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1SubscriptionList from a JSON string
notifications_v1_subscription_list_instance = NotificationsV1SubscriptionList.from_json(json)
# print the JSON string representation of the object
print NotificationsV1SubscriptionList.to_json()

# convert the object into a dict
notifications_v1_subscription_list_dict = notifications_v1_subscription_list_instance.to_dict()
# create an instance of NotificationsV1SubscriptionList from a dict
notifications_v1_subscription_list_form_dict = notifications_v1_subscription_list.from_dict(notifications_v1_subscription_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


