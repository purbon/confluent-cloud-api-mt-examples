# CdxV1ProviderShareListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_provider_share_list_metadata import CdxV1ProviderShareListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderShareListMetadata from a JSON string
cdx_v1_provider_share_list_metadata_instance = CdxV1ProviderShareListMetadata.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderShareListMetadata.to_json()

# convert the object into a dict
cdx_v1_provider_share_list_metadata_dict = cdx_v1_provider_share_list_metadata_instance.to_dict()
# create an instance of CdxV1ProviderShareListMetadata from a dict
cdx_v1_provider_share_list_metadata_form_dict = cdx_v1_provider_share_list_metadata.from_dict(cdx_v1_provider_share_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


