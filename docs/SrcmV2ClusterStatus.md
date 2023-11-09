# SrcmV2ClusterStatus

The status of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecyle phase of the cluster:    PROVISIONED:  cluster is provisioned;    PROVISIONING:  cluster provisioning is in progress;    FAILED:  provisioning failed  | [readonly] 

## Example

```python
from openapi_client.models.srcm_v2_cluster_status import SrcmV2ClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2ClusterStatus from a JSON string
srcm_v2_cluster_status_instance = SrcmV2ClusterStatus.from_json(json)
# print the JSON string representation of the object
print SrcmV2ClusterStatus.to_json()

# convert the object into a dict
srcm_v2_cluster_status_dict = srcm_v2_cluster_status_instance.to_dict()
# create an instance of SrcmV2ClusterStatus from a dict
srcm_v2_cluster_status_form_dict = srcm_v2_cluster_status.from_dict(srcm_v2_cluster_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


