# IamV2SsoGroupMappingList

`GroupMapping` objects represent a set of SSO identities that authorizes them to Confluent Cloud resources.  It provides a mapping functionality of your SSO user to a Confluent identity that is then used to provide access to Confluent Resources.   Related guide: [Use group mappings with your SSO provider](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html).  ## The Group Mappings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.sso.GroupMapping\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `group_mappings_per_org` | Number of Group Mappings per org |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**IamV2SsoGroupMappingListMetadata**](IamV2SsoGroupMappingListMetadata.md) |  | 
**data** | [**List[IamV2SsoGroupMappingListDataInner]**](IamV2SsoGroupMappingListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.iam_v2_sso_group_mapping_list import IamV2SsoGroupMappingList

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2SsoGroupMappingList from a JSON string
iam_v2_sso_group_mapping_list_instance = IamV2SsoGroupMappingList.from_json(json)
# print the JSON string representation of the object
print IamV2SsoGroupMappingList.to_json()

# convert the object into a dict
iam_v2_sso_group_mapping_list_dict = iam_v2_sso_group_mapping_list_instance.to_dict()
# create an instance of IamV2SsoGroupMappingList from a dict
iam_v2_sso_group_mapping_list_form_dict = iam_v2_sso_group_mapping_list.from_dict(iam_v2_sso_group_mapping_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


