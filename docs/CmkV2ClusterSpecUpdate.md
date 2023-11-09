# CmkV2ClusterSpecUpdate

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the cluster. | [optional] 
**availability** | **str** | The availability zone configuration of the cluster  | [optional] 
**config** | [**CmkV2ClusterSpecConfig**](CmkV2ClusterSpecConfig.md) |  | [optional] 
**environment** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.cmk_v2_cluster_spec_update import CmkV2ClusterSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2ClusterSpecUpdate from a JSON string
cmk_v2_cluster_spec_update_instance = CmkV2ClusterSpecUpdate.from_json(json)
# print the JSON string representation of the object
print CmkV2ClusterSpecUpdate.to_json()

# convert the object into a dict
cmk_v2_cluster_spec_update_dict = cmk_v2_cluster_spec_update_instance.to_dict()
# create an instance of CmkV2ClusterSpecUpdate from a dict
cmk_v2_cluster_spec_update_form_dict = cmk_v2_cluster_spec_update.from_dict(cmk_v2_cluster_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


