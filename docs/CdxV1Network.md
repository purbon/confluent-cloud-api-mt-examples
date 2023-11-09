# CdxV1Network

The shared cluster's network configurations for consumer to setup private link

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [optional] [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [optional] [readonly] 
**id** | **str** | ID is the \&quot;natural identifier\&quot; for an object within its scope/namespace; it is normally unique across time but not space. That is, you can assume that the ID will not be reclaimed and reused after an object is deleted (\&quot;time\&quot;); however, it may collide with IDs for other object &#x60;kinds&#x60; or objects of the same &#x60;kind&#x60; within a different scope/namespace (\&quot;space\&quot;). | [optional] [readonly] 
**metadata** | [**CdxV1NetworkMetadata**](CdxV1NetworkMetadata.md) |  | [optional] 
**kafka_bootstrap_url** | **str** | The kafka cluster bootstrap url | [optional] [readonly] 
**zones** | **List[str]** | The 3 availability zones for this network. They can optionally be specified for AWS networks used with PrivateLink. Otherwise, they are automatically chosen by Confluent Cloud.  On AWS, zones are AWS [AZ IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)  (e.g. use1-az3)  On GCP, zones are GCP [zones](https://cloud.google.com/compute/docs/regions-zones)  (e.g. us-central1-c).  On Azure, zones are Confluent-chosen names (e.g. 1, 2, 3) since Azure does not  have universal zone identifiers.  | [optional] 
**dns_domain** | **str** | The root DNS domain for the network if applicable. | [optional] [readonly] 
**zonal_subdomains** | **Dict[str, str]** | The DNS subdomain for each zone. Present on networks that support PrivateLink. Keys are zones and values are DNS domains.  | [optional] [readonly] 
**cloud** | [**CdxV1NetworkCloud**](CdxV1NetworkCloud.md) |  | [optional] 

## Example

```python
from openapi_client.models.cdx_v1_network import CdxV1Network

# TODO update the JSON string below
json = "{}"
# create an instance of CdxV1Network from a JSON string
cdx_v1_network_instance = CdxV1Network.from_json(json)
# print the JSON string representation of the object
print CdxV1Network.to_json()

# convert the object into a dict
cdx_v1_network_dict = cdx_v1_network_instance.to_dict()
# create an instance of CdxV1Network from a dict
cdx_v1_network_form_dict = cdx_v1_network.from_dict(cdx_v1_network_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


