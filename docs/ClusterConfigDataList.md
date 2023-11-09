# ClusterConfigDataList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** |  | 
**metadata** | [**ResourceCollectionMetadata**](ResourceCollectionMetadata.md) |  | 
**data** | [**List[ClusterConfigData]**](ClusterConfigData.md) |  | 

## Example

```python
from openapi_client.models.cluster_config_data_list import ClusterConfigDataList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterConfigDataList from a JSON string
cluster_config_data_list_instance = ClusterConfigDataList.from_json(json)
# print the JSON string representation of the object
print ClusterConfigDataList.to_json()

# convert the object into a dict
cluster_config_data_list_dict = cluster_config_data_list_instance.to_dict()
# create an instance of ClusterConfigDataList from a dict
cluster_config_data_list_form_dict = cluster_config_data_list.from_dict(cluster_config_data_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


