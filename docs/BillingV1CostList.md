# BillingV1CostList

`Cost` objects represent the aggregated billing costs for an organization   Related guide: [Retrieve costs for a range of dates](https://docs.confluent.io/cloud/current/billing/overview.html#retrieve-costs-for-a-range-of-dates).  ## The Costs Model <SchemaDefinition schemaRef=\"#/components/schemas/billing.v1.Cost\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**BillingV1CostListMetadata**](BillingV1CostListMetadata.md) |  | 
**data** | [**List[BillingV1CostListDataInner]**](BillingV1CostListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.billing_v1_cost_list import BillingV1CostList

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1CostList from a JSON string
billing_v1_cost_list_instance = BillingV1CostList.from_json(json)
# print the JSON string representation of the object
print BillingV1CostList.to_json()

# convert the object into a dict
billing_v1_cost_list_dict = billing_v1_cost_list_instance.to_dict()
# create an instance of BillingV1CostList from a dict
billing_v1_cost_list_form_dict = billing_v1_cost_list.from_dict(billing_v1_cost_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


