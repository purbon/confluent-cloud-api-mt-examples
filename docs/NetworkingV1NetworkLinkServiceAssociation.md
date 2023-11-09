# NetworkingV1NetworkLinkServiceAssociation

List of incoming Network Link Enpoints associated with the Network Link Service.   Related guide: [Network Linking Overview](https://docs.confluent.io/cloud/current/networking/network-linking.html).  ## The Network Link Service Associations Model <SchemaDefinition schemaRef=\"#/components/schemas/networking.v1.NetworkLinkServiceAssociation\" />

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**NetworkingV1NetworkLinkServiceAssociationMetadata**](NetworkingV1NetworkLinkServiceAssociationMetadata.md) |  | [optional] 
**spec** | [**NetworkingV1NetworkLinkServiceAssociationSpec**](NetworkingV1NetworkLinkServiceAssociationSpec.md) |  | [optional] 
**status** | [**NetworkingV1NetworkLinkServiceAssociationStatus**](NetworkingV1NetworkLinkServiceAssociationStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.networking_v1_network_link_service_association import NetworkingV1NetworkLinkServiceAssociation

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1NetworkLinkServiceAssociation from a JSON string
networking_v1_network_link_service_association_instance = NetworkingV1NetworkLinkServiceAssociation.from_json(json)
# print the JSON string representation of the object
print NetworkingV1NetworkLinkServiceAssociation.to_json()

# convert the object into a dict
networking_v1_network_link_service_association_dict = networking_v1_network_link_service_association_instance.to_dict()
# create an instance of NetworkingV1NetworkLinkServiceAssociation from a dict
networking_v1_network_link_service_association_form_dict = networking_v1_network_link_service_association.from_dict(networking_v1_network_link_service_association_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


