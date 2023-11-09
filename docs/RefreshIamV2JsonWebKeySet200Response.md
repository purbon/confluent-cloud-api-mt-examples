# RefreshIamV2JsonWebKeySet200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**spec** | **object** |  | 
**status** | [**IamV2JwksStatus**](IamV2JwksStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.refresh_iam_v2_json_web_key_set200_response import RefreshIamV2JsonWebKeySet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RefreshIamV2JsonWebKeySet200Response from a JSON string
refresh_iam_v2_json_web_key_set200_response_instance = RefreshIamV2JsonWebKeySet200Response.from_json(json)
# print the JSON string representation of the object
print RefreshIamV2JsonWebKeySet200Response.to_json()

# convert the object into a dict
refresh_iam_v2_json_web_key_set200_response_dict = refresh_iam_v2_json_web_key_set200_response_instance.to_dict()
# create an instance of RefreshIamV2JsonWebKeySet200Response from a dict
refresh_iam_v2_json_web_key_set200_response_form_dict = refresh_iam_v2_json_web_key_set200_response.from_dict(refresh_iam_v2_json_web_key_set200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


