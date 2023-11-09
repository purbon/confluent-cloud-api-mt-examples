# SrcmV2ClusterListMetadata


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
from openapi_client.models.srcm_v2_cluster_list_metadata import SrcmV2ClusterListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2ClusterListMetadata from a JSON string
srcm_v2_cluster_list_metadata_instance = SrcmV2ClusterListMetadata.from_json(json)
# print the JSON string representation of the object
print SrcmV2ClusterListMetadata.to_json()

# convert the object into a dict
srcm_v2_cluster_list_metadata_dict = srcm_v2_cluster_list_metadata_instance.to_dict()
# create an instance of SrcmV2ClusterListMetadata from a dict
srcm_v2_cluster_list_metadata_form_dict = srcm_v2_cluster_list_metadata.from_dict(srcm_v2_cluster_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


