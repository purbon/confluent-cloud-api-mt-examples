# IamV2SsoGroupMappingMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.iam_v2_sso_group_mapping_metadata import IamV2SsoGroupMappingMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2SsoGroupMappingMetadata from a JSON string
iam_v2_sso_group_mapping_metadata_instance = IamV2SsoGroupMappingMetadata.from_json(json)
# print the JSON string representation of the object
print IamV2SsoGroupMappingMetadata.to_json()

# convert the object into a dict
iam_v2_sso_group_mapping_metadata_dict = iam_v2_sso_group_mapping_metadata_instance.to_dict()
# create an instance of IamV2SsoGroupMappingMetadata from a dict
iam_v2_sso_group_mapping_metadata_form_dict = iam_v2_sso_group_mapping_metadata.from_dict(iam_v2_sso_group_mapping_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


