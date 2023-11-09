# NetworkingV1IpAddressList

IP Addresses  Related guide: [Use Public Egress IP Addresses on Confluent Cloud](https://docs.confluent.io/cloud/current/networking/static-egress-ip-addresses.html)  ## The IP Addresses Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.IpAddress\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1IpAddressListMetadata**](NetworkingV1IpAddressListMetadata.md) |  | 
**data** | [**List[NetworkingV1IpAddressListDataInner]**](NetworkingV1IpAddressListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_ip_address_list import NetworkingV1IpAddressList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1IpAddressList from a JSON string
networking_v1_ip_address_list_instance = NetworkingV1IpAddressList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1IpAddressList.to_json()

# convert the object into a dict
networking_v1_ip_address_list_dict = networking_v1_ip_address_list_instance.to_dict()
# create an instance of NetworkingV1IpAddressList from a dict
networking_v1_ip_address_list_form_dict = networking_v1_ip_address_list.from_dict(networking_v1_ip_address_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


