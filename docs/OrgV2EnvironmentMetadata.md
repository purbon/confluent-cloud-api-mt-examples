# OrgV2EnvironmentMetadata


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
from openapi_client.models.org_v2_environment_metadata import OrgV2EnvironmentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OrgV2EnvironmentMetadata from a JSON string
org_v2_environment_metadata_instance = OrgV2EnvironmentMetadata.from_json(json)
# print the JSON string representation of the object
print OrgV2EnvironmentMetadata.to_json()

# convert the object into a dict
org_v2_environment_metadata_dict = org_v2_environment_metadata_instance.to_dict()
# create an instance of OrgV2EnvironmentMetadata from a dict
org_v2_environment_metadata_form_dict = org_v2_environment_metadata.from_dict(org_v2_environment_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


