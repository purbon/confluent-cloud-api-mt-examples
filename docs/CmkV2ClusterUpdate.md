# CmkV2ClusterUpdate

`Clusters` objects represent Apache Kafka Clusters on Confluent Cloud.  The API allows you to list, create, read, update, and delete your Kafka clusters.   Related guide: [Confluent Cloud Cluster Management for Apache Kafka APIs](https://docs.confluent.io/cloud/current/clusters/cluster-api.html).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/cmk.v2.Cluster\" />  ## Quotas and Limits This resource is subject to the [following quotas](https://docs.confluent.io/cloud/current/quotas/overview.html):  | Quota | Description | | --- | --- | | `kafka_clusters_per_environment` | Number of clusters in one Confluent Cloud environment |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CmkV2ClusterMetadata**](CmkV2ClusterMetadata.md) |  | [optional] 
**spec** | [**CmkV2ClusterSpecUpdate**](CmkV2ClusterSpecUpdate.md) |  | [optional] 
**status** | [**CmkV2ClusterStatus**](CmkV2ClusterStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.cmk_v2_cluster_update import CmkV2ClusterUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2ClusterUpdate from a JSON string
cmk_v2_cluster_update_instance = CmkV2ClusterUpdate.from_json(json)
# print the JSON string representation of the object
print CmkV2ClusterUpdate.to_json()

# convert the object into a dict
cmk_v2_cluster_update_dict = cmk_v2_cluster_update_instance.to_dict()
# create an instance of CmkV2ClusterUpdate from a dict
cmk_v2_cluster_update_form_dict = cmk_v2_cluster_update.from_dict(cmk_v2_cluster_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


