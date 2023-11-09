# NetworkingV1PeeringSpec

The desired state of the Peering

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The name of the peering | [optional] 
**cloud** | [**NetworkingV1PeeringSpecCloud**](NetworkingV1PeeringSpecCloud.md) |  | [optional] 
**environment** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**network** | [**ObjectReference**](ObjectReference.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_peering_spec import NetworkingV1PeeringSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PeeringSpec from a JSON string
networking_v1_peering_spec_instance = NetworkingV1PeeringSpec.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PeeringSpec.to_json()

# convert the object into a dict
networking_v1_peering_spec_dict = networking_v1_peering_spec_instance.to_dict()
# create an instance of NetworkingV1PeeringSpec from a dict
networking_v1_peering_spec_form_dict = networking_v1_peering_spec.from_dict(networking_v1_peering_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


