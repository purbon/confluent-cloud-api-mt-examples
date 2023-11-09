# BillingV1Resource

The resource associated with this object. The resource can be one of Kafka Cluster ID (example: lkc-12345), Connector ID (example:     lcc-12345), Schema Registry Cluster ID (example: lsrc-12345), or ksqlDB Cluster ID (example: lksqlc-12345). May be null or omitted if not associated with a resource. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the resource. | [optional] 
**display_name** | **str** | Display name of the resource. | [optional] 
**environment** | [**BillingV1ResourceEnvironment**](BillingV1ResourceEnvironment.md) |  | [optional] 

## Example

```python
from openapi_client.models.billing_v1_resource import BillingV1Resource

# TODO update the JSON string below
json = "{}"
# create an instance of BillingV1Resource from a JSON string
billing_v1_resource_instance = BillingV1Resource.from_json(json)
# print the JSON string representation of the object
print BillingV1Resource.to_json()

# convert the object into a dict
billing_v1_resource_dict = billing_v1_resource_instance.to_dict()
# create an instance of BillingV1Resource from a dict
billing_v1_resource_form_dict = billing_v1_resource.from_dict(billing_v1_resource_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


