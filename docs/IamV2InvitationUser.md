# IamV2InvitationUser

The user/invitee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.iam_v2_invitation_user import IamV2InvitationUser

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2InvitationUser from a JSON string
iam_v2_invitation_user_instance = IamV2InvitationUser.from_json(json)
# print the JSON string representation of the object
print IamV2InvitationUser.to_json()

# convert the object into a dict
iam_v2_invitation_user_dict = iam_v2_invitation_user_instance.to_dict()
# create an instance of IamV2InvitationUser from a dict
iam_v2_invitation_user_form_dict = iam_v2_invitation_user.from_dict(iam_v2_invitation_user_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


