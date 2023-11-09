# ListCdxV1ProviderSharedResources200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**CdxV1ProviderSharedResourceListMetadata**](CdxV1ProviderSharedResourceListMetadata.md) |  | 
**data** | [**List[ListCdxV1ProviderSharedResources200ResponseAllOfDataInner]**](ListCdxV1ProviderSharedResources200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_cdx_v1_provider_shared_resources200_response import ListCdxV1ProviderSharedResources200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCdxV1ProviderSharedResources200Response from a JSON string
list_cdx_v1_provider_shared_resources200_response_instance = ListCdxV1ProviderSharedResources200Response.from_json(json)
# print the JSON string representation of the object
print ListCdxV1ProviderSharedResources200Response.to_json()

# convert the object into a dict
list_cdx_v1_provider_shared_resources200_response_dict = list_cdx_v1_provider_shared_resources200_response_instance.to_dict()
# create an instance of ListCdxV1ProviderSharedResources200Response from a dict
list_cdx_v1_provider_shared_resources200_response_form_dict = list_cdx_v1_provider_shared_resources200_response.from_dict(list_cdx_v1_provider_shared_resources200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


