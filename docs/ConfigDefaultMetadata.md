# ConfigDefaultMetadata

Default value for the metadata to be used during schema registration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | **object** | The metadata properties and their new values | [optional] 

## Example

```python
from openapi_client.models.config_default_metadata import ConfigDefaultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDefaultMetadata from a JSON string
config_default_metadata_instance = ConfigDefaultMetadata.from_json(json)
# print the JSON string representation of the object
print ConfigDefaultMetadata.to_json()

# convert the object into a dict
config_default_metadata_dict = config_default_metadata_instance.to_dict()
# create an instance of ConfigDefaultMetadata from a dict
config_default_metadata_form_dict = config_default_metadata.from_dict(config_default_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


