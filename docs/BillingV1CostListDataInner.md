# BillingV1CostListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**start_date** | **date** | Start date of time period (inclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. | 
**end_date** | **date** | End date of time period (exclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. | 
**granularity** | **str** | Granularity at which each line item is aggregated. | [optional] [default to 'DAILY']
**network_access_type** | **str** | Network access type for the cluster. | [optional] 
**product** | **str** | Product name. | [optional] 
**line_type** | **str** | Type of the line item. | [optional] 
**price** | **float** | Price for the line item in dollars. | [optional] 
**unit** | **str** | Unit of the line item. | 
**quantity** | **float** | Quantity of the line item. | [optional] 
**original_amount** | **float** | Original amount accrued for this line item. | 
**discount_amount** | **float** | Amount discounted from the original amount in dollars. | [optional] 
**amount** | **float** | Final amount after deducting discounts. | [optional] 
**resource** | [**BillingV1Resource**](BillingV1Resource.md) |  | [optional] 

## Example

```python
from openapi_client.models.billing_v1_cost_list_data_inner import BillingV1CostListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1CostListDataInner from a JSON string
billing_v1_cost_list_data_inner_instance = BillingV1CostListDataInner.from_json(json)
# print the JSON string representation of the object
print BillingV1CostListDataInner.to_json()

# convert the object into a dict
billing_v1_cost_list_data_inner_dict = billing_v1_cost_list_data_inner_instance.to_dict()
# create an instance of BillingV1CostListDataInner from a dict
billing_v1_cost_list_data_inner_form_dict = billing_v1_cost_list_data_inner.from_dict(billing_v1_cost_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


