# openapi_client.SharedTokensCdxV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**redeem_cdx_v1_shared_token**](SharedTokensCdxV1Api.md#redeem_cdx_v1_shared_token) | **POST** /cdx/v1/shared-tokens:redeem | Redeem token
[**resources_cdx_v1_shared_token**](SharedTokensCdxV1Api.md#resources_cdx_v1_shared_token) | **POST** /cdx/v1/shared-tokens:resources | Validate token to view shared resources


# **redeem_cdx_v1_shared_token**
> CdxV1RedeemTokenResponse redeem_cdx_v1_shared_token(redeem_cdx_v1_shared_token_request=redeem_cdx_v1_shared_token_request)

Redeem token

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Redeem the shared token for shared topic and cluster access information

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.cdx_v1_redeem_token_response import CdxV1RedeemTokenResponse
from openapi_client.models.redeem_cdx_v1_shared_token_request import RedeemCdxV1SharedTokenRequest
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
    api_instance = openapi_client.SharedTokensCdxV1Api(api_client)
    redeem_cdx_v1_shared_token_request = openapi_client.RedeemCdxV1SharedTokenRequest() # RedeemCdxV1SharedTokenRequest |  (optional)

    try:
        # Redeem token
        api_response = api_instance.redeem_cdx_v1_shared_token(redeem_cdx_v1_shared_token_request=redeem_cdx_v1_shared_token_request)
        print("The response of SharedTokensCdxV1Api->redeem_cdx_v1_shared_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedTokensCdxV1Api->redeem_cdx_v1_shared_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redeem_cdx_v1_shared_token_request** | [**RedeemCdxV1SharedTokenRequest**](RedeemCdxV1SharedTokenRequest.md)|  | [optional] 

### Return type

[**CdxV1RedeemTokenResponse**](CdxV1RedeemTokenResponse.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer redeems shared token  |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **resources_cdx_v1_shared_token**
> ResourcesCdxV1SharedToken200Response resources_cdx_v1_shared_token(resources_cdx_v1_shared_token_request=resources_cdx_v1_shared_token_request)

Validate token to view shared resources

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Validate and decrypt the shared token and view token's shared resources

### Example

* Basic Authentication (api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.resources_cdx_v1_shared_token200_response import ResourcesCdxV1SharedToken200Response
from openapi_client.models.resources_cdx_v1_shared_token_request import ResourcesCdxV1SharedTokenRequest
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
    api_instance = openapi_client.SharedTokensCdxV1Api(api_client)
    resources_cdx_v1_shared_token_request = openapi_client.ResourcesCdxV1SharedTokenRequest() # ResourcesCdxV1SharedTokenRequest |  (optional)

    try:
        # Validate token to view shared resources
        api_response = api_instance.resources_cdx_v1_shared_token(resources_cdx_v1_shared_token_request=resources_cdx_v1_shared_token_request)
        print("The response of SharedTokensCdxV1Api->resources_cdx_v1_shared_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedTokensCdxV1Api->resources_cdx_v1_shared_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resources_cdx_v1_shared_token_request** | [**ResourcesCdxV1SharedTokenRequest**](ResourcesCdxV1SharedTokenRequest.md)|  | [optional] 

### Return type

[**ResourcesCdxV1SharedToken200Response**](ResourcesCdxV1SharedToken200Response.md)

### Authorization

[api-key](../ccloud/README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Consumer validates share token and view consumer resources before redeeming in the workflow  |  -  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**409** | The request is in conflict with the current server state |  * X-Request-Id - The unique identifier for the API request. <br>  * Location - Resource URI of conflicting resource <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

