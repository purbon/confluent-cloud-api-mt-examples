# UpdateCmkV2ClusterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CmkV2ClusterMetadata**](CmkV2ClusterMetadata.md) |  | [optional] 
**spec** | [**UpdateCmkV2ClusterRequestAllOfSpec**](UpdateCmkV2ClusterRequestAllOfSpec.md) |  | 
**status** | [**CmkV2ClusterStatus**](CmkV2ClusterStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_cmk_v2_cluster_request import UpdateCmkV2ClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCmkV2ClusterRequest from a JSON string
update_cmk_v2_cluster_request_instance = UpdateCmkV2ClusterRequest.from_json(json)
# print the JSON string representation of the object
print UpdateCmkV2ClusterRequest.to_json()

# convert the object into a dict
update_cmk_v2_cluster_request_dict = update_cmk_v2_cluster_request_instance.to_dict()
# create an instance of UpdateCmkV2ClusterRequest from a dict
update_cmk_v2_cluster_request_form_dict = update_cmk_v2_cluster_request.from_dict(update_cmk_v2_cluster_request_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


