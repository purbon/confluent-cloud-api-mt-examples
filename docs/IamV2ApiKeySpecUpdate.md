# IamV2ApiKeySpecUpdate

The desired state of the Api Key

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | A human readable name for the API key | [optional] 
**description** | **str** | A human readable description for the API key | [optional] 

## Example

```python
from openapi_client.models.iam_v2_api_key_spec_update import IamV2ApiKeySpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2ApiKeySpecUpdate from a JSON string
iam_v2_api_key_spec_update_instance = IamV2ApiKeySpecUpdate.from_json(json)
# print the JSON string representation of the object
print IamV2ApiKeySpecUpdate.to_json()

# convert the object into a dict
iam_v2_api_key_spec_update_dict = iam_v2_api_key_spec_update_instance.to_dict()
# create an instance of IamV2ApiKeySpecUpdate from a dict
iam_v2_api_key_spec_update_form_dict = iam_v2_api_key_spec_update.from_dict(iam_v2_api_key_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


