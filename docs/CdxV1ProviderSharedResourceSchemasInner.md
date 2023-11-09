# CdxV1ProviderSharedResourceSchemasInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Name of the subject | [optional] 
**version** | **int** | Version number | [optional] 
**id** | **int** | Globally unique identifier of the schema | [optional] 
**schema_type** | **str** | Schema type | [optional] 
**var_schema** | **str** | Schema definition string | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_provider_shared_resource_schemas_inner import CdxV1ProviderSharedResourceSchemasInner

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1ProviderSharedResourceSchemasInner from a JSON string
cdx_v1_provider_shared_resource_schemas_inner_instance = CdxV1ProviderSharedResourceSchemasInner.from_json(json)
# print the JSON string representation of the object
print CdxV1ProviderSharedResourceSchemasInner.to_json()

# convert the object into a dict
cdx_v1_provider_shared_resource_schemas_inner_dict = cdx_v1_provider_shared_resource_schemas_inner_instance.to_dict()
# create an instance of CdxV1ProviderSharedResourceSchemasInner from a dict
cdx_v1_provider_shared_resource_schemas_inner_form_dict = cdx_v1_provider_shared_resource_schemas_inner.from_dict(cdx_v1_provider_shared_resource_schemas_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


