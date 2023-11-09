# BusinessMetadataResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The business metadata name | [optional] 
**attributes** | **object** | The business metadata attributes | [optional] 
**entity_type** | **str** | The entity type | [optional] 
**entity_name** | **str** | The qualified name of the entity | [optional] 
**error** | [**ErrorMessage**](ErrorMessage.md) |  | [optional] 

## Example

```python
from openapi_client.models.business_metadata_response import BusinessMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessMetadataResponse from a JSON string
business_metadata_response_instance = BusinessMetadataResponse.from_json(json)
# print the JSON string representation of the object
print BusinessMetadataResponse.to_json()

# convert the object into a dict
business_metadata_response_dict = business_metadata_response_instance.to_dict()
# create an instance of BusinessMetadataResponse from a dict
business_metadata_response_form_dict = business_metadata_response.from_dict(business_metadata_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


