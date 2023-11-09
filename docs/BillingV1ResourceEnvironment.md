# BillingV1ResourceEnvironment

The environment associated with this resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the environment. | [optional] 

## Example

```python
from openapi_client.models.billing_v1_resource_environment import BillingV1ResourceEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1ResourceEnvironment from a JSON string
billing_v1_resource_environment_instance = BillingV1ResourceEnvironment.from_json(json)
# print the JSON string representation of the object
print BillingV1ResourceEnvironment.to_json()

# convert the object into a dict
billing_v1_resource_environment_dict = billing_v1_resource_environment_instance.to_dict()
# create an instance of BillingV1ResourceEnvironment from a dict
billing_v1_resource_environment_form_dict = billing_v1_resource_environment.from_dict(billing_v1_resource_environment_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


