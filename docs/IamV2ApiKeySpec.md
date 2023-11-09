# IamV2ApiKeySpec

The desired state of the Api Key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | The API key secret. Only provided in &#x60;create&#x60; responses, not in &#x60;get&#x60; or &#x60;list&#x60;. | [optional] [readonly] 
**display_name** | **str** | A human readable name for the API key | [optional] 
**description** | **str** | A human readable description for the API key | [optional] 
**owner** | [**TypedGlobalObjectReference**](TypedGlobalObjectReference.md) |  | [optional] 
**resource** | [**IamV2ApiKeySpecResource**](IamV2ApiKeySpecResource.md) |  | [optional] 

## Example

```python
from openapi_client.models.iam_v2_api_key_spec import IamV2ApiKeySpec

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ApiKeySpec from a JSON string
iam_v2_api_key_spec_instance = IamV2ApiKeySpec.from_json(json)
# print the JSON string representation of the object
print IamV2ApiKeySpec.to_json()

# convert the object into a dict
iam_v2_api_key_spec_dict = iam_v2_api_key_spec_instance.to_dict()
# create an instance of IamV2ApiKeySpec from a dict
iam_v2_api_key_spec_form_dict = iam_v2_api_key_spec.from_dict(iam_v2_api_key_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


