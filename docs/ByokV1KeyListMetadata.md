# ByokV1KeyListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.byok_v1_key_list_metadata import ByokV1KeyListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ByokV1KeyListMetadata from a JSON string
byok_v1_key_list_metadata_instance = ByokV1KeyListMetadata.from_json(json)
# print the JSON string representation of the object
print ByokV1KeyListMetadata.to_json()

# convert the object into a dict
byok_v1_key_list_metadata_dict = byok_v1_key_list_metadata_instance.to_dict()
# create an instance of ByokV1KeyListMetadata from a dict
byok_v1_key_list_metadata_form_dict = byok_v1_key_list_metadata.from_dict(byok_v1_key_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


