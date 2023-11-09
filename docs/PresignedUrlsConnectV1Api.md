# openapi_client.PresignedUrlsConnectV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**presigned_upload_url_connect_v1_presigned_url**](PresignedUrlsConnectV1Api.md#presigned_upload_url_connect_v1_presigned_url) | **POST** /connect/v1/presigned-upload-url | Request a presigned upload URL for a new Custom Connector Plugin.


# **presigned_upload_url_connect_v1_presigned_url**
> PresignedUploadUrlConnectV1PresignedUrl200Response presigned_upload_url_connect_v1_presigned_url(presigned_upload_url_connect_v1_presigned_url_request=presigned_upload_url_connect_v1_presigned_url_request)

Request a presigned upload URL for a new Custom Connector Plugin.

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Request a presigned upload URL to upload a Custom Connector Plugin archive.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.presigned_upload_url_connect_v1_presigned_url200_response import PresignedUploadUrlConnectV1PresignedUrl200Response
from openapi_client.models.presigned_upload_url_connect_v1_presigned_url_request import PresignedUploadUrlConnectV1PresignedUrlRequest
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
    api_instance = openapi_client.PresignedUrlsConnectV1Api(api_client)
    presigned_upload_url_connect_v1_presigned_url_request = openapi_client.PresignedUploadUrlConnectV1PresignedUrlRequest() # PresignedUploadUrlConnectV1PresignedUrlRequest |  (optional)

    try:
        # Request a presigned upload URL for a new Custom Connector Plugin.
        api_response = api_instance.presigned_upload_url_connect_v1_presigned_url(presigned_upload_url_connect_v1_presigned_url_request=presigned_upload_url_connect_v1_presigned_url_request)
        print("The response of PresignedUrlsConnectV1Api->presigned_upload_url_connect_v1_presigned_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PresignedUrlsConnectV1Api->presigned_upload_url_connect_v1_presigned_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **presigned_upload_url_connect_v1_presigned_url_request** | [**PresignedUploadUrlConnectV1PresignedUrlRequest**](PresignedUploadUrlConnectV1PresignedUrlRequest.md)|  | [optional] 

### Return type

[**PresignedUploadUrlConnectV1PresignedUrl200Response**](PresignedUploadUrlConnectV1PresignedUrl200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Presigned Url. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

