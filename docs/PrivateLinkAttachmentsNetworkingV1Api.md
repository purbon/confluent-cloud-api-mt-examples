# openapi_client.PrivateLinkAttachmentsNetworkingV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_networking_v1_private_link_attachment**](PrivateLinkAttachmentsNetworkingV1Api.md#create_networking_v1_private_link_attachment) | **POST** /networking/v1/private-link-attachments | Create a Private Link Attachment
[**delete_networking_v1_private_link_attachment**](PrivateLinkAttachmentsNetworkingV1Api.md#delete_networking_v1_private_link_attachment) | **DELETE** /networking/v1/private-link-attachments/{id} | Delete a Private Link Attachment
[**get_networking_v1_private_link_attachment**](PrivateLinkAttachmentsNetworkingV1Api.md#get_networking_v1_private_link_attachment) | **GET** /networking/v1/private-link-attachments/{id} | Read a Private Link Attachment
[**list_networking_v1_private_link_attachments**](PrivateLinkAttachmentsNetworkingV1Api.md#list_networking_v1_private_link_attachments) | **GET** /networking/v1/private-link-attachments | List of Private Link Attachments
[**update_networking_v1_private_link_attachment**](PrivateLinkAttachmentsNetworkingV1Api.md#update_networking_v1_private_link_attachment) | **PATCH** /networking/v1/private-link-attachments/{id} | Update a Private Link Attachment


# **create_networking_v1_private_link_attachment**
> CreateNetworkingV1PrivateLinkAttachment202Response create_networking_v1_private_link_attachment(create_networking_v1_private_link_attachment_request=create_networking_v1_private_link_attachment_request)

Create a Private Link Attachment

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a private link attachment.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.create_networking_v1_private_link_attachment202_response import CreateNetworkingV1PrivateLinkAttachment202Response
from openapi_client.models.create_networking_v1_private_link_attachment_request import CreateNetworkingV1PrivateLinkAttachmentRequest
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
    api_instance = openapi_client.PrivateLinkAttachmentsNetworkingV1Api(api_client)
    create_networking_v1_private_link_attachment_request = openapi_client.CreateNetworkingV1PrivateLinkAttachmentRequest() # CreateNetworkingV1PrivateLinkAttachmentRequest |  (optional)

    try:
        # Create a Private Link Attachment
        api_response = api_instance.create_networking_v1_private_link_attachment(create_networking_v1_private_link_attachment_request=create_networking_v1_private_link_attachment_request)
        print("The response of PrivateLinkAttachmentsNetworkingV1Api->create_networking_v1_private_link_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentsNetworkingV1Api->create_networking_v1_private_link_attachment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_networking_v1_private_link_attachment_request** | [**CreateNetworkingV1PrivateLinkAttachmentRequest**](CreateNetworkingV1PrivateLinkAttachmentRequest.md)|  | [optional] 

### Return type

[**CreateNetworkingV1PrivateLinkAttachment202Response**](CreateNetworkingV1PrivateLinkAttachment202Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | A Private Link Attachment is being created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - PrivateLinkAttachment resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_networking_v1_private_link_attachment**
> delete_networking_v1_private_link_attachment(environment, id)

Delete a Private Link Attachment

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a private link attachment.

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
    api_instance = openapi_client.PrivateLinkAttachmentsNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the private link attachment.

    try:
        # Delete a Private Link Attachment
        api_instance.delete_networking_v1_private_link_attachment(environment, id)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentsNetworkingV1Api->delete_networking_v1_private_link_attachment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the private link attachment. | 

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
**204** | A Private Link Attachment is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_networking_v1_private_link_attachment**
> GetNetworkingV1PrivateLinkAttachment200Response get_networking_v1_private_link_attachment(environment, id)

Read a Private Link Attachment

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a private link attachment.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_private_link_attachment200_response import GetNetworkingV1PrivateLinkAttachment200Response
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
    api_instance = openapi_client.PrivateLinkAttachmentsNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Scope the operation to the given environment.
    id = 'id_example' # str | The unique identifier for the private link attachment.

    try:
        # Read a Private Link Attachment
        api_response = api_instance.get_networking_v1_private_link_attachment(environment, id)
        print("The response of PrivateLinkAttachmentsNetworkingV1Api->get_networking_v1_private_link_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentsNetworkingV1Api->get_networking_v1_private_link_attachment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Scope the operation to the given environment. | 
 **id** | **str**| The unique identifier for the private link attachment. | 

### Return type

[**GetNetworkingV1PrivateLinkAttachment200Response**](GetNetworkingV1PrivateLinkAttachment200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Link Attachment. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_networking_v1_private_link_attachments**
> ListNetworkingV1PrivateLinkAttachments200Response list_networking_v1_private_link_attachments(environment, spec_display_name=spec_display_name, spec_cloud=spec_cloud, spec_region=spec_region, status_phase=status_phase, page_size=page_size, page_token=page_token)

List of Private Link Attachments

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all private link attachments.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.list_networking_v1_private_link_attachments200_response import ListNetworkingV1PrivateLinkAttachments200Response
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
    api_instance = openapi_client.PrivateLinkAttachmentsNetworkingV1Api(api_client)
    environment = 'env-00000' # str | Filter the results by exact match for environment.
    spec_display_name = ['[\"prod-gcp-us-central1\",\"prod-aws-useast1\"]'] # List[str] | Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. (optional)
    spec_cloud = ['[\"GCP\",\"AWS\"]'] # List[str] | Filter the results by exact match for spec.cloud. Pass multiple times to see results matching any of the values. (optional)
    spec_region = ['[\"us-central1\",\"us-east-1\"]'] # List[str] | Filter the results by exact match for spec.region. Pass multiple times to see results matching any of the values. (optional)
    status_phase = ['[\"PROVISIONING\",\"READY\"]'] # List[str] | Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Private Link Attachments
        api_response = api_instance.list_networking_v1_private_link_attachments(environment, spec_display_name=spec_display_name, spec_cloud=spec_cloud, spec_region=spec_region, status_phase=status_phase, page_size=page_size, page_token=page_token)
        print("The response of PrivateLinkAttachmentsNetworkingV1Api->list_networking_v1_private_link_attachments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentsNetworkingV1Api->list_networking_v1_private_link_attachments: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment** | **str**| Filter the results by exact match for environment. | 
 **spec_display_name** | [**List[str]**](str.md)| Filter the results by exact match for spec.display_name. Pass multiple times to see results matching any of the values. | [optional] 
 **spec_cloud** | [**List[str]**](str.md)| Filter the results by exact match for spec.cloud. Pass multiple times to see results matching any of the values. | [optional] 
 **spec_region** | [**List[str]**](str.md)| Filter the results by exact match for spec.region. Pass multiple times to see results matching any of the values. | [optional] 
 **status_phase** | [**List[str]**](str.md)| Filter the results by exact match for status.phase. Pass multiple times to see results matching any of the values. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListNetworkingV1PrivateLinkAttachments200Response**](ListNetworkingV1PrivateLinkAttachments200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Link Attachment. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_networking_v1_private_link_attachment**
> GetNetworkingV1PrivateLinkAttachment200Response update_networking_v1_private_link_attachment(id, update_networking_v1_private_link_attachment_request=update_networking_v1_private_link_attachment_request)

Update a Private Link Attachment

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to update a private link attachment.  

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_networking_v1_private_link_attachment200_response import GetNetworkingV1PrivateLinkAttachment200Response
from openapi_client.models.update_networking_v1_private_link_attachment_request import UpdateNetworkingV1PrivateLinkAttachmentRequest
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
    api_instance = openapi_client.PrivateLinkAttachmentsNetworkingV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the private link attachment.
    update_networking_v1_private_link_attachment_request = openapi_client.UpdateNetworkingV1PrivateLinkAttachmentRequest() # UpdateNetworkingV1PrivateLinkAttachmentRequest |  (optional)

    try:
        # Update a Private Link Attachment
        api_response = api_instance.update_networking_v1_private_link_attachment(id, update_networking_v1_private_link_attachment_request=update_networking_v1_private_link_attachment_request)
        print("The response of PrivateLinkAttachmentsNetworkingV1Api->update_networking_v1_private_link_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivateLinkAttachmentsNetworkingV1Api->update_networking_v1_private_link_attachment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the private link attachment. | 
 **update_networking_v1_private_link_attachment_request** | [**UpdateNetworkingV1PrivateLinkAttachmentRequest**](UpdateNetworkingV1PrivateLinkAttachmentRequest.md)|  | [optional] 

### Return type

[**GetNetworkingV1PrivateLinkAttachment200Response**](GetNetworkingV1PrivateLinkAttachment200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Private Link Attachment. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**402** | The request would exceed one or more quotas. |  * X-Request-Id - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

