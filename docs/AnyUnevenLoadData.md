# AnyUnevenLoadData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**status** | **str** |  | 
**previous_status** | **str** |  | 
**status_updated_at** | **datetime** | The date and time at which this task was created. | [readonly] 
**previous_status_updated_at** | **datetime** | The date and time at which this task was created. | [readonly] 
**error_code** | **int** |  | [optional] 
**error_message** | **str** |  | [optional] 
**broker_tasks** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.any_uneven_load_data import AnyUnevenLoadData

# TODO update the JSON string below
json = "{}"
# create an instance of AnyUnevenLoadData from a JSON string
any_uneven_load_data_instance = AnyUnevenLoadData.from_json(json)
# print the JSON string representation of the object
print AnyUnevenLoadData.to_json()

# convert the object into a dict
any_uneven_load_data_dict = any_uneven_load_data_instance.to_dict()
# create an instance of AnyUnevenLoadData from a dict
any_uneven_load_data_form_dict = any_uneven_load_data.from_dict(any_uneven_load_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


