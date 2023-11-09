# openapi_client.NetworksNetworkingV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_networking_v1_network**](NetworksNetworkingV1Api.md#create_networking_v1_network) | **POST** /networking/v1/networks | Create a Network
[**delete_networking_v1_network**](NetworksNetworkingV1Api.md#delete_networking_v1_network) | **DELETE** /networking/v1/networks/{id} | Delete a Network
[**get_networking_v1_network**](NetworksNetworkingV1Api.md#get_networking_v1_network) | **GET** /networking/v1/networks/{id} | Read a Network
[**list_networking_v1_networks**](NetworksNetworkingV1Api.md#list_networking_v1_networks) | **GET** /networking/v1/networks | List of Networks
[**update_networking_v1_network**](NetworksNetworkingV1Api.md#update_networking_v1_network) | **PATCH** /networking/v1/networks/{id} | Update a Network


# **create_networking_v1_network**
> CreateNetworkingV1Network202Response create_networking_v1_network(create_networking_v1_network_request=create_networking_v1_network_request)

Create a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a network.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.create_networking_v1_network202_response import CreateNetworkingV1Network202Response
from openapi_client.models.create_networking_v1_network_request import CreateNetworkingV1NetworkRequest
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
    api_instance = openapi_client.NetworksNetworkingV1Api(api_client)
    create_networking_v1_network_request = openapi_client.CreateNetworkingV1NetworkRequest() # CreateNetworkingV1NetworkRequest |  (optional)

    try:
        # Create a Network
        api_response = api_instance.create_networking_v1_network(create_networking_v1_network_request=create_networking_v1_network_request)
        print("The response of NetworksNetworkingV1Api->create_networking_v1_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksNetworkingV1Api->create_networking_v1_network: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_networking_v1_network_request** | [**CreateNetworkingV1NetworkRequest**](CreateNetworkingV1NetworkRequest.md)|  | [optional] 

### Return type

[**CreateNetworkingV1Network202Response**](CreateNetworkingV1Network202Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Network is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - Network resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_networking_v1_network**
> delete_networking_v1_network(environment, id)

Delete a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a network.

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
    api_instance = openapi_client.NetworksNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the network.

    try:
        # Delete a Network
        api_instance.delete_networking_v1_network(environment, id)
    except Exception as e:
        print("Exception when calling NetworksNetworkingV1Api->delete_networking_v1_network: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the network. | 

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
**204** | A Network is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_networking_v1_network**
> GetNetworkingV1Network200Response get_networking_v1_network(environment, id)

Read a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a network.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_network200_response import GetNetworkingV1Network200Response
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
    api_instance = openapi_client.NetworksNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the network.

    try:
        # Read a Network
        api_response = api_instance.get_networking_v1_network(environment, id)
        print("The response of NetworksNetworkingV1Api->get_networking_v1_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksNetworkingV1Api->get_networking_v1_network: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the network. | 

### Return type

[**GetNetworkingV1Network200Response**](GetNetworkingV1Network200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_networking_v1_networks**
> ListNetworkingV1Networks200Response list_networking_v1_networks(environment, spec_display_name=spec_display_name, spec_cloud=spec_cloud, spec_region=spec_region, spec_cidr=spec_cidr, status_phase=status_phase, connection_type=connection_type, page_size=page_size, page_token=page_token)

List of Networks

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all networks.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.list_networking_v1_networks200_response import ListNetworkingV1Networks200Response
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
    api_instance = openapi_client.NetworksNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Filter the results by exact match for environment.
    spec_display_name = ['[\"prod-gcp-us-central1\",\"prod-aws-us-east1\"]'] # List[str] | Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. (optional)
    spec_cloud = ['[\"GCP\",\"AWS\"]'] # List[str] | Filter the results by exact match for spec.cloud. Pass multiple times to see results matching any of the values. (optional)
    spec_region = ['[\"us-central1\",\"us-east-1\"]'] # List[str] | Filter the results by exact match for spec.region. Pass multiple times to see results matching any of the values. (optional)
    spec_cidr = ['[\"10.200.0.0/16\"]'] # List[str] | Filter the results by exact match for spec.cidr. Pass multiple times to see results matching any of the values. (optional)
    status_phase = ['[\"PROVISIONING\",\"READY\"]'] # List[str] | Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. (optional)
    connection_type = ['[\"peering\",\"privatelink\"]'] # List[str] | Filter the results by exact match for connection_type. Pass multiple times to see results matching any of the values. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Networks
        api_response = api_instance.list_networking_v1_networks(environment, spec_display_name=spec_display_name, spec_cloud=spec_cloud, spec_region=spec_region, spec_cidr=spec_cidr, status_phase=status_phase, connection_type=connection_type, page_size=page_size, page_token=page_token)
        print("The response of NetworksNetworkingV1Api->list_networking_v1_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksNetworkingV1Api->list_networking_v1_networks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filter the results by exact match for environment. | 
 **spec_display_name** | [**List[str]**](str.md)| Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. | [optional] 
 **spec_cloud** | [**List[str]**](str.md)| Filter the results by exact match for spec.cloud. Pass multiple times to see results matching any of the values. | [optional] 
 **spec_region** | [**List[str]**](str.md)| Filter the results by exact match for spec.region. Pass multiple times to see results matching any of the values. | [optional] 
 **spec_cidr** | [**List[str]**](str.md)| Filter the results by exact match for spec.cidr. Pass multiple times to see results matching any of the values. | [optional] 
 **status_phase** | [**List[str]**](str.md)| Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. | [optional] 
 **connection_type** | [**List[str]**](str.md)| Filter the results by exact match for connection_type. Pass multiple times to see results matching any of the values. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListNetworkingV1Networks200Response**](ListNetworkingV1Networks200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_networking_v1_network**
> GetNetworkingV1Network200Response update_networking_v1_network(id, update_networking_v1_network_request=update_networking_v1_network_request)

Update a Network

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a network.  

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_network200_response import GetNetworkingV1Network200Response
from openapi_client.models.update_networking_v1_network_request import UpdateNetworkingV1NetworkRequest
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
    api_instance = openapi_client.NetworksNetworkingV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the network.
    update_networking_v1_network_request = openapi_client.UpdateNetworkingV1NetworkRequest() # UpdateNetworkingV1NetworkRequest |  (optional)

    try:
        # Update a Network
        api_response = api_instance.update_networking_v1_network(id, update_networking_v1_network_request=update_networking_v1_network_request)
        print("The response of NetworksNetworkingV1Api->update_networking_v1_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworksNetworkingV1Api->update_networking_v1_network: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the network. | 
 **update_networking_v1_network_request** | [**UpdateNetworkingV1NetworkRequest**](UpdateNetworkingV1NetworkRequest.md)|  | [optional] 

### Return type

[**GetNetworkingV1Network200Response**](GetNetworkingV1Network200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

