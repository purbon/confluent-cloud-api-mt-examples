# BalancerStatusData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**status** | **str** |  | 
**error_code** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**any_uneven_load** | [**Relationship**](Relationship.md) |  | 
**broker_tasks** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.balancer_status_data import BalancerStatusData

# TODO update the JSON string below
json = "{}"
# create an instance of BalancerStatusData from a JSON string
balancer_status_data_instance = BalancerStatusData.from_json(json)
# print the JSON string representation of the object
print BalancerStatusData.to_json()

# convert the object into a dict
balancer_status_data_dict = balancer_status_data_instance.to_dict()
# create an instance of BalancerStatusData from a dict
balancer_status_data_form_dict = balancer_status_data.from_dict(balancer_status_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


