# NetworkingV1PeeringStatus

The status of the Peering

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the peering:    PROVISIONING: peering provisioning is in progress;    PENDING_ACCEPT: peering connection request is pending acceptance by the customer;    READY:  peering is ready;    FAILED: peering is in a failed state;    DEPROVISIONING: peering deprovisioning is in progress;    DISCONNECTED: peering has been disconnected in the cloud provider by the customer;  | [readonly] 
**error_code** | **str** | Error code if peering is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if peering is in a failed state | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_peering_status import NetworkingV1PeeringStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PeeringStatus from a JSON string
networking_v1_peering_status_instance = NetworkingV1PeeringStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PeeringStatus.to_json()

# convert the object into a dict
networking_v1_peering_status_dict = networking_v1_peering_status_instance.to_dict()
# create an instance of NetworkingV1PeeringStatus from a dict
networking_v1_peering_status_form_dict = networking_v1_peering_status.from_dict(networking_v1_peering_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


