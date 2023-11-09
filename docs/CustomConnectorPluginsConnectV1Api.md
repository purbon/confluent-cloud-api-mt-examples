# openapi_client.CustomConnectorPluginsConnectV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connect_v1_custom_connector_plugin**](CustomConnectorPluginsConnectV1Api.md#create_connect_v1_custom_connector_plugin) | **POST** /connect/v1/custom-connector-plugins | Create a Custom Connector Plugin
[**delete_connect_v1_custom_connector_plugin**](CustomConnectorPluginsConnectV1Api.md#delete_connect_v1_custom_connector_plugin) | **DELETE** /connect/v1/custom-connector-plugins/{id} | Delete a Custom Connector Plugin
[**get_connect_v1_custom_connector_plugin**](CustomConnectorPluginsConnectV1Api.md#get_connect_v1_custom_connector_plugin) | **GET** /connect/v1/custom-connector-plugins/{id} | Read a Custom Connector Plugin
[**list_connect_v1_custom_connector_plugins**](CustomConnectorPluginsConnectV1Api.md#list_connect_v1_custom_connector_plugins) | **GET** /connect/v1/custom-connector-plugins | List of Custom Connector Plugins
[**update_connect_v1_custom_connector_plugin**](CustomConnectorPluginsConnectV1Api.md#update_connect_v1_custom_connector_plugin) | **PATCH** /connect/v1/custom-connector-plugins/{id} | Update a Custom Connector Plugin


# **create_connect_v1_custom_connector_plugin**
> CreateConnectV1CustomConnectorPluginRequest create_connect_v1_custom_connector_plugin(create_connect_v1_custom_connector_plugin_request=create_connect_v1_custom_connector_plugin_request)

Create a Custom Connector Plugin

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a custom connector plugin.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_connect_v1_custom_connector_plugin_request import CreateConnectV1CustomConnectorPluginRequest
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
    api_instance = openapi_client.CustomConnectorPluginsConnectV1Api(api_client)
    create_connect_v1_custom_connector_plugin_request = openapi_client.CreateConnectV1CustomConnectorPluginRequest() # CreateConnectV1CustomConnectorPluginRequest |  (optional)

    try:
        # Create a Custom Connector Plugin
        api_response = api_instance.create_connect_v1_custom_connector_plugin(create_connect_v1_custom_connector_plugin_request=create_connect_v1_custom_connector_plugin_request)
        print("The response of CustomConnectorPluginsConnectV1Api->create_connect_v1_custom_connector_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomConnectorPluginsConnectV1Api->create_connect_v1_custom_connector_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connect_v1_custom_connector_plugin_request** | [**CreateConnectV1CustomConnectorPluginRequest**](CreateConnectV1CustomConnectorPluginRequest.md)|  | [optional] 

### Return type

[**CreateConnectV1CustomConnectorPluginRequest**](CreateConnectV1CustomConnectorPluginRequest.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Custom Connector Plugin was created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - CustomConnectorPlugin resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_connect_v1_custom_connector_plugin**
> delete_connect_v1_custom_connector_plugin(id)

Delete a Custom Connector Plugin

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a custom connector plugin.

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
    api_instance = openapi_client.CustomConnectorPluginsConnectV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the custom connector plugin.

    try:
        # Delete a Custom Connector Plugin
        api_instance.delete_connect_v1_custom_connector_plugin(id)
    except Exception as e:
        print("Exception when calling CustomConnectorPluginsConnectV1Api->delete_connect_v1_custom_connector_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the custom connector plugin. | 

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
**204** | A Custom Connector Plugin is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_connect_v1_custom_connector_plugin**
> GetConnectV1CustomConnectorPlugin200Response get_connect_v1_custom_connector_plugin(id)

Read a Custom Connector Plugin

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a custom connector plugin.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.get_connect_v1_custom_connector_plugin200_response import GetConnectV1CustomConnectorPlugin200Response
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
    api_instance = openapi_client.CustomConnectorPluginsConnectV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the custom connector plugin.

    try:
        # Read a Custom Connector Plugin
        api_response = api_instance.get_connect_v1_custom_connector_plugin(id)
        print("The response of CustomConnectorPluginsConnectV1Api->get_connect_v1_custom_connector_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomConnectorPluginsConnectV1Api->get_connect_v1_custom_connector_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the custom connector plugin. | 

### Return type

[**GetConnectV1CustomConnectorPlugin200Response**](GetConnectV1CustomConnectorPlugin200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Connector Plugin. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_connect_v1_custom_connector_plugins**
> ConnectV1CustomConnectorPluginList list_connect_v1_custom_connector_plugins(page_size=page_size, page_token=page_token)

List of Custom Connector Plugins

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all custom connector plugins.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.connect_v1_custom_connector_plugin_list import ConnectV1CustomConnectorPluginList
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
    api_instance = openapi_client.CustomConnectorPluginsConnectV1Api(api_client)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Custom Connector Plugins
        api_response = api_instance.list_connect_v1_custom_connector_plugins(page_size=page_size, page_token=page_token)
        print("The response of CustomConnectorPluginsConnectV1Api->list_connect_v1_custom_connector_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomConnectorPluginsConnectV1Api->list_connect_v1_custom_connector_plugins: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ConnectV1CustomConnectorPluginList**](ConnectV1CustomConnectorPluginList.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Connector Plugin. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_connect_v1_custom_connector_plugin**
> GetConnectV1CustomConnectorPlugin200Response update_connect_v1_custom_connector_plugin(id, connect_v1_custom_connector_plugin_update=connect_v1_custom_connector_plugin_update)

Update a Custom Connector Plugin

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a custom connector plugin.  

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.connect_v1_custom_connector_plugin_update import ConnectV1CustomConnectorPluginUpdate
from openapi_client.models.get_connect_v1_custom_connector_plugin200_response import GetConnectV1CustomConnectorPlugin200Response
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
    api_instance = openapi_client.CustomConnectorPluginsConnectV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the custom connector plugin.
    connect_v1_custom_connector_plugin_update = openapi_client.ConnectV1CustomConnectorPluginUpdate() # ConnectV1CustomConnectorPluginUpdate |  (optional)

    try:
        # Update a Custom Connector Plugin
        api_response = api_instance.update_connect_v1_custom_connector_plugin(id, connect_v1_custom_connector_plugin_update=connect_v1_custom_connector_plugin_update)
        print("The response of CustomConnectorPluginsConnectV1Api->update_connect_v1_custom_connector_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomConnectorPluginsConnectV1Api->update_connect_v1_custom_connector_plugin: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the custom connector plugin. | 
 **connect_v1_custom_connector_plugin_update** | [**ConnectV1CustomConnectorPluginUpdate**](ConnectV1CustomConnectorPluginUpdate.md)|  | [optional] 

### Return type

[**GetConnectV1CustomConnectorPlugin200Response**](GetConnectV1CustomConnectorPlugin200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom Connector Plugin. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

