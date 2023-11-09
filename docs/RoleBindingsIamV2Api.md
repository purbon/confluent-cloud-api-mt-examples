# openapi_client.RoleBindingsIamV2Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_iam_v2_role_binding**](RoleBindingsIamV2Api.md#create_iam_v2_role_binding) | **POST** /iam/v2/role-bindings | Create a Role Binding
[**delete_iam_v2_role_binding**](RoleBindingsIamV2Api.md#delete_iam_v2_role_binding) | **DELETE** /iam/v2/role-bindings/{id} | Delete a Role Binding
[**get_iam_v2_role_binding**](RoleBindingsIamV2Api.md#get_iam_v2_role_binding) | **GET** /iam/v2/role-bindings/{id} | Read a Role Binding
[**list_iam_v2_role_bindings**](RoleBindingsIamV2Api.md#list_iam_v2_role_bindings) | **GET** /iam/v2/role-bindings | List of Role Bindings


# **create_iam_v2_role_binding**
> CreateIamV2RoleBindingRequest create_iam_v2_role_binding(create_iam_v2_role_binding_request=create_iam_v2_role_binding_request)

Create a Role Binding

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to create a role binding.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.create_iam_v2_role_binding_request import CreateIamV2RoleBindingRequest
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
    api_instance = openapi_client.RoleBindingsIamV2Api(api_client)
    create_iam_v2_role_binding_request = openapi_client.CreateIamV2RoleBindingRequest() # CreateIamV2RoleBindingRequest |  (optional)

    try:
        # Create a Role Binding
        api_response = api_instance.create_iam_v2_role_binding(create_iam_v2_role_binding_request=create_iam_v2_role_binding_request)
        print("The response of RoleBindingsIamV2Api->create_iam_v2_role_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBindingsIamV2Api->create_iam_v2_role_binding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_iam_v2_role_binding_request** | [**CreateIamV2RoleBindingRequest**](CreateIamV2RoleBindingRequest.md)|  | [optional] 

### Return type

[**CreateIamV2RoleBindingRequest**](CreateIamV2RoleBindingRequest.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Role Binding was created. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Location - RoleBinding resource uri <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**422** | Validation Failed |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_iam_v2_role_binding**
> GetIamV2RoleBinding200Response delete_iam_v2_role_binding(id)

Delete a Role Binding

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to delete a role binding.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_iam_v2_role_binding200_response import GetIamV2RoleBinding200Response
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
    api_instance = openapi_client.RoleBindingsIamV2Api(api_client)
    id = 'id_example' # str | The unique identifier for the role binding.

    try:
        # Delete a Role Binding
        api_response = api_instance.delete_iam_v2_role_binding(id)
        print("The response of RoleBindingsIamV2Api->delete_iam_v2_role_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBindingsIamV2Api->delete_iam_v2_role_binding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role binding. | 

### Return type

[**GetIamV2RoleBinding200Response**](GetIamV2RoleBinding200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Role Binding is being deleted. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_iam_v2_role_binding**
> GetIamV2RoleBinding200Response get_iam_v2_role_binding(id)

Read a Role Binding

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read a role binding.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_iam_v2_role_binding200_response import GetIamV2RoleBinding200Response
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
    api_instance = openapi_client.RoleBindingsIamV2Api(api_client)
    id = 'id_example' # str | The unique identifier for the role binding.

    try:
        # Read a Role Binding
        api_response = api_instance.get_iam_v2_role_binding(id)
        print("The response of RoleBindingsIamV2Api->get_iam_v2_role_binding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBindingsIamV2Api->get_iam_v2_role_binding: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the role binding. | 

### Return type

[**GetIamV2RoleBinding200Response**](GetIamV2RoleBinding200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role Binding. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_iam_v2_role_bindings**
> IamV2RoleBindingList list_iam_v2_role_bindings(crn_pattern, principal=principal, role_name=role_name, page_size=page_size, page_token=page_token)

List of Role Bindings

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all role bindings.

### Example

* Basic Authentication (api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.iam_v2_role_binding_list import IamV2RoleBindingList
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
    api_instance = openapi_client.RoleBindingsIamV2Api(api_client)
    crn_pattern = 'crn://confluent.cloud/organization=1111aaaa-11aa-11aa-11aa-111111aaaaaa/environment=env-aaa1111/cloud-cluster=lkc-1111aaa' # str | Filter the results by a partial search of crn_pattern.
    principal = 'User:u-111aaa' # str | Filter the results by exact match for principal. (optional)
    role_name = 'CloudClusterAdmin' # str | Filter the results by exact match for role_name. (optional)
    page_size = 100 # int | A pagination size for collection requests. (optional) (default to 100)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Role Bindings
        api_response = api_instance.list_iam_v2_role_bindings(crn_pattern, principal=principal, role_name=role_name, page_size=page_size, page_token=page_token)
        print("The response of RoleBindingsIamV2Api->list_iam_v2_role_bindings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoleBindingsIamV2Api->list_iam_v2_role_bindings: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **crn_pattern** | **str**| Filter the results by a partial search of crn_pattern. | 
 **principal** | **str**| Filter the results by exact match for principal. | [optional] 
 **role_name** | **str**| Filter the results by exact match for role_name. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 100]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**IamV2RoleBindingList**](IamV2RoleBindingList.md)

### Authorization

[api-key](../ccloud/README.md#api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Role Binding. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

