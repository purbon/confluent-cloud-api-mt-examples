# BillingV1CostListMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **object** |  | [optional] 
**last** | **object** |  | [optional] 
**prev** | **object** |  | [optional] 
**next** | **object** |  | [optional] 
**total_size** | **int** | Number of records in the full result set. This response may be paginated and have a smaller number of records. | [optional] 

## Example

```python
from openapi_client.models.billing_v1_cost_list_metadata import BillingV1CostListMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1CostListMetadata from a JSON string
billing_v1_cost_list_metadata_instance = BillingV1CostListMetadata.from_json(json)
# print the JSON string representation of the object
print BillingV1CostListMetadata.to_json()

# convert the object into a dict
billing_v1_cost_list_metadata_dict = billing_v1_cost_list_metadata_instance.to_dict()
# create an instance of BillingV1CostListMetadata from a dict
billing_v1_cost_list_metadata_form_dict = billing_v1_cost_list_metadata.from_dict(billing_v1_cost_list_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


