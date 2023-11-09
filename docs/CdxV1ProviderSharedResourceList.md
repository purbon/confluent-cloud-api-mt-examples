# CdxV1ProviderSharedResourceList

`ProviderSharedResource` object contains details of the data stream (topic, schema registry subjects, sharing metadata) that you have shared through Stream Sharing.   ## The Provider Shared Resources Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ProviderSharedResource\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**CdxV1ProviderSharedResourceListMetadata**](CdxV1ProviderSharedResourceListMetadata.md) |  | 
**data** | [**List[CdxV1ProviderSharedResourceListDataInner]**](CdxV1ProviderSharedResourceListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.cdx_v1_provider_shared_resource_list import CdxV1ProviderSharedResourceList

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderSharedResourceList from a JSON string
cdx_v1_provider_shared_resource_list_instance = CdxV1ProviderSharedResourceList.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderSharedResourceList.to_json()

# convert the object into a dict
cdx_v1_provider_shared_resource_list_dict = cdx_v1_provider_shared_resource_list_instance.to_dict()
# create an instance of CdxV1ProviderSharedResourceList from a dict
cdx_v1_provider_shared_resource_list_form_dict = cdx_v1_provider_shared_resource_list.from_dict(cdx_v1_provider_shared_resource_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


