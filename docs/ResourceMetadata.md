# ResourceMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** |  | 
**resource_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.resource_metadata import ResourceMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceMetadata from a JSON string
resource_metadata_instance = ResourceMetadata.from_json(json)
# print the JSON string representation of the object
print ResourceMetadata.to_json()

# convert the object into a dict
resource_metadata_dict = resource_metadata_instance.to_dict()
# create an instance of ResourceMetadata from a dict
resource_metadata_form_dict = resource_metadata.from_dict(resource_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


