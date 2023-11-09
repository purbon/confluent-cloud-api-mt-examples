# openapi_client.ClientQuotasKafkaQuotasV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kafka_quotas_v1_client_quota**](ClientQuotasKafkaQuotasV1Api.md#create_kafka_quotas_v1_client_quota) | **POST** /kafka-quotas/v1/client-quotas | Create a Client Quota
[**delete_kafka_quotas_v1_client_quota**](ClientQuotasKafkaQuotasV1Api.md#delete_kafka_quotas_v1_client_quota) | **DELETE** /kafka-quotas/v1/client-quotas/{id} | Delete a Client Quota
[**get_kafka_quotas_v1_client_quota**](ClientQuotasKafkaQuotasV1Api.md#get_kafka_quotas_v1_client_quota) | **GET** /kafka-quotas/v1/client-quotas/{id} | Read a Client Quota
[**list_kafka_quotas_v1_client_quotas**](ClientQuotasKafkaQuotasV1Api.md#list_kafka_quotas_v1_client_quotas) | **GET** /kafka-quotas/v1/client-quotas | List of Client Quotas
[**update_kafka_quotas_v1_client_quota**](ClientQuotasKafkaQuotasV1Api.md#update_kafka_quotas_v1_client_quota) | **PATCH** /kafka-quotas/v1/client-quotas/{id} | Update a Client Quota


# **create_kafka_quotas_v1_client_quota**
> CreateKafkaQuotasV1ClientQuota202Response create_kafka_quotas_v1_client_quota(create_kafka_quotas_v1_client_quota_request=create_kafka_quotas_v1_client_quota_request)

Create a Client Quota

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a client quota.

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_kafka_quotas_v1_client_quota202_response import CreateKafkaQuotasV1ClientQuota202Response
from openapi_client.models.create_kafka_quotas_v1_client_quota_request import CreateKafkaQuotasV1ClientQuotaRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClientQuotasKafkaQuotasV1Api(api_client)
    create_kafka_quotas_v1_client_quota_request = openapi_client.CreateKafkaQuotasV1ClientQuotaRequest() # CreateKafkaQuotasV1ClientQuotaRequest |  (optional)

    try:
        # Create a Client Quota
        api_response = api_instance.create_kafka_quotas_v1_client_quota(create_kafka_quotas_v1_client_quota_request=create_kafka_quotas_v1_client_quota_request)
        print("The response of ClientQuotasKafkaQuotasV1Api->create_kafka_quotas_v1_client_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQuotasKafkaQuotasV1Api->create_kafka_quotas_v1_client_quota: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_kafka_quotas_v1_client_quota_request** | [**CreateKafkaQuotasV1ClientQuotaRequest**](CreateKafkaQuotasV1ClientQuotaRequest.md)|  | [optional] 

### Return type

[**CreateKafkaQuotasV1ClientQuota202Response**](CreateKafkaQuotasV1ClientQuota202Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Client Quota is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - ClientQuota resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_kafka_quotas_v1_client_quota**
> delete_kafka_quotas_v1_client_quota(id)

Delete a Client Quota

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a client quota.

### Example

* Basic Authentication (api-key):
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClientQuotasKafkaQuotasV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the client quota.

    try:
        # Delete a Client Quota
        api_instance.delete_kafka_quotas_v1_client_quota(id)
    except Exception as e:
        print("Exception when calling ClientQuotasKafkaQuotasV1Api->delete_kafka_quotas_v1_client_quota: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the client quota. | 

### Return type

void (empty response body)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A Client Quota is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_kafka_quotas_v1_client_quota**
> GetKafkaQuotasV1ClientQuota200Response get_kafka_quotas_v1_client_quota(id)

Read a Client Quota

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a client quota.

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_kafka_quotas_v1_client_quota200_response import GetKafkaQuotasV1ClientQuota200Response
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClientQuotasKafkaQuotasV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the client quota.

    try:
        # Read a Client Quota
        api_response = api_instance.get_kafka_quotas_v1_client_quota(id)
        print("The response of ClientQuotasKafkaQuotasV1Api->get_kafka_quotas_v1_client_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQuotasKafkaQuotasV1Api->get_kafka_quotas_v1_client_quota: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the client quota. | 

### Return type

[**GetKafkaQuotasV1ClientQuota200Response**](GetKafkaQuotasV1ClientQuota200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client Quota. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_kafka_quotas_v1_client_quotas**
> ListKafkaQuotasV1ClientQuotas200Response list_kafka_quotas_v1_client_quotas(spec_cluster, environment, page_size=page_size, page_token=page_token)

List of Client Quotas

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all client quotas.

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_kafka_quotas_v1_client_quotas200_response import ListKafkaQuotasV1ClientQuotas200Response
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClientQuotasKafkaQuotasV1Api(api_client)
    spec_cluster = 'lkc-xxxxx' # str | Filter the results by exact match for spec.cluster.
    environment = 'env-xxxxx' # str | Filter the results by exact match for environment.
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Client Quotas
        api_response = api_instance.list_kafka_quotas_v1_client_quotas(spec_cluster, environment, page_size=page_size, page_token=page_token)
        print("The response of ClientQuotasKafkaQuotasV1Api->list_kafka_quotas_v1_client_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQuotasKafkaQuotasV1Api->list_kafka_quotas_v1_client_quotas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec_cluster** | **str**| Filter the results by exact match for spec.cluster. | 
 **environment** | **str**| Filter the results by exact match for environment. | 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListKafkaQuotasV1ClientQuotas200Response**](ListKafkaQuotasV1ClientQuotas200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client Quota. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_kafka_quotas_v1_client_quota**
> GetKafkaQuotasV1ClientQuota200Response update_kafka_quotas_v1_client_quota(id, update_kafka_quotas_v1_client_quota_request=update_kafka_quotas_v1_client_quota_request)

Update a Client Quota

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a client quota.  

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_kafka_quotas_v1_client_quota200_response import GetKafkaQuotasV1ClientQuota200Response
from openapi_client.models.update_kafka_quotas_v1_client_quota_request import UpdateKafkaQuotasV1ClientQuotaRequest
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClientQuotasKafkaQuotasV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the client quota.
    update_kafka_quotas_v1_client_quota_request = openapi_client.UpdateKafkaQuotasV1ClientQuotaRequest() # UpdateKafkaQuotasV1ClientQuotaRequest |  (optional)

    try:
        # Update a Client Quota
        api_response = api_instance.update_kafka_quotas_v1_client_quota(id, update_kafka_quotas_v1_client_quota_request=update_kafka_quotas_v1_client_quota_request)
        print("The response of ClientQuotasKafkaQuotasV1Api->update_kafka_quotas_v1_client_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQuotasKafkaQuotasV1Api->update_kafka_quotas_v1_client_quota: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the client quota. | 
 **update_kafka_quotas_v1_client_quota_request** | [**UpdateKafkaQuotasV1ClientQuotaRequest**](UpdateKafkaQuotasV1ClientQuotaRequest.md)|  | [optional] 

### Return type

[**GetKafkaQuotasV1ClientQuota200Response**](GetKafkaQuotasV1ClientQuota200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client Quota. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

