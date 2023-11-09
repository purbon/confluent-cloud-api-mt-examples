# ClusterData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceMetadata**](ResourceMetadata.md) |  | 
**cluster_id** | **str** |  | 
**controller** | [**Relationship**](Relationship.md) |  | [optional] 
**acls** | [**Relationship**](Relationship.md) |  | 
**brokers** | [**Relationship**](Relationship.md) |  | 
**broker_configs** | [**Relationship**](Relationship.md) |  | 
**consumer_groups** | [**Relationship**](Relationship.md) |  | 
**topics** | [**Relationship**](Relationship.md) |  | 
**partition_reassignments** | [**Relationship**](Relationship.md) |  | 

## Example

```python
from openapi_client.models.cluster_data import ClusterData

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterData from a JSON string
cluster_data_instance = ClusterData.from_json(json)
# print the JSON string representation of the object
print ClusterData.to_json()

# convert the object into a dict
cluster_data_dict = cluster_data_instance.to_dict()
# create an instance of ClusterData from a dict
cluster_data_form_dict = cluster_data.from_dict(cluster_data_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


