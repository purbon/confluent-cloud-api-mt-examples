# NotificationsV1Target

Target for the particular integration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Integration Type | 
**webhook_url** | **str** | MS Teams Webhook URL for the particular team channel | 
**role_name** | **str** | name of the role | 
**user** | **str** | ID of the user | 
**url** | **str** | URL endpoint for the webhook | 

## Example

```python
from openapi_client.models.notifications_v1_target import NotificationsV1Target

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1Target from a JSON string
notifications_v1_target_instance = NotificationsV1Target.from_json(json)
# print the JSON string representation of the object
print NotificationsV1Target.to_json()

# convert the object into a dict
notifications_v1_target_dict = notifications_v1_target_instance.to_dict()
# create an instance of NotificationsV1Target from a dict
notifications_v1_target_form_dict = notifications_v1_target.from_dict(notifications_v1_target_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


