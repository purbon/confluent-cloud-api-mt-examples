# OrgV2EnvironmentListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.org_v2_environment_list_metadata import OrgV2EnvironmentListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of OrgV2EnvironmentListMetadata from a JSON string
org_v2_environment_list_metadata_instance = OrgV2EnvironmentListMetadata.from_json(json)
# print the JSON string representation of the object
print OrgV2EnvironmentListMetadata.to_json()

# convert the object into a dict
org_v2_environment_list_metadata_dict = org_v2_environment_list_metadata_instance.to_dict()
# create an instance of OrgV2EnvironmentListMetadata from a dict
org_v2_environment_list_metadata_form_dict = org_v2_environment_list_metadata.from_dict(org_v2_environment_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


