# NetworkingV1NetworkLinkEndpointMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | **object** |  | 
**resource_name** | **object** |  | [optional] 
**created_at** | **datetime** | The date and time at which this object was created. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**updated_at** | **datetime** | The date and time at which this object was last updated. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time at which this object was (or will be) deleted. It is represented in RFC3339 format and is in UTC. | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_network_link_endpoint_metadata import NetworkingV1NetworkLinkEndpointMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkEndpointMetadata from a JSON string
networking_v1_network_link_endpoint_metadata_instance = NetworkingV1NetworkLinkEndpointMetadata.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkEndpointMetadata.to_json()

# convert the object into a dict
networking_v1_network_link_endpoint_metadata_dict = networking_v1_network_link_endpoint_metadata_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkEndpointMetadata from a dict
networking_v1_network_link_endpoint_metadata_form_dict = networking_v1_network_link_endpoint_metadata.from_dict(networking_v1_network_link_endpoint_metadata_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


