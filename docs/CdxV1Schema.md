# CdxV1Schema

Schema

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
from openapi_client.models.cdx_v1_schema import CdxV1Schema

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1Schema from a JSON string
cdx_v1_schema_instance = CdxV1Schema.from_json(json)
# print the JSON string representation of the object
print CdxV1Schema.to_json()

# convert the object into a dict
cdx_v1_schema_dict = cdx_v1_schema_instance.to_dict()
# create an instance of CdxV1Schema from a dict
cdx_v1_schema_form_dict = cdx_v1_schema.from_dict(cdx_v1_schema_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


