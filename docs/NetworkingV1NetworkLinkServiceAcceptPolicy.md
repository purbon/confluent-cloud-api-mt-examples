# NetworkingV1NetworkLinkServiceAcceptPolicy

List of environments/networks from which connections can be accepted on this network link service. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environments** | **List[str]** | List of environments from which connections can be accepted. All networks win the list of environment will be allowed.  | [optional] 
**networks** | **List[str]** | List of networks from which connections can be accepted.  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_accept_policy import NetworkingV1NetworkLinkServiceAcceptPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceAcceptPolicy from a JSON string
networking_v1_network_link_service_accept_policy_instance = NetworkingV1NetworkLinkServiceAcceptPolicy.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceAcceptPolicy.to_json()

# convert the object into a dict
networking_v1_network_link_service_accept_policy_dict = networking_v1_network_link_service_accept_policy_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceAcceptPolicy from a dict
networking_v1_network_link_service_accept_policy_form_dict = networking_v1_network_link_service_accept_policy.from_dict(networking_v1_network_link_service_accept_policy_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


