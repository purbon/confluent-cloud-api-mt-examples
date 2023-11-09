# SrcmV2Cluster

`Clusters` objects represent Schema Registry Clusters on Confluent Cloud.  The API allows you to list, create, read, and delete your Schema Registry clusters.   Related guide: [Confluent Cloud Schema Registry Cluster APIs](https://docs.confluent.io/cloud/current/stream-governance/clusters-regions-api.html#schema-registry-cluster-management).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/srcm.v2.Cluster\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**SrcmV2ClusterMetadata**](SrcmV2ClusterMetadata.md) |  | [optional] 
**spec** | [**SrcmV2ClusterSpec**](SrcmV2ClusterSpec.md) |  | [optional] 
**status** | [**SrcmV2ClusterStatus**](SrcmV2ClusterStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.srcm_v2_cluster import SrcmV2Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2Cluster from a JSON string
srcm_v2_cluster_instance = SrcmV2Cluster.from_json(json)
# print the JSON string representation of the object
print SrcmV2Cluster.to_json()

# convert the object into a dict
srcm_v2_cluster_dict = srcm_v2_cluster_instance.to_dict()
# create an instance of SrcmV2Cluster from a dict
srcm_v2_cluster_form_dict = srcm_v2_cluster.from_dict(srcm_v2_cluster_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


