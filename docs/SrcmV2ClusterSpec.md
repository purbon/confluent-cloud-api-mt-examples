# SrcmV2ClusterSpec

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The cluster name. | [optional] [readonly] 
**package** | **str** | The billing package.  Note: Clusters can be upgraded from ESSENTIALS to ADVANCED, but cannot be downgraded from ADVANCED to ESSENTIALS.  | [optional] 
**http_endpoint** | **str** | The cluster HTTP request URL. | [optional] [readonly] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 
**region** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.srcm_v2_cluster_spec import SrcmV2ClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2ClusterSpec from a JSON string
srcm_v2_cluster_spec_instance = SrcmV2ClusterSpec.from_json(json)
# print the JSON string representation of the object
print SrcmV2ClusterSpec.to_json()

# convert the object into a dict
srcm_v2_cluster_spec_dict = srcm_v2_cluster_spec_instance.to_dict()
# create an instance of SrcmV2ClusterSpec from a dict
srcm_v2_cluster_spec_form_dict = srcm_v2_cluster_spec.from_dict(srcm_v2_cluster_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


