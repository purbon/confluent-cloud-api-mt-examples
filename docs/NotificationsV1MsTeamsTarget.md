# NotificationsV1MsTeamsTarget

Target required for MS Teams integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Integration Type | 
**webhook_url** | **str** | MS Teams Webhook URL for the particular team channel | 

## Example

```python
from openapi_client.models.notifications_v1_ms_teams_target import NotificationsV1MsTeamsTarget

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1MsTeamsTarget from a JSON string
notifications_v1_ms_teams_target_instance = NotificationsV1MsTeamsTarget.from_json(json)
# print the JSON string representation of the object
print NotificationsV1MsTeamsTarget.to_json()

# convert the object into a dict
notifications_v1_ms_teams_target_dict = notifications_v1_ms_teams_target_instance.to_dict()
# create an instance of NotificationsV1MsTeamsTarget from a dict
notifications_v1_ms_teams_target_form_dict = notifications_v1_ms_teams_target.from_dict(notifications_v1_ms_teams_target_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


