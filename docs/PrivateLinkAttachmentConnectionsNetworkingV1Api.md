# openapi_client.PrivateLinkAttachmentConnectionsNetworkingV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_networking_v1_private_link_attachment_connection**](PrivateLinkAttachmentConnectionsNetworkingV1Api.md#create_networking_v1_private_link_attachment_connection) | **POST** /networking/v1/private-link-attachment-connections | Create a Private Link Attachment Connection
[**delete_networking_v1_private_link_attachment_connection**](PrivateLinkAttachmentConnectionsNetworkingV1Api.md#delete_networking_v1_private_link_attachment_connection) | **DELETE** /networking/v1/private-link-attachment-connections/{id} | Delete a Private Link Attachment Connection
[**get_networking_v1_private_link_attachment_connection**](PrivateLinkAttachmentConnectionsNetworkingV1Api.md#get_networking_v1_private_link_attachment_connection) | **GET** /networking/v1/private-link-attachment-connections/{id} | Read a Private Link Attachment Connection
[**list_networking_v1_private_link_attachment_connections**](PrivateLinkAttachmentConnectionsNetworkingV1Api.md#list_networking_v1_private_link_attachment_connections) | **GET** /networking/v1/private-link-attachment-connections | List of Private Link Attachment Connections
[**update_networking_v1_private_link_attachment_connection**](PrivateLinkAttachmentConnectionsNetworkingV1Api.md#update_networking_v1_private_link_attachment_connection) | **PATCH** /networking/v1/private-link-attachment-connections/{id} | Update a Private Link Attachment Connection


# **create_networking_v1_private_link_attachment_connection**
> CreateNetworkingV1PrivateLinkAttachmentConnection202Response create_networking_v1_private_link_attachment_connection(create_networking_v1_private_link_attachment_connection_request=create_networking_v1_private_link_attachment_connection_request)

Create a Private Link Attachment Connection

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a private link attachment connection.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.create_networking_v1_private_link_attachment_connection202_response import CreateNetworkingV1PrivateLinkAttachmentConnection202Response
from openapi_client.models.create_networking_v1_private_link_attachment_connection_request import CreateNetworkingV1PrivateLinkAttachmentConnectionRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PrivateLinkAttachmentConnectionsNetworkingV1Api(api_client)
    create_networking_v1_private_link_attachment_connection_request = openapi_client.CreateNetworkingV1PrivateLinkAttachmentConnectionRequest() # CreateNetworkingV1PrivateLinkAttachmentConnectionRequest |  (optional)

    try:
        # Create a Private Link Attachment Connection
        api_response = api_instance.create_networking_v1_private_link_attachment_connection(create_networking_v1_private_link_attachment_connection_request=create_networking_v1_private_link_attachment_connection_request)
        print("The response of PrivateLinkAttachmentConnectionsNetworkingV1Api->create_networking_v1_private_link_attachment_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentConnectionsNetworkingV1Api->create_networking_v1_private_link_attachment_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_networking_v1_private_link_attachment_connection_request** | [**CreateNetworkingV1PrivateLinkAttachmentConnectionRequest**](CreateNetworkingV1PrivateLinkAttachmentConnectionRequest.md)|  | [optional] 

### Return type

[**CreateNetworkingV1PrivateLinkAttachmentConnection202Response**](CreateNetworkingV1PrivateLinkAttachmentConnection202Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Private Link Attachment Connection is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - PrivateLinkAttachmentConnection resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_networking_v1_private_link_attachment_connection**
> delete_networking_v1_private_link_attachment_connection(environment, id)

Delete a Private Link Attachment Connection

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a private link attachment connection.

### Example

* Basic Authentication (cloud-api-key):
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

# Configure HTTP basic authorization: cloud-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PrivateLinkAttachmentConnectionsNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the private link attachment connection.

    try:
        # Delete a Private Link Attachment Connection
        api_instance.delete_networking_v1_private_link_attachment_connection(environment, id)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentConnectionsNetworkingV1Api->delete_networking_v1_private_link_attachment_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the private link attachment connection. | 

### Return type

void (empty response body)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | A Private Link Attachment Connection is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_networking_v1_private_link_attachment_connection**
> GetNetworkingV1PrivateLinkAttachmentConnection200Response get_networking_v1_private_link_attachment_connection(environment, id)

Read a Private Link Attachment Connection

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a private link attachment connection.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_private_link_attachment_connection200_response import GetNetworkingV1PrivateLinkAttachmentConnection200Response
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PrivateLinkAttachmentConnectionsNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the private link attachment connection.

    try:
        # Read a Private Link Attachment Connection
        api_response = api_instance.get_networking_v1_private_link_attachment_connection(environment, id)
        print("The response of PrivateLinkAttachmentConnectionsNetworkingV1Api->get_networking_v1_private_link_attachment_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentConnectionsNetworkingV1Api->get_networking_v1_private_link_attachment_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the private link attachment connection. | 

### Return type

[**GetNetworkingV1PrivateLinkAttachmentConnection200Response**](GetNetworkingV1PrivateLinkAttachmentConnection200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Link Attachment Connection. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_networking_v1_private_link_attachment_connections**
> ListNetworkingV1PrivateLinkAttachmentConnections200Response list_networking_v1_private_link_attachment_connections(environment, spec_private_link_attachment, page_size=page_size, page_token=page_token)

List of Private Link Attachment Connections

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all private link attachment connections.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.list_networking_v1_private_link_attachment_connections200_response import ListNetworkingV1PrivateLinkAttachmentConnections200Response
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PrivateLinkAttachmentConnectionsNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Filter the results by exact match for environment.
    spec_private_link_attachment = 'platt-00000' # str | Filter the results by exact match for spec.private_link_attachment.
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Private Link Attachment Connections
        api_response = api_instance.list_networking_v1_private_link_attachment_connections(environment, spec_private_link_attachment, page_size=page_size, page_token=page_token)
        print("The response of PrivateLinkAttachmentConnectionsNetworkingV1Api->list_networking_v1_private_link_attachment_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentConnectionsNetworkingV1Api->list_networking_v1_private_link_attachment_connections: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filter the results by exact match for environment. | 
 **spec_private_link_attachment** | **str**| Filter the results by exact match for spec.private_link_attachment. | 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListNetworkingV1PrivateLinkAttachmentConnections200Response**](ListNetworkingV1PrivateLinkAttachmentConnections200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Link Attachment Connection. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_networking_v1_private_link_attachment_connection**
> GetNetworkingV1PrivateLinkAttachmentConnection200Response update_networking_v1_private_link_attachment_connection(id, update_networking_v1_private_link_attachment_connection_request=update_networking_v1_private_link_attachment_connection_request)

Update a Private Link Attachment Connection

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a private link attachment connection.  

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_private_link_attachment_connection200_response import GetNetworkingV1PrivateLinkAttachmentConnection200Response
from openapi_client.models.update_networking_v1_private_link_attachment_connection_request import UpdateNetworkingV1PrivateLinkAttachmentConnectionRequest
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PrivateLinkAttachmentConnectionsNetworkingV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the private link attachment connection.
    update_networking_v1_private_link_attachment_connection_request = openapi_client.UpdateNetworkingV1PrivateLinkAttachmentConnectionRequest() # UpdateNetworkingV1PrivateLinkAttachmentConnectionRequest |  (optional)

    try:
        # Update a Private Link Attachment Connection
        api_response = api_instance.update_networking_v1_private_link_attachment_connection(id, update_networking_v1_private_link_attachment_connection_request=update_networking_v1_private_link_attachment_connection_request)
        print("The response of PrivateLinkAttachmentConnectionsNetworkingV1Api->update_networking_v1_private_link_attachment_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentConnectionsNetworkingV1Api->update_networking_v1_private_link_attachment_connection: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the private link attachment connection. | 
 **update_networking_v1_private_link_attachment_connection_request** | [**UpdateNetworkingV1PrivateLinkAttachmentConnectionRequest**](UpdateNetworkingV1PrivateLinkAttachmentConnectionRequest.md)|  | [optional] 

### Return type

[**GetNetworkingV1PrivateLinkAttachmentConnection200Response**](GetNetworkingV1PrivateLinkAttachmentConnection200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Link Attachment Connection. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

