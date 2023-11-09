# ByokV1KeyMetadata


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
from openapi_client.models.byok_v1_key_metadata import ByokV1KeyMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1KeyMetadata from a JSON string
byok_v1_key_metadata_instance = ByokV1KeyMetadata.from_json(json)
# print the JSON string representation of the object
print ByokV1KeyMetadata.to_json()

# convert the object into a dict
byok_v1_key_metadata_dict = byok_v1_key_metadata_instance.to_dict()
# create an instance of ByokV1KeyMetadata from a dict
byok_v1_key_metadata_form_dict = byok_v1_key_metadata.from_dict(byok_v1_key_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


