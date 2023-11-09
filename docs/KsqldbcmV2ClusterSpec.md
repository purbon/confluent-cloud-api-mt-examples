# KsqldbcmV2ClusterSpec

The desired state of the Cluster

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the ksqlDB cluster. | [optional] 
**use_detailed_processing_log** | **bool** | This flag controls whether you want to include the row data in the processing log topic. Turn it off if you don&#39;t want to emit sensitive information to the processing log  | [optional] [default to True]
**csu** | **int** | The number of CSUs (Confluent Streaming Units) in a ksqlDB cluster. | [optional] 
**kafka_cluster** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 
**credential_identity** | [**TypedGlobalObjectReference**](TypedGlobalObjectReference.md) |  | [optional] 
**environment** | [**GlobalObjectReference**](GlobalObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.ksqldbcm_v2_cluster_spec import KsqldbcmV2ClusterSpec

# TODO update the JSON string below
json = "{}"
# create an instance of KsqldbcmV2ClusterSpec from a JSON string
ksqldbcm_v2_cluster_spec_instance = KsqldbcmV2ClusterSpec.from_json(json)
# print the JSON string representation of the object
print KsqldbcmV2ClusterSpec.to_json()

# convert the object into a dict
ksqldbcm_v2_cluster_spec_dict = ksqldbcm_v2_cluster_spec_instance.to_dict()
# create an instance of KsqldbcmV2ClusterSpec from a dict
ksqldbcm_v2_cluster_spec_form_dict = ksqldbcm_v2_cluster_spec.from_dict(ksqldbcm_v2_cluster_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


