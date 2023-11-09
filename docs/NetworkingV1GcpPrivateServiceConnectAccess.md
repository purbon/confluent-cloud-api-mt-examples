# NetworkingV1GcpPrivateServiceConnectAccess

GCP Private Service Connect access configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | PrivateLink kind type. | 
**project** | **str** | The GCP project ID for the account containing the VPCs that you want to connect from using Private Service Connect. You can find your Google Cloud Project ID under **Project ID** section of your [Google Cloud Console dashboard](https://console.cloud.google.com/home/dashboard).  | 

## Example

```python
from openapi_client.models.networking_v1_gcp_private_service_connect_access import NetworkingV1GcpPrivateServiceConnectAccess

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkingV1GcpPrivateServiceConnectAccess from a JSON string
networking_v1_gcp_private_service_connect_access_instance = NetworkingV1GcpPrivateServiceConnectAccess.from_json(json)
# print the JSON string representation of the object
print NetworkingV1GcpPrivateServiceConnectAccess.to_json()

# convert the object into a dict
networking_v1_gcp_private_service_connect_access_dict = networking_v1_gcp_private_service_connect_access_instance.to_dict()
# create an instance of NetworkingV1GcpPrivateServiceConnectAccess from a dict
networking_v1_gcp_private_service_connect_access_form_dict = networking_v1_gcp_private_service_connect_access.from_dict(networking_v1_gcp_private_service_connect_access_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


