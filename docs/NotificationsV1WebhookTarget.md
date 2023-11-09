# NotificationsV1WebhookTarget

Target required for webhook integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Integration Type | 
**url** | **str** | URL endpoint for the webhook | 

## Example

```python
from openapi_client.models.notifications_v1_webhook_target import NotificationsV1WebhookTarget

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1WebhookTarget from a JSON string
notifications_v1_webhook_target_instance = NotificationsV1WebhookTarget.from_json(json)
# print the JSON string representation of the object
print NotificationsV1WebhookTarget.to_json()

# convert the object into a dict
notifications_v1_webhook_target_dict = notifications_v1_webhook_target_instance.to_dict()
# create an instance of NotificationsV1WebhookTarget from a dict
notifications_v1_webhook_target_form_dict = notifications_v1_webhook_target.from_dict(notifications_v1_webhook_target_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


