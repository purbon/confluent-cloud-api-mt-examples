# KsqldbcmV2ClusterStatus

The status of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_endpoint** | **str** | The dataplane endpoint of the ksqlDB cluster. | [optional] [readonly] 
**phase** | **str** | Status of the ksqlDB cluster. | [readonly] 
**is_paused** | **bool** | Tells you if the cluster has been paused | [readonly] 
**storage** | **int** | Amount of storage (in GB) provisioned to this cluster | [readonly] 
**topic_prefix** | **str** | Topic name prefix used by this ksqlDB cluster. Used to assign ACLs for this ksqlDB cluster to use. | [optional] [readonly] 

## Example

```python
from openapi_client.models.ksqldbcm_v2_cluster_status import KsqldbcmV2ClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of KsqldbcmV2ClusterStatus from a JSON string
ksqldbcm_v2_cluster_status_instance = KsqldbcmV2ClusterStatus.from_json(json)
# print the JSON string representation of the object
print KsqldbcmV2ClusterStatus.to_json()

# convert the object into a dict
ksqldbcm_v2_cluster_status_dict = ksqldbcm_v2_cluster_status_instance.to_dict()
# create an instance of KsqldbcmV2ClusterStatus from a dict
ksqldbcm_v2_cluster_status_form_dict = ksqldbcm_v2_cluster_status.from_dict(ksqldbcm_v2_cluster_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


