# NetworkingV1NetworkLinkServiceAssociationList

List of incoming Network Link Enpoints associated with the Network Link Service.   Related guide: [Network Linking Overview](https://docs.confluent.io/cloud/current/networking/network-linking.html).  ## The Network Link Service Associations Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.NetworkLinkServiceAssociation\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**NetworkingV1NetworkLinkServiceAssociationListMetadata**](NetworkingV1NetworkLinkServiceAssociationListMetadata.md) |  | 
**data** | [**List[NetworkingV1NetworkLinkServiceAssociationListDataInner]**](NetworkingV1NetworkLinkServiceAssociationListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_association_list import NetworkingV1NetworkLinkServiceAssociationList

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceAssociationList from a JSON string
networking_v1_network_link_service_association_list_instance = NetworkingV1NetworkLinkServiceAssociationList.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceAssociationList.to_json()

# convert the object into a dict
networking_v1_network_link_service_association_list_dict = networking_v1_network_link_service_association_list_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceAssociationList from a dict
networking_v1_network_link_service_association_list_form_dict = networking_v1_network_link_service_association_list.from_dict(networking_v1_network_link_service_association_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


