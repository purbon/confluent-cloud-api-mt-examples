# CreateSrcmV2Cluster202Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**SrcmV2ClusterMetadata**](SrcmV2ClusterMetadata.md) |  | [optional] 
**spec** | [**ListSrcmV2Clusters200ResponseAllOfDataInnerSpec**](ListSrcmV2Clusters200ResponseAllOfDataInnerSpec.md) |  | 
**status** | [**SrcmV2ClusterStatus**](SrcmV2ClusterStatus.md) |  | 

## Example

```python
from openapi_client.models.create_srcm_v2_cluster202_response import CreateSrcmV2Cluster202Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSrcmV2Cluster202Response from a JSON string
create_srcm_v2_cluster202_response_instance = CreateSrcmV2Cluster202Response.from_json(json)
# print the JSON string representation of the object
print CreateSrcmV2Cluster202Response.to_json()

# convert the object into a dict
create_srcm_v2_cluster202_response_dict = create_srcm_v2_cluster202_response_instance.to_dict()
# create an instance of CreateSrcmV2Cluster202Response from a dict
create_srcm_v2_cluster202_response_form_dict = create_srcm_v2_cluster202_response.from_dict(create_srcm_v2_cluster202_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


