# CdxV1SharedGroup

The shared consumer group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The resource kind | 
**group_prefix** | **str** | The consumer group prefix | 

## Example

```python
from openapi_client.models.cdx_v1_shared_group import CdxV1SharedGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1SharedGroup from a JSON string
cdx_v1_shared_group_instance = CdxV1SharedGroup.from_json(json)
# print the JSON string representation of the object
print CdxV1SharedGroup.to_json()

# convert the object into a dict
cdx_v1_shared_group_dict = cdx_v1_shared_group_instance.to_dict()
# create an instance of CdxV1SharedGroup from a dict
cdx_v1_shared_group_form_dict = cdx_v1_shared_group.from_dict(cdx_v1_shared_group_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


