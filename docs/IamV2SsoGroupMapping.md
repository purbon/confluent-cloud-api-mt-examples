# IamV2SsoGroupMapping

`GroupMapping` objects represent a set of SSO identities that authorizes them to Confluent Cloud resources.  It provides a mapping functionality of your SSO user to a Confluent identity that is then used to provide access to Confluent Resources.   Related guide: [Use group mappings with your SSO provider](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html).  ## The Group Mappings Model <SchemaDefinition schemaRef=\"#/components/schemas/iam.v2.sso.GroupMapping\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `group_mappings_per_org` | Number of Group Mappings per org |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**IamV2SsoGroupMappingMetadata**](IamV2SsoGroupMappingMetadata.md) |  | [optional] 
**display_name** | **str** | The name of the &#x60;GroupMapping&#x60;. | [optional] 
**description** | **str** | A description of how this &#x60;GroupMapping&#x60; is used | [optional] 
**filter** | **str** | A filter expression in [Supported Common Expression Language (CEL)](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#supported-common-expression-language-cel-filters) that specifies which identities can authenticate using your group mapping (see [Set identity pool filters](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#set-identity-pool-filters) for more details). | [optional] 
**principal** | **str** | Represents the federated identity associated with this group mapping. | [optional] [readonly] 
**state** | **str** | The current state of the group mapping | [optional] [readonly] 

## Example

```python
from openapi_client.models.iam_v2_sso_group_mapping import IamV2SsoGroupMapping

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2SsoGroupMapping from a JSON string
iam_v2_sso_group_mapping_instance = IamV2SsoGroupMapping.from_json(json)
# print the JSON string representation of the object
print IamV2SsoGroupMapping.to_json()

# convert the object into a dict
iam_v2_sso_group_mapping_dict = iam_v2_sso_group_mapping_instance.to_dict()
# create an instance of IamV2SsoGroupMapping from a dict
iam_v2_sso_group_mapping_form_dict = iam_v2_sso_group_mapping.from_dict(iam_v2_sso_group_mapping_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


