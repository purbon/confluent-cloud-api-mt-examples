# SdV1SourceCodeObject

A object containing pipeline's source code definition.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | A list of KSQL statements that defines a pipeline. | 

## Example

```python
from openapi_client.models.sd_v1_source_code_object import SdV1SourceCodeObject

# TODO update the JSON string below
json = "{}"
# create an instance of SdV1SourceCodeObject from a JSON string
sd_v1_source_code_object_instance = SdV1SourceCodeObject.from_json(json)
# print the JSON string representation of the object
print SdV1SourceCodeObject.to_json()

# convert the object into a dict
sd_v1_source_code_object_dict = sd_v1_source_code_object_instance.to_dict()
# create an instance of SdV1SourceCodeObject from a dict
sd_v1_source_code_object_form_dict = sd_v1_source_code_object.from_dict(sd_v1_source_code_object_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


