# IamV2InvitationCreator

The invitation creator

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.iam_v2_invitation_creator import IamV2InvitationCreator

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2InvitationCreator from a JSON string
iam_v2_invitation_creator_instance = IamV2InvitationCreator.from_json(json)
# print the JSON string representation of the object
print IamV2InvitationCreator.to_json()

# convert the object into a dict
iam_v2_invitation_creator_dict = iam_v2_invitation_creator_instance.to_dict()
# create an instance of IamV2InvitationCreator from a dict
iam_v2_invitation_creator_form_dict = iam_v2_invitation_creator.from_dict(iam_v2_invitation_creator_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


