# ObjectMeta

ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **str** | Self is a Uniform Resource Locator (URL) at which an object can be addressed. This URL encodes the service location, API version, and other particulars necessary to locate the resource at a point in time | [readonly] 
**resource_name** | **str** | Resource Name is a Uniform Resource Identifier (URI) that is globally unique across space and time. It is represented as a Confluent Resource Name | [optional] [readonly] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.object_meta import ObjectMeta

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMeta from a JSON string
object_meta_instance = ObjectMeta.from_json(json)
# print the JSON string representation of the object
print ObjectMeta.to_json()

# convert the object into a dict
object_meta_dict = object_meta_instance.to_dict()
# create an instance of ObjectMeta from a dict
object_meta_form_dict = object_meta.from_dict(object_meta_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


