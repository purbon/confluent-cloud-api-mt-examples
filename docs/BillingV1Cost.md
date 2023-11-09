# BillingV1Cost

`Cost` objects represent the aggregated billing costs for an organization   Related guide: [Retrieve costs for a range of dates](https://docs.confluent.io/cloud/current/billing/overview.html#retrieve-costs-for-a-range-of-dates).  ## The Costs Model <SchemaDefinition schemaRef=\"#/components/schemas/billing.v1.Cost\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**start_date** | **date** | Start date of time period (inclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. | [optional] 
**end_date** | **date** | End date of time period (exclusive) to retrieve billing costs. It is represented in RFC3339 format and is in UTC. | [optional] 
**granularity** | **str** | Granularity at which each line item is aggregated. | [optional] [default to 'DAILY']
**network_access_type** | **str** | Network access type for the cluster. | [optional] 
**product** | **str** | Product name. | [optional] 
**line_type** | **str** | Type of the line item. | [optional] 
**price** | **float** | Price for the line item in dollars. | [optional] 
**unit** | **str** | Unit of the line item. | [optional] 
**quantity** | **float** | Quantity of the line item. | [optional] 
**original_amount** | **float** | Original amount accrued for this line item. | [optional] 
**discount_amount** | **float** | Amount discounted from the original amount in dollars. | [optional] 
**amount** | **float** | Final amount after deducting discounts. | [optional] 
**resource** | [**BillingV1Resource**](BillingV1Resource.md) |  | [optional] 

## Example

```python
from openapi_client.models.billing_v1_cost import BillingV1Cost

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1Cost from a JSON string
billing_v1_cost_instance = BillingV1Cost.from_json(json)
# print the JSON string representation of the object
print BillingV1Cost.to_json()

# convert the object into a dict
billing_v1_cost_dict = billing_v1_cost_instance.to_dict()
# create an instance of BillingV1Cost from a dict
billing_v1_cost_form_dict = billing_v1_cost.from_dict(billing_v1_cost_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


