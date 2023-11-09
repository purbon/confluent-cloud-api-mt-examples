# NotificationsV1SlackTarget

Target required for Slack integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Integration Type | 
**webhook_url** | **str** | Slack Webhook URL for the particular Slack channel | 

## Example

```python
from openapi_client.models.notifications_v1_slack_target import NotificationsV1SlackTarget

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1SlackTarget from a JSON string
notifications_v1_slack_target_instance = NotificationsV1SlackTarget.from_json(json)
# print the JSON string representation of the object
print NotificationsV1SlackTarget.to_json()

# convert the object into a dict
notifications_v1_slack_target_dict = notifications_v1_slack_target_instance.to_dict()
# create an instance of NotificationsV1SlackTarget from a dict
notifications_v1_slack_target_form_dict = notifications_v1_slack_target.from_dict(notifications_v1_slack_target_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


