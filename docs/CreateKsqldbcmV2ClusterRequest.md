# CreateKsqldbcmV2ClusterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**KsqldbcmV2ClusterMetadata**](KsqldbcmV2ClusterMetadata.md) |  | [optional] 
**spec** | [**CreateKsqldbcmV2ClusterRequestAllOfSpec**](CreateKsqldbcmV2ClusterRequestAllOfSpec.md) |  | 
**status** | [**KsqldbcmV2ClusterStatus**](KsqldbcmV2ClusterStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_ksqldbcm_v2_cluster_request import CreateKsqldbcmV2ClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKsqldbcmV2ClusterRequest from a JSON string
create_ksqldbcm_v2_cluster_request_instance = CreateKsqldbcmV2ClusterRequest.from_json(json)
# print the JSON string representation of the object
print CreateKsqldbcmV2ClusterRequest.to_json()

# convert the object into a dict
create_ksqldbcm_v2_cluster_request_dict = create_ksqldbcm_v2_cluster_request_instance.to_dict()
# create an instance of CreateKsqldbcmV2ClusterRequest from a dict
create_ksqldbcm_v2_cluster_request_form_dict = create_ksqldbcm_v2_cluster_request.from_dict(create_ksqldbcm_v2_cluster_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


