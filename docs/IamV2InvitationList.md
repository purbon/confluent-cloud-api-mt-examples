# IamV2InvitationList

`Invitation` objects represent invitations to invite users to join your organizations in Confluent Cloud.  The API allows you to list all your invitations, as well as create, read, and delete a specified invitation.   Related guide: [User invitations in Confluent Cloud](https://docs.confluent.io/cloud/current/access-management/identity/user-accounts.html).  ## The Invitations Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.Invitation\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `invitations_per_org` | Invitations in a Confluent Cloud organization |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2InvitationListMetadata**](IamV2InvitationListMetadata.md) |  | 
**data** | [**List[IamV2InvitationListDataInner]**](IamV2InvitationListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_invitation_list import IamV2InvitationList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2InvitationList from a JSON string
iam_v2_invitation_list_instance = IamV2InvitationList.from_json(json)
# print the JSON string representation of the object
print IamV2InvitationList.to_json()

# convert the object into a dict
iam_v2_invitation_list_dict = iam_v2_invitation_list_instance.to_dict()
# create an instance of IamV2InvitationList from a dict
iam_v2_invitation_list_form_dict = iam_v2_invitation_list.from_dict(iam_v2_invitation_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


