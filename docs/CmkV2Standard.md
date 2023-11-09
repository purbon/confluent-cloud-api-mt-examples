# CmkV2Standard

The standard cluster type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Standard cluster type.  | 

## Example

```python
from openapi_client.models.cmk_v2_standard import CmkV2Standard

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2Standard from a JSON string
cmk_v2_standard_instance = CmkV2Standard.from_json(json)
# print the JSON string representation of the object
print CmkV2Standard.to_json()

# convert the object into a dict
cmk_v2_standard_dict = cmk_v2_standard_instance.to_dict()
# create an instance of CmkV2Standard from a dict
cmk_v2_standard_form_dict = cmk_v2_standard.from_dict(cmk_v2_standard_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


