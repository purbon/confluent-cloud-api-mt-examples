# IamV2JwksObject

`JWKS` contains the published keys for the given OpenIDProvider

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kty** | **str** | Specifies the cryptographic algorithm family used with the key | 
**kid** | **str** | Specifies the key-id issued by the OpenIDProvider for the particular tenant | 
**alg** | **str** | Specifies the algorithm to be used to generate the public key | 
**use** | **str** | Specifies the intended usage of the key | [optional] 
**n** | **str** | Specifies the modulus of the RSA public key. Represented as a Base64urlUInt-encoded value | [optional] 
**e** | **str** | Specifies the exponent of the RSA public key. | [optional] 

## Example

```python
from openapi_client.models.iam_v2_jwks_object import IamV2JwksObject

# TODO update the JSON string below
json = "{}"
# create an instance of IamV2JwksObject from a JSON string
iam_v2_jwks_object_instance = IamV2JwksObject.from_json(json)
# print the JSON string representation of the object
print IamV2JwksObject.to_json()

# convert the object into a dict
iam_v2_jwks_object_dict = iam_v2_jwks_object_instance.to_dict()
# create an instance of IamV2JwksObject from a dict
iam_v2_jwks_object_form_dict = iam_v2_jwks_object.from_dict(iam_v2_jwks_object_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


