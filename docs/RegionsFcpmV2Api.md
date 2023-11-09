# openapi_client.RegionsFcpmV2Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fcpm_v2_regions**](RegionsFcpmV2Api.md#list_fcpm_v2_regions) | **GET** /fcpm/v2/regions | List of Regions


# **list_fcpm_v2_regions**
> FcpmV2RegionList list_fcpm_v2_regions(cloud=cloud, region_name=region_name, page_size=page_size, page_token=page_token)

List of Regions

[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all regions.

### Example

* Basic Authentication (cloud-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.fcpm_v2_region_list import FcpmV2RegionList
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
    api_instance = openapi_client.RegionsFcpmV2Api(api_client)
    cloud = 'AWS' # str | Filter the results by exact match for cloud. (optional)
    region_name = 'us-east-2' # str | Filter the results by exact match for region_name. (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Regions
        api_response = api_instance.list_fcpm_v2_regions(cloud=cloud, region_name=region_name, page_size=page_size, page_token=page_token)
        print("The response of RegionsFcpmV2Api->list_fcpm_v2_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionsFcpmV2Api->list_fcpm_v2_regions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cloud** | **str**| Filter the results by exact match for cloud. | [optional] 
 **region_name** | **str**| Filter the results by exact match for region_name. | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**FcpmV2RegionList**](FcpmV2RegionList.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Region. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

