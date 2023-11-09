# GlobalObjectReference

ObjectReference provides information for you to locate the referred object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 

## Example

```python
from openapi_client.models.global_object_reference import GlobalObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalObjectReference from a JSON string
global_object_reference_instance = GlobalObjectReference.from_json(json)
# print the JSON string representation of the object
print GlobalObjectReference.to_json()

# convert the object into a dict
global_object_reference_dict = global_object_reference_instance.to_dict()
# create an instance of GlobalObjectReference from a dict
global_object_reference_form_dict = global_object_reference.from_dict(global_object_reference_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


