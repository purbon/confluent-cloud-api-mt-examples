# KsqldbcmV2ClusterMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.ksqldbcm_v2_cluster_metadata import KsqldbcmV2ClusterMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of KsqldbcmV2ClusterMetadata from a JSON string
ksqldbcm_v2_cluster_metadata_instance = KsqldbcmV2ClusterMetadata.from_json(json)
# print the JSON string representation of the object
print KsqldbcmV2ClusterMetadata.to_json()

# convert the object into a dict
ksqldbcm_v2_cluster_metadata_dict = ksqldbcm_v2_cluster_metadata_instance.to_dict()
# create an instance of KsqldbcmV2ClusterMetadata from a dict
ksqldbcm_v2_cluster_metadata_form_dict = ksqldbcm_v2_cluster_metadata.from_dict(ksqldbcm_v2_cluster_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


