# CmkV2ClusterStatus

The status of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecyle phase of the cluster:   PROVISIONED:  cluster is provisioned;   PROVISIONING:  cluster provisioning is in progress;   FAILED:  provisioning failed  | [readonly] 
**cku** | **int** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.cmk_v2_cluster_status import CmkV2ClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2ClusterStatus from a JSON string
cmk_v2_cluster_status_instance = CmkV2ClusterStatus.from_json(json)
# print the JSON string representation of the object
print CmkV2ClusterStatus.to_json()

# convert the object into a dict
cmk_v2_cluster_status_dict = cmk_v2_cluster_status_instance.to_dict()
# create an instance of CmkV2ClusterStatus from a dict
cmk_v2_cluster_status_form_dict = cmk_v2_cluster_status.from_dict(cmk_v2_cluster_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


