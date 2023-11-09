# IamV2SsoGroupMappingListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**IamV2SsoGroupMappingMetadata**](IamV2SsoGroupMappingMetadata.md) |  | 
**display_name** | **str** | The name of the &#x60;GroupMapping&#x60;. | 
**description** | **str** | A description of how this &#x60;GroupMapping&#x60; is used | 
**filter** | **str** | A filter expression in [Supported Common Expression Language (CEL)](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#supported-common-expression-language-cel-filters) that specifies which identities can authenticate using your group mapping (see [Set identity pool filters](https://docs.confluent.io/cloud/current/access-management/authenticate/oauth/identity-pools.html#set-identity-pool-filters) for more details). | 
**principal** | **str** | Represents the federated identity associated with this group mapping. | [readonly] 
**state** | **str** | The current state of the group mapping | [readonly] 

## Example

```python
from openapi_client.models.iam_v2_sso_group_mapping_list_data_inner import IamV2SsoGroupMappingListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2SsoGroupMappingListDataInner from a JSON string
iam_v2_sso_group_mapping_list_data_inner_instance = IamV2SsoGroupMappingListDataInner.from_json(json)
# print the JSON string representation of the object
print IamV2SsoGroupMappingListDataInner.to_json()

# convert the object into a dict
iam_v2_sso_group_mapping_list_data_inner_dict = iam_v2_sso_group_mapping_list_data_inner_instance.to_dict()
# create an instance of IamV2SsoGroupMappingListDataInner from a dict
iam_v2_sso_group_mapping_list_data_inner_form_dict = iam_v2_sso_group_mapping_list_data_inner.from_dict(iam_v2_sso_group_mapping_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


