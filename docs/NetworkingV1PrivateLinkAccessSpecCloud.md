# NetworkingV1PrivateLinkAccessSpecCloud

The cloud-specific PrivateLink details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLink kind type. | 
**account** | **str** | The AWS account ID | 
**subscription** | **str** | The Azure subscription ID for the account containing the VNets you want to connect from using Azure Private Link. You can find your Azure subscription ID in the subscription section of your [Microsoft Azure Portal](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade). Must be a valid **32 character UUID string**.  | 
**project** | **str** | The GCP project ID for the account containing the VPCs that you want to connect from using Private Service Connect. You can find your Google Cloud Project ID under **Project ID** section of your [Google Cloud Console dashboard](https://console.cloud.google.com/home/dashboard).  | 

## Example

```python
from openapi_client.models.networking_v1_private_link_access_spec_cloud import NetworkingV1PrivateLinkAccessSpecCloud

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1PrivateLinkAccessSpecCloud from a JSON string
networking_v1_private_link_access_spec_cloud_instance = NetworkingV1PrivateLinkAccessSpecCloud.from_json(json)
# print the JSON string representation of the object
print NetworkingV1PrivateLinkAccessSpecCloud.to_json()

# convert the object into a dict
networking_v1_private_link_access_spec_cloud_dict = networking_v1_private_link_access_spec_cloud_instance.to_dict()
# create an instance of NetworkingV1PrivateLinkAccessSpecCloud from a dict
networking_v1_private_link_access_spec_cloud_form_dict = networking_v1_private_link_access_spec_cloud.from_dict(networking_v1_private_link_access_spec_cloud_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


