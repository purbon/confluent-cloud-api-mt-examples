# ReassignmentData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**topic_name** | **str** |  | 
**partition_id** | **int** |  | 
**adding_replicas** | **List[int]** |  | 
**removing_replicas** | **List[int]** |  | 
**replicas** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.reassignment_data import ReassignmentData

# TODO update the JSON string below
json = "{}"
# create an instance of ReassignmentData from a JSON string
reassignment_data_instance = ReassignmentData.from_json(json)
# print the JSON string representation of the object
print ReassignmentData.to_json()

# convert the object into a dict
reassignment_data_dict = reassignment_data_instance.to_dict()
# create an instance of ReassignmentData from a dict
reassignment_data_form_dict = reassignment_data.from_dict(reassignment_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


