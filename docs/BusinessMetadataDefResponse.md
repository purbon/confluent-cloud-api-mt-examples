# BusinessMetadataDefResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | The category | [optional] 
**guid** | **str** | The internal guid | [optional] 
**created_by** | **str** | The creator | [optional] 
**updated_by** | **str** | The updater | [optional] 
**create_time** | **int** | The create time | [optional] 
**update_time** | **int** | The update time | [optional] 
**version** | **int** | The version | [optional] 
**name** | **str** | The name | [optional] 
**description** | **str** | The description | [optional] 
**type_version** | **str** | The type version | [optional] 
**service_type** | **str** | The service type | [optional] 
**options** | **Dict[str, str]** | The options | [optional] 
**attribute_defs** | [**List[AttributeDef]**](AttributeDef.md) | The attribute definitions | [optional] 
**error** | [**ErrorMessage**](ErrorMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.business_metadata_def_response import BusinessMetadataDefResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessMetadataDefResponse from a JSON string
business_metadata_def_response_instance = BusinessMetadataDefResponse.from_json(json)
# print the JSON string representation of the object
print BusinessMetadataDefResponse.to_json()

# convert the object into a dict
business_metadata_def_response_dict = business_metadata_def_response_instance.to_dict()
# create an instance of BusinessMetadataDefResponse from a dict
business_metadata_def_response_form_dict = business_metadata_def_response.from_dict(business_metadata_def_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


