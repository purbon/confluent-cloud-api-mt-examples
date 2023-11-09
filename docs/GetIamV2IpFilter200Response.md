# GetIamV2IpFilter200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**IamV2IpFilterMetadata**](IamV2IpFilterMetadata.md) |  | [optional] 
**filter_name** | **str** | A human readable name for an IP Filter. Can contain any unicode letter or number, the ASCII space character, or any of the following special characters: &#x60;[&#x60;, &#x60;]&#x60;, &#x60;|&#x60;, &#x60;&amp;&#x60;, &#x60;+&#x60;, &#x60;-&#x60;, &#x60;_&#x60;, &#x60;/&#x60;, &#x60;.&#x60;, &#x60;,&#x60;.  | 
**resource_group** | **str** | Scope of resources covered by this IP filter. The only resource_group currently available is \&quot;management\&quot;. | 
**ip_groups** | [**List[GlobalObjectReference]**](GlobalObjectReference.md) | A list of IP Groups. | 

## Example

```python
from openapi_client.models.get_iam_v2_ip_filter200_response import GetIamV2IpFilter200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIamV2IpFilter200Response from a JSON string
get_iam_v2_ip_filter200_response_instance = GetIamV2IpFilter200Response.from_json(json)
# print the JSON string representation of the object
print GetIamV2IpFilter200Response.to_json()

# convert the object into a dict
get_iam_v2_ip_filter200_response_dict = get_iam_v2_ip_filter200_response_instance.to_dict()
# create an instance of GetIamV2IpFilter200Response from a dict
get_iam_v2_ip_filter200_response_form_dict = get_iam_v2_ip_filter200_response.from_dict(get_iam_v2_ip_filter200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


