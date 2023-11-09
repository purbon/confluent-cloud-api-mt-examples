# IamV2JwksSpec

The desired state of the Jwks

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jwks_status** | **str** | The desired state of the public key data | [optional] 

## Example

```python
from openapi_client.models.iam_v2_jwks_spec import IamV2JwksSpec

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2JwksSpec from a JSON string
iam_v2_jwks_spec_instance = IamV2JwksSpec.from_json(json)
# print the JSON string representation of the object
print IamV2JwksSpec.to_json()

# convert the object into a dict
iam_v2_jwks_spec_dict = iam_v2_jwks_spec_instance.to_dict()
# create an instance of IamV2JwksSpec from a dict
iam_v2_jwks_spec_form_dict = iam_v2_jwks_spec.from_dict(iam_v2_jwks_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


