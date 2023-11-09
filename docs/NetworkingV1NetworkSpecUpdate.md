# NetworkingV1NetworkSpecUpdate

The desired state of the Network

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the network | [optional] 
**zones_info** | [**List[NetworkingV1ZoneInfo]**](NetworkingV1ZoneInfo.md) | Cloud provider zones metadata. | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_spec_update import NetworkingV1NetworkSpecUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkSpecUpdate from a JSON string
networking_v1_network_spec_update_instance = NetworkingV1NetworkSpecUpdate.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkSpecUpdate.to_json()

# convert the object into a dict
networking_v1_network_spec_update_dict = networking_v1_network_spec_update_instance.to_dict()
# create an instance of NetworkingV1NetworkSpecUpdate from a dict
networking_v1_network_spec_update_form_dict = networking_v1_network_spec_update.from_dict(networking_v1_network_spec_update_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


