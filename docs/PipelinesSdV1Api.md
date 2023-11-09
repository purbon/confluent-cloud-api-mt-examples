# openapi_client.PipelinesSdV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sd_v1_pipeline**](PipelinesSdV1Api.md#create_sd_v1_pipeline) | **POST** /sd/v1/pipelines | Create a Pipeline
[**delete_sd_v1_pipeline**](PipelinesSdV1Api.md#delete_sd_v1_pipeline) | **DELETE** /sd/v1/pipelines/{id} | Delete a Pipeline
[**get_sd_v1_pipeline**](PipelinesSdV1Api.md#get_sd_v1_pipeline) | **GET** /sd/v1/pipelines/{id} | Read a Pipeline
[**list_sd_v1_pipelines**](PipelinesSdV1Api.md#list_sd_v1_pipelines) | **GET** /sd/v1/pipelines | List of Pipelines
[**update_sd_v1_pipeline**](PipelinesSdV1Api.md#update_sd_v1_pipeline) | **PATCH** /sd/v1/pipelines/{id} | Update a Pipeline


# **create_sd_v1_pipeline**
> CreateSdV1Pipeline202Response create_sd_v1_pipeline(create_sd_v1_pipeline_request=create_sd_v1_pipeline_request)

Create a Pipeline

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a pipeline.

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_sd_v1_pipeline202_response import CreateSdV1Pipeline202Response
from openapi_client.models.create_sd_v1_pipeline_request import CreateSdV1PipelineRequest
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
    api_instance = openapi_client.PipelinesSdV1Api(api_client)
    create_sd_v1_pipeline_request = openapi_client.CreateSdV1PipelineRequest() # CreateSdV1PipelineRequest |  (optional)

    try:
        # Create a Pipeline
        api_response = api_instance.create_sd_v1_pipeline(create_sd_v1_pipeline_request=create_sd_v1_pipeline_request)
        print("The response of PipelinesSdV1Api->create_sd_v1_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesSdV1Api->create_sd_v1_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sd_v1_pipeline_request** | [**CreateSdV1PipelineRequest**](CreateSdV1PipelineRequest.md)|  | [optional] 

### Return type

[**CreateSdV1Pipeline202Response**](CreateSdV1Pipeline202Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Pipeline is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - Pipeline resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_sd_v1_pipeline**
> delete_sd_v1_pipeline(environment, spec_kafka_cluster, id)

Delete a Pipeline

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a pipeline.

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
    api_instance = openapi_client.PipelinesSdV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    spec_kafka_cluster = 'lkc-00000' # str | Scope the operation to the given spec.kafka_cluster.
    id = 'id_example' # str | The unique identifier for the pipeline.

    try:
        # Delete a Pipeline
        api_instance.delete_sd_v1_pipeline(environment, spec_kafka_cluster, id)
    except Exception as e:
        print("Exception when calling PipelinesSdV1Api->delete_sd_v1_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **spec_kafka_cluster** | **str**| Scope the operation to the given spec.kafka_cluster. | 
 **id** | **str**| The unique identifier for the pipeline. | 

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
**204** | A Pipeline is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_sd_v1_pipeline**
> GetSdV1Pipeline200Response get_sd_v1_pipeline(environment, spec_kafka_cluster, id)

Read a Pipeline

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a pipeline.

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_sd_v1_pipeline200_response import GetSdV1Pipeline200Response
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
    api_instance = openapi_client.PipelinesSdV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    spec_kafka_cluster = 'lkc-00000' # str | Scope the operation to the given spec.kafka_cluster.
    id = 'id_example' # str | The unique identifier for the pipeline.

    try:
        # Read a Pipeline
        api_response = api_instance.get_sd_v1_pipeline(environment, spec_kafka_cluster, id)
        print("The response of PipelinesSdV1Api->get_sd_v1_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesSdV1Api->get_sd_v1_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **spec_kafka_cluster** | **str**| Scope the operation to the given spec.kafka_cluster. | 
 **id** | **str**| The unique identifier for the pipeline. | 

### Return type

[**GetSdV1Pipeline200Response**](GetSdV1Pipeline200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_sd_v1_pipelines**
> ListSdV1Pipelines200Response list_sd_v1_pipelines(environment, spec_kafka_cluster, page_size=page_size, page_token=page_token)

List of Pipelines

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all pipelines.

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_sd_v1_pipelines200_response import ListSdV1Pipelines200Response
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
    api_instance = openapi_client.PipelinesSdV1Api(api_client)
    environment = 'env-00000' # str | Filter the results by exact match for environment.
    spec_kafka_cluster = 'lkc-00000' # str | Filter the results by exact match for spec.kafka_cluster.
    page_size = 100 # int | A pagination size for collection requests. (optional) (default to 100)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Pipelines
        api_response = api_instance.list_sd_v1_pipelines(environment, spec_kafka_cluster, page_size=page_size, page_token=page_token)
        print("The response of PipelinesSdV1Api->list_sd_v1_pipelines:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesSdV1Api->list_sd_v1_pipelines: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filter the results by exact match for environment. | 
 **spec_kafka_cluster** | **str**| Filter the results by exact match for spec.kafka_cluster. | 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 100]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListSdV1Pipelines200Response**](ListSdV1Pipelines200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_sd_v1_pipeline**
> GetSdV1Pipeline200Response update_sd_v1_pipeline(id, update_sd_v1_pipeline_request=update_sd_v1_pipeline_request)

Update a Pipeline

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a pipeline.  

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_sd_v1_pipeline200_response import GetSdV1Pipeline200Response
from openapi_client.models.update_sd_v1_pipeline_request import UpdateSdV1PipelineRequest
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
    api_instance = openapi_client.PipelinesSdV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the pipeline.
    update_sd_v1_pipeline_request = openapi_client.UpdateSdV1PipelineRequest() # UpdateSdV1PipelineRequest |  (optional)

    try:
        # Update a Pipeline
        api_response = api_instance.update_sd_v1_pipeline(id, update_sd_v1_pipeline_request=update_sd_v1_pipeline_request)
        print("The response of PipelinesSdV1Api->update_sd_v1_pipeline:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipelinesSdV1Api->update_sd_v1_pipeline: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the pipeline. | 
 **update_sd_v1_pipeline_request** | [**UpdateSdV1PipelineRequest**](UpdateSdV1PipelineRequest.md)|  | [optional] 

### Return type

[**GetSdV1Pipeline200Response**](GetSdV1Pipeline200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pipeline. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

