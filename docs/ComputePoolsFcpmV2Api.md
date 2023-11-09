# openapi_client.ComputePoolsFcpmV2Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_fcpm_v2_compute_pool**](ComputePoolsFcpmV2Api.md#create_fcpm_v2_compute_pool) | **POST** /fcpm/v2/compute-pools | Create a Compute Pool
[**delete_fcpm_v2_compute_pool**](ComputePoolsFcpmV2Api.md#delete_fcpm_v2_compute_pool) | **DELETE** /fcpm/v2/compute-pools/{id} | Delete a Compute Pool
[**get_fcpm_v2_compute_pool**](ComputePoolsFcpmV2Api.md#get_fcpm_v2_compute_pool) | **GET** /fcpm/v2/compute-pools/{id} | Read a Compute Pool
[**list_fcpm_v2_compute_pools**](ComputePoolsFcpmV2Api.md#list_fcpm_v2_compute_pools) | **GET** /fcpm/v2/compute-pools | List of Compute Pools
[**update_fcpm_v2_compute_pool**](ComputePoolsFcpmV2Api.md#update_fcpm_v2_compute_pool) | **PATCH** /fcpm/v2/compute-pools/{id} | Update a Compute Pool


# **create_fcpm_v2_compute_pool**
> CreateFcpmV2ComputePool202Response create_fcpm_v2_compute_pool(create_fcpm_v2_compute_pool_request=create_fcpm_v2_compute_pool_request)

Create a Compute Pool

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a compute pool.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_fcpm_v2_compute_pool202_response import CreateFcpmV2ComputePool202Response
from openapi_client.models.create_fcpm_v2_compute_pool_request import CreateFcpmV2ComputePoolRequest
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
    api_instance = openapi_client.ComputePoolsFcpmV2Api(api_client)
    create_fcpm_v2_compute_pool_request = openapi_client.CreateFcpmV2ComputePoolRequest() # CreateFcpmV2ComputePoolRequest |  (optional)

    try:
        # Create a Compute Pool
        api_response = api_instance.create_fcpm_v2_compute_pool(create_fcpm_v2_compute_pool_request=create_fcpm_v2_compute_pool_request)
        print("The response of ComputePoolsFcpmV2Api->create_fcpm_v2_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolsFcpmV2Api->create_fcpm_v2_compute_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_fcpm_v2_compute_pool_request** | [**CreateFcpmV2ComputePoolRequest**](CreateFcpmV2ComputePoolRequest.md)|  | [optional] 

### Return type

[**CreateFcpmV2ComputePool202Response**](CreateFcpmV2ComputePool202Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Compute Pool is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - ComputePool resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_fcpm_v2_compute_pool**
> delete_fcpm_v2_compute_pool(environment, id)

Delete a Compute Pool

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a compute pool.

### Example

* Basic Authentication (cloud-api-key):
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

# Configure HTTP basic authorization: cloud-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ComputePoolsFcpmV2Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the compute pool.

    try:
        # Delete a Compute Pool
        api_instance.delete_fcpm_v2_compute_pool(environment, id)
    except Exception as e:
        print("Exception when calling ComputePoolsFcpmV2Api->delete_fcpm_v2_compute_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the compute pool. | 

### Return type

void (empty response body)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A Compute Pool is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_fcpm_v2_compute_pool**
> GetFcpmV2ComputePool200Response get_fcpm_v2_compute_pool(environment, id)

Read a Compute Pool

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a compute pool.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_fcpm_v2_compute_pool200_response import GetFcpmV2ComputePool200Response
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
    api_instance = openapi_client.ComputePoolsFcpmV2Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the compute pool.

    try:
        # Read a Compute Pool
        api_response = api_instance.get_fcpm_v2_compute_pool(environment, id)
        print("The response of ComputePoolsFcpmV2Api->get_fcpm_v2_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolsFcpmV2Api->get_fcpm_v2_compute_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the compute pool. | 

### Return type

[**GetFcpmV2ComputePool200Response**](GetFcpmV2ComputePool200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compute Pool. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_fcpm_v2_compute_pools**
> ListFcpmV2ComputePools200Response list_fcpm_v2_compute_pools(environment, spec_region=spec_region, spec_network=spec_network, page_size=page_size, page_token=page_token)

List of Compute Pools

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all compute pools.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_fcpm_v2_compute_pools200_response import ListFcpmV2ComputePools200Response
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
    api_instance = openapi_client.ComputePoolsFcpmV2Api(api_client)
    environment = 'env-00000' # str | Filter the results by exact match for environment.
    spec_region = 'us-west-1' # str | Filter the results by exact match for spec.region. (optional)
    spec_network = 'n-00000' # str | Filter the results by exact match for spec.network. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Compute Pools
        api_response = api_instance.list_fcpm_v2_compute_pools(environment, spec_region=spec_region, spec_network=spec_network, page_size=page_size, page_token=page_token)
        print("The response of ComputePoolsFcpmV2Api->list_fcpm_v2_compute_pools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolsFcpmV2Api->list_fcpm_v2_compute_pools: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filter the results by exact match for environment. | 
 **spec_region** | **str**| Filter the results by exact match for spec.region. | [optional] 
 **spec_network** | **str**| Filter the results by exact match for spec.network. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListFcpmV2ComputePools200Response**](ListFcpmV2ComputePools200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compute Pool. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_fcpm_v2_compute_pool**
> GetFcpmV2ComputePool200Response update_fcpm_v2_compute_pool(id, update_fcpm_v2_compute_pool_request=update_fcpm_v2_compute_pool_request)

Update a Compute Pool

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a compute pool.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_fcpm_v2_compute_pool200_response import GetFcpmV2ComputePool200Response
from openapi_client.models.update_fcpm_v2_compute_pool_request import UpdateFcpmV2ComputePoolRequest
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
    api_instance = openapi_client.ComputePoolsFcpmV2Api(api_client)
    id = 'id_example' # str | The unique identifier for the compute pool.
    update_fcpm_v2_compute_pool_request = openapi_client.UpdateFcpmV2ComputePoolRequest() # UpdateFcpmV2ComputePoolRequest |  (optional)

    try:
        # Update a Compute Pool
        api_response = api_instance.update_fcpm_v2_compute_pool(id, update_fcpm_v2_compute_pool_request=update_fcpm_v2_compute_pool_request)
        print("The response of ComputePoolsFcpmV2Api->update_fcpm_v2_compute_pool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComputePoolsFcpmV2Api->update_fcpm_v2_compute_pool: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the compute pool. | 
 **update_fcpm_v2_compute_pool_request** | [**UpdateFcpmV2ComputePoolRequest**](UpdateFcpmV2ComputePoolRequest.md)|  | [optional] 

### Return type

[**GetFcpmV2ComputePool200Response**](GetFcpmV2ComputePool200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Compute Pool. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

