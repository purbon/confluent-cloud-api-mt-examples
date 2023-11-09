# ObjectReference

ObjectReference provides information for you to locate the referred object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the referred resource | 
**environment** | **str** | Environment of the referred resource, if env-scoped | [optional] 
**related** | **str** | API URL for accessing or modifying the referred object | [readonly] 
**resource_name** | **str** | CRN reference to the referred resource | [readonly] 
**api_version** | **str** | API group and version of the referred resource | [optional] [readonly] 
**kind** | **str** | Kind of the referred resource | [optional] [readonly] 

## Example

```python
from openapi_client.models.object_reference import ObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectReference from a JSON string
object_reference_instance = ObjectReference.from_json(json)
# print the JSON string representation of the object
print ObjectReference.to_json()

# convert the object into a dict
object_reference_dict = object_reference_instance.to_dict()
# create an instance of ObjectReference from a dict
object_reference_form_dict = object_reference.from_dict(object_reference_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


