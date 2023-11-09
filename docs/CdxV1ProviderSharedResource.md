# CdxV1ProviderSharedResource

`ProviderSharedResource` object contains details of the data stream (topic, schema registry subjects, sharing metadata) that you have shared through Stream Sharing.   ## The Provider Shared Resources Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.ProviderSharedResource\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CdxV1ProviderSharedResourceMetadata**](CdxV1ProviderSharedResourceMetadata.md) |  | [optional] 
**crn** | **str** | Deprecated please use resources attribute. | [optional] 
**resources** | **List[str]** | List of resource crns that are shared together | [optional] 
**display_name** | **str** | Shared resource display name | [optional] 
**description** | **str** | Description of shared resource | [optional] [readonly] 
**tags** | **List[str]** | list of tags | [optional] [readonly] 
**schemas** | [**List[CdxV1ProviderSharedResourceSchemasInner]**](CdxV1ProviderSharedResourceSchemasInner.md) | List of schemas in JSON format. This field is work in progress and subject to changes. | [optional] [readonly] 
**organization_description** | **str** | Shared resource&#39;s organization description | [optional] 
**organization_contact** | **str** | Email of contact person from the organization | [optional] 
**logo_url** | **str** | Resource logo url | [optional] [readonly] 
**organization_name** | **object** | Organization to which the shared resource belongs. Deprecated | [optional] [readonly] 
**environment_name** | **str** | The environment name of the shared resource. Deprecated | [optional] [readonly] 
**cluster_name** | **str** | The cluster display name of the shared resource. Deprecated | [optional] [readonly] 
**cloud_cluster** | [**EnvScopedObjectReference**](EnvScopedObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_provider_shared_resource import CdxV1ProviderSharedResource

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderSharedResource from a JSON string
cdx_v1_provider_shared_resource_instance = CdxV1ProviderSharedResource.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderSharedResource.to_json()

# convert the object into a dict
cdx_v1_provider_shared_resource_dict = cdx_v1_provider_shared_resource_instance.to_dict()
# create an instance of CdxV1ProviderSharedResource from a dict
cdx_v1_provider_shared_resource_form_dict = cdx_v1_provider_shared_resource.from_dict(cdx_v1_provider_shared_resource_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


