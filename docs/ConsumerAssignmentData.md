# ConsumerAssignmentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**consumer_group_id** | **str** |  | 
**consumer_id** | **str** |  | 
**topic_name** | **str** |  | 
**partition_id** | **int** |  | 
**partition** | [**Relationship**](Relationship.md) |  | 
**lag** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.consumer_assignment_data import ConsumerAssignmentData

# TODO update the JSON string below
json = "{}"
# create an instance of ConsumerAssignmentData from a JSON string
consumer_assignment_data_instance = ConsumerAssignmentData.from_json(json)
# print the JSON string representation of the object
print ConsumerAssignmentData.to_json()

# convert the object into a dict
consumer_assignment_data_dict = consumer_assignment_data_instance.to_dict()
# create an instance of ConsumerAssignmentData from a dict
consumer_assignment_data_form_dict = consumer_assignment_data.from_dict(consumer_assignment_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


