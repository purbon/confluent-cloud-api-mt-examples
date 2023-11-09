# GetCdxV1OptIn200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**stream_share_enabled** | **bool** | Enable stream sharing for the organization | [optional] 

## Example

```python
from openapi_client.models.get_cdx_v1_opt_in200_response import GetCdxV1OptIn200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdxV1OptIn200Response from a JSON string
get_cdx_v1_opt_in200_response_instance = GetCdxV1OptIn200Response.from_json(json)
# print the JSON string representation of the object
print GetCdxV1OptIn200Response.to_json()

# convert the object into a dict
get_cdx_v1_opt_in200_response_dict = get_cdx_v1_opt_in200_response_instance.to_dict()
# create an instance of GetCdxV1OptIn200Response from a dict
get_cdx_v1_opt_in200_response_form_dict = get_cdx_v1_opt_in200_response.from_dict(get_cdx_v1_opt_in200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


