# openapi_client.IPAddressesNetworkingV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_networking_v1_ip_addresses**](IPAddressesNetworkingV1Api.md#list_networking_v1_ip_addresses) | **GET** /networking/v1/ip-addresses | List of IP Addresses


# **list_networking_v1_ip_addresses**
> NetworkingV1IpAddressList list_networking_v1_ip_addresses(cloud=cloud, region=region, services=services, address_type=address_type, page_size=page_size, page_token=page_token)

List of IP Addresses

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Related guide: [Use Public Egress IP addresses on Confluent Cloud](https://docs.confluent.io/cloud/current/networking/static-egress-ip-addresses.html)  Retrieve a sorted, filtered, paginated list of all IP Addresses.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.networking_v1_ip_address_list import NetworkingV1IpAddressList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: cloud-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.IPAddressesNetworkingV1Api(api_client)
    cloud = ['[\"GCP\",\"AWS\"]'] # List[str] | Filter the results by exact match for cloud. Pass multiple times to see results matching any of the values. (optional)
    region = ['[\"us-central1\",\"us-east-1\"]'] # List[str] | Filter the results by exact match for region. Pass multiple times to see results matching any of the values. (optional)
    services = ['[\"KAFKA\",\"CONNECT\"]'] # List[str] | Filter the results by exact match for services. Pass multiple times to see results matching any of the values. (optional)
    address_type = ['[\"INGRESS\",\"EGRESS\"]'] # List[str] | Filter the results by exact match for address_type. Pass multiple times to see results matching any of the values. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of IP Addresses
        api_response = api_instance.list_networking_v1_ip_addresses(cloud=cloud, region=region, services=services, address_type=address_type, page_size=page_size, page_token=page_token)
        print("The response of IPAddressesNetworkingV1Api->list_networking_v1_ip_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPAddressesNetworkingV1Api->list_networking_v1_ip_addresses: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | [**List[str]**](str.md)| Filter the results by exact match for cloud. Pass multiple times to see results matching any of the values. | [optional] 
 **region** | [**List[str]**](str.md)| Filter the results by exact match for region. Pass multiple times to see results matching any of the values. | [optional] 
 **services** | [**List[str]**](str.md)| Filter the results by exact match for services. Pass multiple times to see results matching any of the values. | [optional] 
 **address_type** | [**List[str]**](str.md)| Filter the results by exact match for address_type. Pass multiple times to see results matching any of the values. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**NetworkingV1IpAddressList**](NetworkingV1IpAddressList.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

