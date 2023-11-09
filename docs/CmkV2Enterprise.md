# CmkV2Enterprise

The enterprise cluster type. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Enterprise cluster type.  | 

## Example

```python
from openapi_client.models.cmk_v2_enterprise import CmkV2Enterprise

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2Enterprise from a JSON string
cmk_v2_enterprise_instance = CmkV2Enterprise.from_json(json)
# print the JSON string representation of the object
print CmkV2Enterprise.to_json()

# convert the object into a dict
cmk_v2_enterprise_dict = cmk_v2_enterprise_instance.to_dict()
# create an instance of CmkV2Enterprise from a dict
cmk_v2_enterprise_form_dict = cmk_v2_enterprise.from_dict(cmk_v2_enterprise_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


