# CmkV2ClusterListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**CmkV2ClusterMetadata**](CmkV2ClusterMetadata.md) |  | 
**spec** | **object** |  | 
**status** | [**CmkV2ClusterStatus**](CmkV2ClusterStatus.md) |  | 

## Example

```python
from openapi_client.models.cmk_v2_cluster_list_data_inner import CmkV2ClusterListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2ClusterListDataInner from a JSON string
cmk_v2_cluster_list_data_inner_instance = CmkV2ClusterListDataInner.from_json(json)
# print the JSON string representation of the object
print CmkV2ClusterListDataInner.to_json()

# convert the object into a dict
cmk_v2_cluster_list_data_inner_dict = cmk_v2_cluster_list_data_inner_instance.to_dict()
# create an instance of CmkV2ClusterListDataInner from a dict
cmk_v2_cluster_list_data_inner_form_dict = cmk_v2_cluster_list_data_inner.from_dict(cmk_v2_cluster_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


