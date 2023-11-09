# NetworkingV1NetworkLinkServiceListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [readonly] 
**metadata** | [**NetworkingV1NetworkLinkServiceMetadata**](NetworkingV1NetworkLinkServiceMetadata.md) |  | 
**spec** | **object** |  | 
**status** | [**NetworkingV1NetworkLinkServiceStatus**](NetworkingV1NetworkLinkServiceStatus.md) |  | 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_list_data_inner import NetworkingV1NetworkLinkServiceListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceListDataInner from a JSON string
networking_v1_network_link_service_list_data_inner_instance = NetworkingV1NetworkLinkServiceListDataInner.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceListDataInner.to_json()

# convert the object into a dict
networking_v1_network_link_service_list_data_inner_dict = networking_v1_network_link_service_list_data_inner_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceListDataInner from a dict
networking_v1_network_link_service_list_data_inner_form_dict = networking_v1_network_link_service_list_data_inner.from_dict(networking_v1_network_link_service_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


