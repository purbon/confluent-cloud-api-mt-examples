# SrcmV2ClusterSpecUpdate

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package** | **str** | The billing package.  Note: Clusters can be upgraded from ESSENTIALS to ADVANCED, but cannot be downgraded from ADVANCED to ESSENTIALS.  | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.srcm_v2_cluster_spec_update import SrcmV2ClusterSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2ClusterSpecUpdate from a JSON string
srcm_v2_cluster_spec_update_instance = SrcmV2ClusterSpecUpdate.from_json(json)
# print the JSON string representation of the object
print SrcmV2ClusterSpecUpdate.to_json()

# convert the object into a dict
srcm_v2_cluster_spec_update_dict = srcm_v2_cluster_spec_update_instance.to_dict()
# create an instance of SrcmV2ClusterSpecUpdate from a dict
srcm_v2_cluster_spec_update_form_dict = srcm_v2_cluster_spec_update.from_dict(srcm_v2_cluster_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


