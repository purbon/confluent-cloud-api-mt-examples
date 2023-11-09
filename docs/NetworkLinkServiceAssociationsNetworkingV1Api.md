# openapi_client.NetworkLinkServiceAssociationsNetworkingV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_networking_v1_network_link_service_association**](NetworkLinkServiceAssociationsNetworkingV1Api.md#get_networking_v1_network_link_service_association) | **GET** /networking/v1/network-link-service-associations/{id} | Read a Network Link Service Association
[**list_networking_v1_network_link_service_associations**](NetworkLinkServiceAssociationsNetworkingV1Api.md#list_networking_v1_network_link_service_associations) | **GET** /networking/v1/network-link-service-associations | List of Network Link Service Associations


# **get_networking_v1_network_link_service_association**
> GetNetworkingV1NetworkLinkServiceAssociation200Response get_networking_v1_network_link_service_association(id)

Read a Network Link Service Association

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a network link service association.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_network_link_service_association200_response import GetNetworkingV1NetworkLinkServiceAssociation200Response
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

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NetworkLinkServiceAssociationsNetworkingV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the network link service association.

    try:
        # Read a Network Link Service Association
        api_response = api_instance.get_networking_v1_network_link_service_association(id)
        print("The response of NetworkLinkServiceAssociationsNetworkingV1Api->get_networking_v1_network_link_service_association:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLinkServiceAssociationsNetworkingV1Api->get_networking_v1_network_link_service_association: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the network link service association. | 

### Return type

[**GetNetworkingV1NetworkLinkServiceAssociation200Response**](GetNetworkingV1NetworkLinkServiceAssociation200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Link Service Association. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_networking_v1_network_link_service_associations**
> ListNetworkingV1NetworkLinkServiceAssociations200Response list_networking_v1_network_link_service_associations(spec_network_link_service, environment, status_phase=status_phase, page_size=page_size, page_token=page_token)

List of Network Link Service Associations

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all network link service associations.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.list_networking_v1_network_link_service_associations200_response import ListNetworkingV1NetworkLinkServiceAssociations200Response
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

# Configure HTTP basic authorization: api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NetworkLinkServiceAssociationsNetworkingV1Api(api_client)
    spec_network_link_service = 'nls-abcde' # str | Filter the results by exact match for spec.network_link_service.
    environment = 'env-00000' # str | Filter the results by exact match for environment.
    status_phase = ['[\"READY\",\"PENDING_ACCEPT\"]'] # List[str] | Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Network Link Service Associations
        api_response = api_instance.list_networking_v1_network_link_service_associations(spec_network_link_service, environment, status_phase=status_phase, page_size=page_size, page_token=page_token)
        print("The response of NetworkLinkServiceAssociationsNetworkingV1Api->list_networking_v1_network_link_service_associations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLinkServiceAssociationsNetworkingV1Api->list_networking_v1_network_link_service_associations: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_network_link_service** | **str**| Filter the results by exact match for spec.network_link_service. | 
 **environment** | **str**| Filter the results by exact match for environment. | 
 **status_phase** | [**List[str]**](str.md)| Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListNetworkingV1NetworkLinkServiceAssociations200Response**](ListNetworkingV1NetworkLinkServiceAssociations200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Link Service Association. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

