# CdxV1ConsumerSharedResourceMetadata


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
from openapi_client.models.cdx_v1_consumer_shared_resource_metadata import CdxV1ConsumerSharedResourceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ConsumerSharedResourceMetadata from a JSON string
cdx_v1_consumer_shared_resource_metadata_instance = CdxV1ConsumerSharedResourceMetadata.from_json(json)
# print the JSON string representation of the object
print CdxV1ConsumerSharedResourceMetadata.to_json()

# convert the object into a dict
cdx_v1_consumer_shared_resource_metadata_dict = cdx_v1_consumer_shared_resource_metadata_instance.to_dict()
# create an instance of CdxV1ConsumerSharedResourceMetadata from a dict
cdx_v1_consumer_shared_resource_metadata_form_dict = cdx_v1_consumer_shared_resource_metadata.from_dict(cdx_v1_consumer_shared_resource_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


