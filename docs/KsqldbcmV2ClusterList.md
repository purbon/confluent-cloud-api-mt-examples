# KsqldbcmV2ClusterList

`Cluster` represents a ksqlDB runtime that you can issue queries to using its API endpoint. It executes SQL statements and queries which under the hood get built into corresponding Kafka Streams topologies. The API allows you to list, create, read, and delete your ksqlDB clusters.   Related guide: [ksqlDB in Confluent Cloud](https://docs.confluent.io/cloud/current/ksqldb/ksqldb-cluster-api.html).  ## The Clusters Model <SchemaDefinition schemaRef=\"#/components/schemas/ksqldbcm.v2.Cluster\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `ksql.limits.max_apps_per_cluster` | Clusters in one Confluent Cloud Kafka Cluster. |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**KsqldbcmV2ClusterListMetadata**](KsqldbcmV2ClusterListMetadata.md) |  | 
**data** | [**List[KsqldbcmV2ClusterListDataInner]**](KsqldbcmV2ClusterListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.ksqldbcm_v2_cluster_list import KsqldbcmV2ClusterList

# TODO update the JSON string below
json = "{}"
# create an instance of KsqldbcmV2ClusterList from a JSON string
ksqldbcm_v2_cluster_list_instance = KsqldbcmV2ClusterList.from_json(json)
# print the JSON string representation of the object
print KsqldbcmV2ClusterList.to_json()

# convert the object into a dict
ksqldbcm_v2_cluster_list_dict = ksqldbcm_v2_cluster_list_instance.to_dict()
# create an instance of KsqldbcmV2ClusterList from a dict
ksqldbcm_v2_cluster_list_form_dict = ksqldbcm_v2_cluster_list.from_dict(ksqldbcm_v2_cluster_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


