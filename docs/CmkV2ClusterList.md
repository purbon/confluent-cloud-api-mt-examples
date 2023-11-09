# CmkV2ClusterList

`Clusters` objects represent Apache Kafka Clusters on Confluent Cloud.  The API allows you to list, create, read, update, and delete your Kafka clusters.   Related guide: [Confluent Cloud Cluster Management for Apache Kafka APIs](https://docs.confluent.io/cloud/current/clusters/cluster-api.html).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/cmk.v2.Cluster\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `kafka_clusters_per_environment` | Number of clusters in one Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**CmkV2ClusterListMetadata**](CmkV2ClusterListMetadata.md) |  | 
**data** | [**List[CmkV2ClusterListDataInner]**](CmkV2ClusterListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.cmk_v2_cluster_list import CmkV2ClusterList

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2ClusterList from a JSON string
cmk_v2_cluster_list_instance = CmkV2ClusterList.from_json(json)
# print the JSON string representation of the object
print CmkV2ClusterList.to_json()

# convert the object into a dict
cmk_v2_cluster_list_dict = cmk_v2_cluster_list_instance.to_dict()
# create an instance of CmkV2ClusterList from a dict
cmk_v2_cluster_list_form_dict = cmk_v2_cluster_list.from_dict(cmk_v2_cluster_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


