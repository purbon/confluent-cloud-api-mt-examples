# NotificationsV1RoleEmailTarget

Email integration target to send email to all user with specified role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Email Integration type for Role | 
**role_name** | **str** | name of the role | 

## Example

```python
from openapi_client.models.notifications_v1_role_email_target import NotificationsV1RoleEmailTarget

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationsV1RoleEmailTarget from a JSON string
notifications_v1_role_email_target_instance = NotificationsV1RoleEmailTarget.from_json(json)
# print the JSON string representation of the object
print NotificationsV1RoleEmailTarget.to_json()

# convert the object into a dict
notifications_v1_role_email_target_dict = notifications_v1_role_email_target_instance.to_dict()
# create an instance of NotificationsV1RoleEmailTarget from a dict
notifications_v1_role_email_target_form_dict = notifications_v1_role_email_target.from_dict(notifications_v1_role_email_target_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


