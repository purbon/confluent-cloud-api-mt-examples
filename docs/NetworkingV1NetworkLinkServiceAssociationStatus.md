# NetworkingV1NetworkLinkServiceAssociationStatus

The status of the Network Link Service Association

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the network link endpoint:    PROVISIONING: network link endpoint provisioning is in progress;    PENDING_ACCEPT: network link endpoint request is pending acceptance by the the owner of the target;    READY:  network link endpoint is ready;    FAILED: network link endpoint is in a failed state;    DEPROVISIONING: network link endpoint deprovisioning is in progress;    EXPIRED: network link endpoint request is expired, can only be deleted;    DISCONNECTED: network link endpoint is in a disconnected state, target owner has removed the permissions;    DISCONNECTING: network link endpoint disconnection is in progress;    INACTIVE: network link endpoint is created, but not active since there are no clusters in the network;  | [readonly] 
**error_code** | **str** | Error code if network link is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if network link is in a failed state | [optional] [readonly] 
**expires_at** | **datetime** | The date and time when the request expires if it is not accepted by the target network admin. | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_association_status import NetworkingV1NetworkLinkServiceAssociationStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceAssociationStatus from a JSON string
networking_v1_network_link_service_association_status_instance = NetworkingV1NetworkLinkServiceAssociationStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceAssociationStatus.to_json()

# convert the object into a dict
networking_v1_network_link_service_association_status_dict = networking_v1_network_link_service_association_status_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceAssociationStatus from a dict
networking_v1_network_link_service_association_status_form_dict = networking_v1_network_link_service_association_status.from_dict(networking_v1_network_link_service_association_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


