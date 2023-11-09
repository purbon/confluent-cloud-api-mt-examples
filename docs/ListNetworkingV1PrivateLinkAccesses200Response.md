# ListNetworkingV1PrivateLinkAccesses200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1PrivateLinkAccessListMetadata**](NetworkingV1PrivateLinkAccessListMetadata.md) |  | 
**data** | [**List[ListNetworkingV1Peerings200ResponseAllOfDataInner]**](ListNetworkingV1Peerings200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_networking_v1_private_link_accesses200_response import ListNetworkingV1PrivateLinkAccesses200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListNetworkingV1PrivateLinkAccesses200Response from a JSON string
list_networking_v1_private_link_accesses200_response_instance = ListNetworkingV1PrivateLinkAccesses200Response.from_json(json)
# print the JSON string representation of the object
print ListNetworkingV1PrivateLinkAccesses200Response.to_json()

# convert the object into a dict
list_networking_v1_private_link_accesses200_response_dict = list_networking_v1_private_link_accesses200_response_instance.to_dict()
# create an instance of ListNetworkingV1PrivateLinkAccesses200Response from a dict
list_networking_v1_private_link_accesses200_response_form_dict = list_networking_v1_private_link_accesses200_response.from_dict(list_networking_v1_private_link_accesses200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


