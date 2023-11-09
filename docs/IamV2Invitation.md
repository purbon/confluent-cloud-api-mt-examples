# IamV2Invitation

`Invitation` objects represent invitations to invite users to join your organizations in Confluent Cloud.  The API allows you to list all your invitations, as well as create, read, and delete a specified invitation.   Related guide: [User invitations in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/identity/user-accounts.html).  ## The Invitations Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.Invitation\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `invitations_per_org` | Invitations in a Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2InvitationMetadata**](IamV2InvitationMetadata.md) |  | [optional] 
**email** | **str** | The user/invitee&#39;s email address | [optional] 
**auth_type** | **str** | The user/invitee&#39;s authentication type. Note that only the [OrganizationAdmin role](https://docs.confluent.io/cloud/current/access-management/access-control/cloud-rbac.html#organizationadmin) can invite AUTH_TYPE_LOCAL users to SSO organizations. The user&#39;s auth_type is set as AUTH_TYPE_SSO by default if the organization has SSO enabled. Otherwise, the user&#39;s auth_type is AUTH_TYPE_LOCAL by default.  | [optional] 
**status** | **str** | The status of invitations | [optional] [readonly] 
**accepted_at** | **datetime** | The timestamp that the invitation was accepted | [optional] [readonly] 
**expires_at** | **datetime** | The timestamp that the invitation will expire | [optional] [readonly] 
**user** | [**IamV2InvitationUser**](IamV2InvitationUser.md) |  | [optional] 
**creator** | [**IamV2InvitationCreator**](IamV2InvitationCreator.md) |  | [optional] 

## Example

```python
from openapi_client.models.iam_v2_invitation import IamV2Invitation

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2Invitation from a JSON string
iam_v2_invitation_instance = IamV2Invitation.from_json(json)
# print the JSON string representation of the object
print IamV2Invitation.to_json()

# convert the object into a dict
iam_v2_invitation_dict = iam_v2_invitation_instance.to_dict()
# create an instance of IamV2Invitation from a dict
iam_v2_invitation_form_dict = iam_v2_invitation.from_dict(iam_v2_invitation_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


