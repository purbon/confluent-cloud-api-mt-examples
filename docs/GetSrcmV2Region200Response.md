# GetSrcmV2Region200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**SrcmV2RegionMetadata**](SrcmV2RegionMetadata.md) |  | [optional] 
**spec** | **object** |  | 

## Example

```python
from openapi_client.models.get_srcm_v2_region200_response import GetSrcmV2Region200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSrcmV2Region200Response from a JSON string
get_srcm_v2_region200_response_instance = GetSrcmV2Region200Response.from_json(json)
# print the JSON string representation of the object
print GetSrcmV2Region200Response.to_json()

# convert the object into a dict
get_srcm_v2_region200_response_dict = get_srcm_v2_region200_response_instance.to_dict()
# create an instance of GetSrcmV2Region200Response from a dict
get_srcm_v2_region200_response_form_dict = get_srcm_v2_region200_response.from_dict(get_srcm_v2_region200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


