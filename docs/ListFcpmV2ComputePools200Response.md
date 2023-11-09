# ListFcpmV2ComputePools200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**FcpmV2ComputePoolListMetadata**](FcpmV2ComputePoolListMetadata.md) |  | 
**data** | [**List[ListFcpmV2ComputePools200ResponseAllOfDataInner]**](ListFcpmV2ComputePools200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_fcpm_v2_compute_pools200_response import ListFcpmV2ComputePools200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListFcpmV2ComputePools200Response from a JSON string
list_fcpm_v2_compute_pools200_response_instance = ListFcpmV2ComputePools200Response.from_json(json)
# print the JSON string representation of the object
print ListFcpmV2ComputePools200Response.to_json()

# convert the object into a dict
list_fcpm_v2_compute_pools200_response_dict = list_fcpm_v2_compute_pools200_response_instance.to_dict()
# create an instance of ListFcpmV2ComputePools200Response from a dict
list_fcpm_v2_compute_pools200_response_form_dict = list_fcpm_v2_compute_pools200_response.from_dict(list_fcpm_v2_compute_pools200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


