# openapi_client.ExportersV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_exporter**](ExportersV1Api.md#delete_exporter) | **DELETE** /exporters/{name} | Delete schema exporter by name.
[**get_exporter_config_by_name**](ExportersV1Api.md#get_exporter_config_by_name) | **GET** /exporters/{name}/config | Gets schema exporter config by name.
[**get_exporter_info_by_name**](ExportersV1Api.md#get_exporter_info_by_name) | **GET** /exporters/{name} | Gets schema exporter by name.
[**get_exporter_status_by_name**](ExportersV1Api.md#get_exporter_status_by_name) | **GET** /exporters/{name}/status | Gets schema exporter status by name.
[**list_exporters**](ExportersV1Api.md#list_exporters) | **GET** /exporters | Gets all schema exporters.
[**pause_exporter_by_name**](ExportersV1Api.md#pause_exporter_by_name) | **PUT** /exporters/{name}/pause | Pause schema exporter by name.
[**register_exporter**](ExportersV1Api.md#register_exporter) | **POST** /exporters | Creates a new schema exporter.
[**reset_exporter_by_name**](ExportersV1Api.md#reset_exporter_by_name) | **PUT** /exporters/{name}/reset | Reset schema exporter by name.
[**resume_exporter_by_name**](ExportersV1Api.md#resume_exporter_by_name) | **PUT** /exporters/{name}/resume | Resume schema exporter by name.
[**update_exporter_config_by_name**](ExportersV1Api.md#update_exporter_config_by_name) | **PUT** /exporters/{name}/config | Update schema exporter config by name.
[**update_exporter_info**](ExportersV1Api.md#update_exporter_info) | **PUT** /exporters/{name} | Update schema exporter by name.


# **delete_exporter**
> delete_exporter(name)

Delete schema exporter by name.

Deletes the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter

    try:
        # Delete schema exporter by name.
        api_instance.delete_exporter(name)
    except Exception as e:
        print("Exception when calling ExportersV1Api->delete_exporter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 

### Return type

void (empty response body)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_exporter_config_by_name**
> ExporterConfigResponse get_exporter_config_by_name(name)

Gets schema exporter config by name.

Retrieves the config of the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_config_response import ExporterConfigResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter

    try:
        # Gets schema exporter config by name.
        api_response = api_instance.get_exporter_config_by_name(name)
        print("The response of ExportersV1Api->get_exporter_config_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->get_exporter_config_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 

### Return type

[**ExporterConfigResponse**](ExporterConfigResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40450 – Exporter not found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_exporter_info_by_name**
> ExporterReference get_exporter_info_by_name(name)

Gets schema exporter by name.

Retrieves the information of the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_reference import ExporterReference
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter

    try:
        # Gets schema exporter by name.
        api_response = api_instance.get_exporter_info_by_name(name)
        print("The response of ExportersV1Api->get_exporter_info_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->get_exporter_info_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 

### Return type

[**ExporterReference**](ExporterReference.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40450 – Exporter not found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_exporter_status_by_name**
> ExporterStatusResponse get_exporter_status_by_name(name)

Gets schema exporter status by name.

Retrieves the status of the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_status_response import ExporterStatusResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter

    try:
        # Gets schema exporter status by name.
        api_response = api_instance.get_exporter_status_by_name(name)
        print("The response of ExportersV1Api->get_exporter_status_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->get_exporter_status_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 

### Return type

[**ExporterStatusResponse**](ExporterStatusResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40450 – Exporter not found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_exporters**
> List[str] list_exporters()

Gets all schema exporters.

Retrieves a list of schema exporters that have been created.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)

    try:
        # Gets all schema exporters.
        api_response = api_instance.list_exporters()
        print("The response of ExportersV1Api->list_exporters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->list_exporters: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Name of the exporter |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **pause_exporter_by_name**
> ExporterResponse pause_exporter_by_name(name)

Pause schema exporter by name.

Pauses the state of the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_response import ExporterResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter

    try:
        # Pause schema exporter by name.
        api_response = api_instance.pause_exporter_by_name(name)
        print("The response of ExportersV1Api->pause_exporter_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->pause_exporter_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 

### Return type

[**ExporterResponse**](ExporterResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. |  -  |
**409** | Invalid. Error code 40952 – Invalid exporter subjects. Error code 40963 – Exporter not paused. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **register_exporter**
> ExporterResponse register_exporter(exporter_reference)

Creates a new schema exporter.

Creates a new schema exporter. All attributes in request body are optional except config.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_reference import ExporterReference
from openapi_client.models.exporter_response import ExporterResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    exporter_reference = openapi_client.ExporterReference() # ExporterReference | Schema

    try:
        # Creates a new schema exporter.
        api_response = api_instance.register_exporter(exporter_reference)
        print("The response of ExportersV1Api->register_exporter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->register_exporter: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exporter_reference** | [**ExporterReference**](ExporterReference.md)| Schema | 

### Return type

[**ExporterResponse**](ExporterResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json
 - **Accept**: application/json; qs=0.5, application/json, application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schema successfully registered. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict. Error code 40950 – Missing or invalid exporter name \\ Error code 40951 – Missing or invalid exporter config \\ Error code 40952 – Invalid exporter subjects \\ Error code 40960 – Exporter already exists \\ Error code 40964 – Too many exporters |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **reset_exporter_by_name**
> ExporterResponse reset_exporter_by_name(name)

Reset schema exporter by name.

Reset the state of the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_response import ExporterResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter

    try:
        # Reset schema exporter by name.
        api_response = api_instance.reset_exporter_by_name(name)
        print("The response of ExportersV1Api->reset_exporter_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->reset_exporter_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 

### Return type

[**ExporterResponse**](ExporterResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40450 – Exporter not found |  -  |
**409** | Invalid. Error code 40963 – Exporter not paused. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **resume_exporter_by_name**
> ExporterResponse resume_exporter_by_name(name)

Resume schema exporter by name.

Resume running of the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_response import ExporterResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter

    try:
        # Resume schema exporter by name.
        api_response = api_instance.resume_exporter_by_name(name)
        print("The response of ExportersV1Api->resume_exporter_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->resume_exporter_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 

### Return type

[**ExporterResponse**](ExporterResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40450 indicates subject not found. |  -  |
**409** | Invalid. Error code 40961 – Exporter already running. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_exporter_config_by_name**
> ExporterResponse update_exporter_config_by_name(name, exporter_config_response)

Update schema exporter config by name.

Retrieves the config of the schema exporter.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_config_response import ExporterConfigResponse
from openapi_client.models.exporter_response import ExporterResponse
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter
    exporter_config_response = openapi_client.ExporterConfigResponse() # ExporterConfigResponse | Exporter Update Request

    try:
        # Update schema exporter config by name.
        api_response = api_instance.update_exporter_config_by_name(name, exporter_config_response)
        print("The response of ExportersV1Api->update_exporter_config_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->update_exporter_config_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 
 **exporter_config_response** | [**ExporterConfigResponse**](ExporterConfigResponse.md)| Exporter Update Request | 

### Return type

[**ExporterResponse**](ExporterResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. |  -  |
**409** | Invalid. Error code 40952 – Invalid exporter subjects. Error code 40963 – Exporter not paused. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_exporter_info**
> ExporterResponse update_exporter_info(name, exporter_update_request)

Update schema exporter by name.

Updates the information or configurations of the schema exporter. All attributes in request body are optional.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.exporter_response import ExporterResponse
from openapi_client.models.exporter_update_request import ExporterUpdateRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportersV1Api(api_client)
    name = 'name_example' # str | Name of the exporter
    exporter_update_request = openapi_client.ExporterUpdateRequest() # ExporterUpdateRequest | Exporter Update Request

    try:
        # Update schema exporter by name.
        api_response = api_instance.update_exporter_info(name, exporter_update_request)
        print("The response of ExportersV1Api->update_exporter_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportersV1Api->update_exporter_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the exporter | 
 **exporter_update_request** | [**ExporterUpdateRequest**](ExporterUpdateRequest.md)| Exporter Update Request | 

### Return type

[**ExporterResponse**](ExporterResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json
 - **Accept**: application/vnd.schemaregistry.v1+json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The original request. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. |  -  |
**409** | Invalid. Error code 40952 – Invalid exporter subjects. Error code 40963 – Exporter not paused. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

