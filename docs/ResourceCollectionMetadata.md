# ResourceCollectionMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** |  | 
**next** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.resource_collection_metadata import ResourceCollectionMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceCollectionMetadata from a JSON string
resource_collection_metadata_instance = ResourceCollectionMetadata.from_json(json)
# print the JSON string representation of the object
print ResourceCollectionMetadata.to_json()

# convert the object into a dict
resource_collection_metadata_dict = resource_collection_metadata_instance.to_dict()
# create an instance of ResourceCollectionMetadata from a dict
resource_collection_metadata_form_dict = resource_collection_metadata.from_dict(resource_collection_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


