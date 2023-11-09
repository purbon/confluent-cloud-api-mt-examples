# BusinessMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_name** | **str** | The business metadata name | [optional] 
**attributes** | **object** | The business metadata attributes | [optional] 
**entity_type** | **str** | The entity type | [optional] 
**entity_name** | **str** | The qualified name of the entity | [optional] 

## Example

```python
from openapi_client.models.business_metadata import BusinessMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessMetadata from a JSON string
business_metadata_instance = BusinessMetadata.from_json(json)
# print the JSON string representation of the object
print BusinessMetadata.to_json()

# convert the object into a dict
business_metadata_dict = business_metadata_instance.to_dict()
# create an instance of BusinessMetadata from a dict
business_metadata_form_dict = business_metadata.from_dict(business_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


