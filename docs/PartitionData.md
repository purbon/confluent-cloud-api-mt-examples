# PartitionData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**topic_name** | **str** |  | 
**partition_id** | **int** |  | 
**leader** | [**Relationship**](Relationship.md) |  | [optional] 
**replicas** | [**Relationship**](Relationship.md) |  | 
**reassignment** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.partition_data import PartitionData

# TODO update the JSON string below
json = "{}"
# create an instance of PartitionData from a JSON string
partition_data_instance = PartitionData.from_json(json)
# print the JSON string representation of the object
print PartitionData.to_json()

# convert the object into a dict
partition_data_dict = partition_data_instance.to_dict()
# create an instance of PartitionData from a dict
partition_data_form_dict = partition_data.from_dict(partition_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


