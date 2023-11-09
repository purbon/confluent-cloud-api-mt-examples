# SrcmV2ClusterList

`Clusters` objects represent Schema Registry Clusters on Confluent Cloud.  The API allows you to list, create, read, and delete your Schema Registry clusters.   Related guide: [Confluent Cloud Schema Registry Cluster APIs](https://docs.confluent.io/cloud/current/stream-governance/clusters-regions-api.html#schema-registry-cluster-management).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/srcm.v2.Cluster\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**SrcmV2ClusterListMetadata**](SrcmV2ClusterListMetadata.md) |  | 
**data** | [**List[SrcmV2ClusterListDataInner]**](SrcmV2ClusterListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.srcm_v2_cluster_list import SrcmV2ClusterList

# TODO update the JSON string below
json = "{}"
# create an instance of SrcmV2ClusterList from a JSON string
srcm_v2_cluster_list_instance = SrcmV2ClusterList.from_json(json)
# print the JSON string representation of the object
print SrcmV2ClusterList.to_json()

# convert the object into a dict
srcm_v2_cluster_list_dict = srcm_v2_cluster_list_instance.to_dict()
# create an instance of SrcmV2ClusterList from a dict
srcm_v2_cluster_list_form_dict = srcm_v2_cluster_list.from_dict(srcm_v2_cluster_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


