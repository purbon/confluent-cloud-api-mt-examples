# CmkV2Basic

The basic cluster type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Basic cluster type.  | 

## Example

```python
from openapi_client.models.cmk_v2_basic import CmkV2Basic

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2Basic from a JSON string
cmk_v2_basic_instance = CmkV2Basic.from_json(json)
# print the JSON string representation of the object
print CmkV2Basic.to_json()

# convert the object into a dict
cmk_v2_basic_dict = cmk_v2_basic_instance.to_dict()
# create an instance of CmkV2Basic from a dict
cmk_v2_basic_form_dict = cmk_v2_basic.from_dict(cmk_v2_basic_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


