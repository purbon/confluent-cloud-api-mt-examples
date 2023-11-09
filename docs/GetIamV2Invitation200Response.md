# GetIamV2Invitation200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**IamV2InvitationMetadata**](IamV2InvitationMetadata.md) |  | [optional] 
**email** | **str** | The user/invitee&#39;s email address | 
**auth_type** | **str** | The user/invitee&#39;s authentication type. Note that only the [OrganizationAdmin role](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite AUTH_TYPE_LOCAL users to SSO organizations. The user&#39;s auth_type is set as AUTH_TYPE_SSO by default if the organization has SSO enabled. Otherwise, the user&#39;s auth_type is AUTH_TYPE_LOCAL by default.  | [optional] 
**status** | **str** | The status of invitations | [optional] [readonly] 
**accepted_at** | **datetime** | The timestamp that the invitation was accepted | [optional] [readonly] 
**expires_at** | **datetime** | The timestamp that the invitation will expire | [optional] [readonly] 
**user** | [**IamV2InvitationUser**](IamV2InvitationUser.md) |  | [optional] 
**creator** | [**IamV2InvitationCreator**](IamV2InvitationCreator.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_iam_v2_invitation200_response import GetIamV2Invitation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIamV2Invitation200Response from a JSON string
get_iam_v2_invitation200_response_instance = GetIamV2Invitation200Response.from_json(json)
# print the JSON string representation of the object
print GetIamV2Invitation200Response.to_json()

# convert the object into a dict
get_iam_v2_invitation200_response_dict = get_iam_v2_invitation200_response_instance.to_dict()
# create an instance of GetIamV2Invitation200Response from a dict
get_iam_v2_invitation200_response_form_dict = get_iam_v2_invitation200_response.from_dict(get_iam_v2_invitation200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


