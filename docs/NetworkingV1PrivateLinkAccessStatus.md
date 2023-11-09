# NetworkingV1PrivateLinkAccessStatus

The status of the Private Link Access

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phase** | **str** | The lifecycle phase of the PrivateLink access configuration:    PROVISIONING: PrivateLink access provisioning is in progress;    READY:  PrivateLink access is ready;    FAILED: PrivateLink access is in a failed state;    DEPROVISIONING: PrivateLink access deprovisioning is in progress;  | [readonly] 
**error_code** | **str** | Error code if PrivateLink access is in a failed state. May be used for programmatic error checking. | [optional] [readonly] 
**error_message** | **str** | Displayable error message if PrivateLink access is in a failed state | [optional] [readonly] 

## Example

```python
from openapi_client.models.networking_v1_private_link_access_status import NetworkingV1PrivateLinkAccessStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAccessStatus from a JSON string
networking_v1_private_link_access_status_instance = NetworkingV1PrivateLinkAccessStatus.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAccessStatus.to_json()

# convert the object into a dict
networking_v1_private_link_access_status_dict = networking_v1_private_link_access_status_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAccessStatus from a dict
networking_v1_private_link_access_status_form_dict = networking_v1_private_link_access_status.from_dict(networking_v1_private_link_access_status_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


