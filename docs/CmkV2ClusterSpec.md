# CmkV2ClusterSpec

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the cluster. | [optional] 
**availability** | **str** | The availability zone configuration of the cluster  | [optional] 
**cloud** | **str** | The cloud service provider in which the cluster is running. | [optional] 
**region** | **str** | The cloud service provider region where the cluster is running. | [optional] 
**config** | [**CmkV2ClusterSpecConfig**](CmkV2ClusterSpecConfig.md) |  | [optional] 
**kafka_bootstrap_endpoint** | **str** | The bootstrap endpoint used by Kafka clients to connect to the cluster. | [optional] [readonly] 
**http_endpoint** | **str** | The cluster HTTP request URL. | [optional] [readonly] 
**api_endpoint** | **str** | The Kafka API cluster endpoint used by Kafka clients to connect to the cluster. | [optional] [readonly] 
**environment** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 
**network** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 
**byok** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.cmk_v2_cluster_spec import CmkV2ClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2ClusterSpec from a JSON string
cmk_v2_cluster_spec_instance = CmkV2ClusterSpec.from_json(json)
# print the JSON string representation of the object
print CmkV2ClusterSpec.to_json()

# convert the object into a dict
cmk_v2_cluster_spec_dict = cmk_v2_cluster_spec_instance.to_dict()
# create an instance of CmkV2ClusterSpec from a dict
cmk_v2_cluster_spec_form_dict = cmk_v2_cluster_spec.from_dict(cmk_v2_cluster_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


