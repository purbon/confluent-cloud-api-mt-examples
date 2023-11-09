# FcpmV2RegionMetadata


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
from openapi_client.models.fcpm_v2_region_metadata import FcpmV2RegionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of FcpmV2RegionMetadata from a JSON string
fcpm_v2_region_metadata_instance = FcpmV2RegionMetadata.from_json(json)
# print the JSON string representation of the object
print FcpmV2RegionMetadata.to_json()

# convert the object into a dict
fcpm_v2_region_metadata_dict = fcpm_v2_region_metadata_instance.to_dict()
# create an instance of FcpmV2RegionMetadata from a dict
fcpm_v2_region_metadata_form_dict = fcpm_v2_region_metadata.from_dict(fcpm_v2_region_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


