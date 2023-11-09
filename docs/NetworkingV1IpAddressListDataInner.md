# NetworkingV1IpAddressListDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**ip_prefix** | **str** | The IP Address range. | [optional] 
**cloud** | **str** | The cloud service provider in which the address exists. | [optional] 
**region** | **str** | The region/location where the IP Address is in use. | [optional] 
**services** | **List[str]** | The service types that will use the address. | [optional] 
**address_type** | **str** | Whether the address is used for egress or ingress. | [optional] 

## Example

```python
from openapi_client.models.networking_v1_ip_address_list_data_inner import NetworkingV1IpAddressListDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1IpAddressListDataInner from a JSON string
networking_v1_ip_address_list_data_inner_instance = NetworkingV1IpAddressListDataInner.from_json(json)
# print the JSON string representation of the object
print NetworkingV1IpAddressListDataInner.to_json()

# convert the object into a dict
networking_v1_ip_address_list_data_inner_dict = networking_v1_ip_address_list_data_inner_instance.to_dict()
# create an instance of NetworkingV1IpAddressListDataInner from a dict
networking_v1_ip_address_list_data_inner_form_dict = networking_v1_ip_address_list_data_inner.from_dict(networking_v1_ip_address_list_data_inner_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


