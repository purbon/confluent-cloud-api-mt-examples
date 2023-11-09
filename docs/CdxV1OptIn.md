# CdxV1OptIn

Stream sharing opt in options  ## The Opt Ins Model <SchemaDefinition schemaRef=\"#/components/schemas/cdx.v1.OptIn\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**stream_share_enabled** | **bool** | Enable stream sharing for the organization | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_opt_in import CdxV1OptIn

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1OptIn from a JSON string
cdx_v1_opt_in_instance = CdxV1OptIn.from_json(json)
# print the JSON string representation of the object
print CdxV1OptIn.to_json()

# convert the object into a dict
cdx_v1_opt_in_dict = cdx_v1_opt_in_instance.to_dict()
# create an instance of CdxV1OptIn from a dict
cdx_v1_opt_in_form_dict = cdx_v1_opt_in.from_dict(cdx_v1_opt_in_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


