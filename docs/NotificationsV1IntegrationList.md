# NotificationsV1IntegrationList

You can create an `Integration` to specify how we can notify you when we receive an alert/notification for a subscription. Please note that you can only perform create, update and delete operations for integrations of type `Webhook`, `Slack` and `MsTeams`. You cannot create, update or delete integrations of type `RoleEmail` and `UserEmail`.   Related guide: [Cloud Notifications](https://docs.confluent.io/cloud/current/monitoring/configure-notifications.html#notifications-for-ccloud).  ## The Integrations Model <SchemaDefinition schemaRef=\"#/components/schemas/notifications.v1.Integration\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `integrations_per_org` | Maximum number of integrations in one Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NotificationsV1IntegrationListMetadata**](NotificationsV1IntegrationListMetadata.md) |  | 
**data** | [**List[NotificationsV1IntegrationListDataInner]**](NotificationsV1IntegrationListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.notifications_v1_integration_list import NotificationsV1IntegrationList

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1IntegrationList from a JSON string
notifications_v1_integration_list_instance = NotificationsV1IntegrationList.from_json(json)
# print the JSON string representation of the object
print NotificationsV1IntegrationList.to_json()

# convert the object into a dict
notifications_v1_integration_list_dict = notifications_v1_integration_list_instance.to_dict()
# create an instance of NotificationsV1IntegrationList from a dict
notifications_v1_integration_list_form_dict = notifications_v1_integration_list.from_dict(notifications_v1_integration_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


