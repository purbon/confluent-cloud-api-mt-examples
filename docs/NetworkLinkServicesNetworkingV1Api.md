# openapi_client.NetworkLinkServicesNetworkingV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_networking_v1_network_link_service**](NetworkLinkServicesNetworkingV1Api.md#create_networking_v1_network_link_service) | **POST** /networking/v1/network-link-services | Create a Network Link Service
[**delete_networking_v1_network_link_service**](NetworkLinkServicesNetworkingV1Api.md#delete_networking_v1_network_link_service) | **DELETE** /networking/v1/network-link-services/{id} | Delete a Network Link Service
[**get_networking_v1_network_link_service**](NetworkLinkServicesNetworkingV1Api.md#get_networking_v1_network_link_service) | **GET** /networking/v1/network-link-services/{id} | Read a Network Link Service
[**list_networking_v1_network_link_services**](NetworkLinkServicesNetworkingV1Api.md#list_networking_v1_network_link_services) | **GET** /networking/v1/network-link-services | List of Network Link Services
[**update_networking_v1_network_link_service**](NetworkLinkServicesNetworkingV1Api.md#update_networking_v1_network_link_service) | **PATCH** /networking/v1/network-link-services/{id} | Update a Network Link Service


# **create_networking_v1_network_link_service**
> CreateNetworkingV1NetworkLinkService202Response create_networking_v1_network_link_service(create_networking_v1_network_link_service_request=create_networking_v1_network_link_service_request)

Create a Network Link Service

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a network link service.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.create_networking_v1_network_link_service202_response import CreateNetworkingV1NetworkLinkService202Response
from openapi_client.models.create_networking_v1_network_link_service_request import CreateNetworkingV1NetworkLinkServiceRequest
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
    api_instance = openapi_client.NetworkLinkServicesNetworkingV1Api(api_client)
    create_networking_v1_network_link_service_request = openapi_client.CreateNetworkingV1NetworkLinkServiceRequest() # CreateNetworkingV1NetworkLinkServiceRequest |  (optional)

    try:
        # Create a Network Link Service
        api_response = api_instance.create_networking_v1_network_link_service(create_networking_v1_network_link_service_request=create_networking_v1_network_link_service_request)
        print("The response of NetworkLinkServicesNetworkingV1Api->create_networking_v1_network_link_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLinkServicesNetworkingV1Api->create_networking_v1_network_link_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_networking_v1_network_link_service_request** | [**CreateNetworkingV1NetworkLinkServiceRequest**](CreateNetworkingV1NetworkLinkServiceRequest.md)|  | [optional] 

### Return type

[**CreateNetworkingV1NetworkLinkService202Response**](CreateNetworkingV1NetworkLinkService202Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Network Link Service is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - NetworkLinkService resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_networking_v1_network_link_service**
> delete_networking_v1_network_link_service(environment, id)

Delete a Network Link Service

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a network link service.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
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
    api_instance = openapi_client.NetworkLinkServicesNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the network link service.

    try:
        # Delete a Network Link Service
        api_instance.delete_networking_v1_network_link_service(environment, id)
    except Exception as e:
        print("Exception when calling NetworkLinkServicesNetworkingV1Api->delete_networking_v1_network_link_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the network link service. | 

### Return type

void (empty response body)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A Network Link Service is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_networking_v1_network_link_service**
> GetNetworkingV1NetworkLinkService200Response get_networking_v1_network_link_service(environment, id)

Read a Network Link Service

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a network link service.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_network_link_service200_response import GetNetworkingV1NetworkLinkService200Response
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
    api_instance = openapi_client.NetworkLinkServicesNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the network link service.

    try:
        # Read a Network Link Service
        api_response = api_instance.get_networking_v1_network_link_service(environment, id)
        print("The response of NetworkLinkServicesNetworkingV1Api->get_networking_v1_network_link_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLinkServicesNetworkingV1Api->get_networking_v1_network_link_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the network link service. | 

### Return type

[**GetNetworkingV1NetworkLinkService200Response**](GetNetworkingV1NetworkLinkService200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Link Service. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_networking_v1_network_link_services**
> ListNetworkingV1NetworkLinkServices200Response list_networking_v1_network_link_services(environment, spec_display_name=spec_display_name, status_phase=status_phase, spec_network=spec_network, page_size=page_size, page_token=page_token)

List of Network Link Services

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all network link services.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.list_networking_v1_network_link_services200_response import ListNetworkingV1NetworkLinkServices200Response
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
    api_instance = openapi_client.NetworkLinkServicesNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Filter the results by exact match for environment.
    spec_display_name = ['[\"prod-net-1-nls\",\"dev-net-1-nls\"]'] # List[str] | Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. (optional)
    status_phase = ['[\"READY\"]'] # List[str] | Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. (optional)
    spec_network = ['[\"n-00000\",\"n-00001\"]'] # List[str] | Filter the results by exact match for spec.network. Pass multiple times to see results matching any of the values. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Network Link Services
        api_response = api_instance.list_networking_v1_network_link_services(environment, spec_display_name=spec_display_name, status_phase=status_phase, spec_network=spec_network, page_size=page_size, page_token=page_token)
        print("The response of NetworkLinkServicesNetworkingV1Api->list_networking_v1_network_link_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLinkServicesNetworkingV1Api->list_networking_v1_network_link_services: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filter the results by exact match for environment. | 
 **spec_display_name** | [**List[str]**](str.md)| Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. | [optional] 
 **status_phase** | [**List[str]**](str.md)| Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. | [optional] 
 **spec_network** | [**List[str]**](str.md)| Filter the results by exact match for spec.network. Pass multiple times to see results matching any of the values. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListNetworkingV1NetworkLinkServices200Response**](ListNetworkingV1NetworkLinkServices200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Link Service. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_networking_v1_network_link_service**
> GetNetworkingV1NetworkLinkService200Response update_networking_v1_network_link_service(id, update_networking_v1_network_link_service_request=update_networking_v1_network_link_service_request)

Update a Network Link Service

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a network link service.  

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_network_link_service200_response import GetNetworkingV1NetworkLinkService200Response
from openapi_client.models.update_networking_v1_network_link_service_request import UpdateNetworkingV1NetworkLinkServiceRequest
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
    api_instance = openapi_client.NetworkLinkServicesNetworkingV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the network link service.
    update_networking_v1_network_link_service_request = openapi_client.UpdateNetworkingV1NetworkLinkServiceRequest() # UpdateNetworkingV1NetworkLinkServiceRequest |  (optional)

    try:
        # Update a Network Link Service
        api_response = api_instance.update_networking_v1_network_link_service(id, update_networking_v1_network_link_service_request=update_networking_v1_network_link_service_request)
        print("The response of NetworkLinkServicesNetworkingV1Api->update_networking_v1_network_link_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLinkServicesNetworkingV1Api->update_networking_v1_network_link_service: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the network link service. | 
 **update_networking_v1_network_link_service_request** | [**UpdateNetworkingV1NetworkLinkServiceRequest**](UpdateNetworkingV1NetworkLinkServiceRequest.md)|  | [optional] 

### Return type

[**GetNetworkingV1NetworkLinkService200Response**](GetNetworkingV1NetworkLinkService200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Link Service. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

