# IamV2JwksStatus

The status of the Jwks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwks_status** | **str** | The actual state of the public key data | [optional] 
**jwks_last_refresh_at** | **datetime** | The last successful refresh time for the public key data | [optional] 

## Example

```python
from openapi_client.models.iam_v2_jwks_status import IamV2JwksStatus

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2JwksStatus from a JSON string
iam_v2_jwks_status_instance = IamV2JwksStatus.from_json(json)
# print the JSON string representation of the object
print IamV2JwksStatus.to_json()

# convert the object into a dict
iam_v2_jwks_status_dict = iam_v2_jwks_status_instance.to_dict()
# create an instance of IamV2JwksStatus from a dict
iam_v2_jwks_status_form_dict = iam_v2_jwks_status.from_dict(iam_v2_jwks_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


