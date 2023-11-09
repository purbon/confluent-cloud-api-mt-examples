# ClusterConfig

Cluster Config

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_schemas** | **int** | Maximum number of registered schemas allowed | [optional] 
**max_requests_per_sec** | **int** | Maximum number of allowed requests per second | [optional] 

## Example

```python
from openapi_client.models.cluster_config import ClusterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterConfig from a JSON string
cluster_config_instance = ClusterConfig.from_json(json)
# print the JSON string representation of the object
print ClusterConfig.to_json()

# convert the object into a dict
cluster_config_dict = cluster_config_instance.to_dict()
# create an instance of ClusterConfig from a dict
cluster_config_form_dict = cluster_config.from_dict(cluster_config_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


