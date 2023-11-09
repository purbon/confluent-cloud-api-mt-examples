# BillingV1Environment

The details of the environment for a given resource. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the environment. | [optional] 

## Example

```python
from openapi_client.models.billing_v1_environment import BillingV1Environment

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1Environment from a JSON string
billing_v1_environment_instance = BillingV1Environment.from_json(json)
# print the JSON string representation of the object
print BillingV1Environment.to_json()

# convert the object into a dict
billing_v1_environment_dict = billing_v1_environment_instance.to_dict()
# create an instance of BillingV1Environment from a dict
billing_v1_environment_form_dict = billing_v1_environment.from_dict(billing_v1_environment_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


