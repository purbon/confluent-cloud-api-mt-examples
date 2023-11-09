# openapi_client.AppliedQuotasServiceQuotaV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_quota_v1_applied_quota**](AppliedQuotasServiceQuotaV1Api.md#get_service_quota_v1_applied_quota) | **GET** /service-quota/v1/applied-quotas/{id} | Read an Applied Quota
[**list_service_quota_v1_applied_quotas**](AppliedQuotasServiceQuotaV1Api.md#list_service_quota_v1_applied_quotas) | **GET** /service-quota/v1/applied-quotas | List of Applied Quotas


# **get_service_quota_v1_applied_quota**
> GetServiceQuotaV1AppliedQuota200Response get_service_quota_v1_applied_quota(id, environment=environment, network=network, kafka_cluster=kafka_cluster)

Read an Applied Quota

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Make a request to read an applied quota.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_service_quota_v1_applied_quota200_response import GetServiceQuotaV1AppliedQuota200Response
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
    api_instance = openapi_client.AppliedQuotasServiceQuotaV1Api(api_client)
    id = 'id_example' # str | The unique identifier for the applied quota.
    environment = 'env-00000' # str | The environment ID the quota is associated with. This field is only required when retrieving a single quota and the scope of quota is \"ENVIRONMENT\" or \"NETWORK\" or \"KAFKA_CLUSTER\".  (optional)
    network = 'n-12034' # str | The network ID the quota is associated with. This field is only required when retrieving a single quota and the scope of quota is \"NETWORK\".  (optional)
    kafka_cluster = 'lkc-00000' # str | The kafka cluster ID the quota is associated with. This field is required only when the scope of quota is \"KAFKA_CLUSTER\".  (optional)

    try:
        # Read an Applied Quota
        api_response = api_instance.get_service_quota_v1_applied_quota(id, environment=environment, network=network, kafka_cluster=kafka_cluster)
        print("The response of AppliedQuotasServiceQuotaV1Api->get_service_quota_v1_applied_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliedQuotasServiceQuotaV1Api->get_service_quota_v1_applied_quota: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The unique identifier for the applied quota. | 
 **environment** | **str**| The environment ID the quota is associated with. This field is only required when retrieving a single quota and the scope of quota is \&quot;ENVIRONMENT\&quot; or \&quot;NETWORK\&quot; or \&quot;KAFKA_CLUSTER\&quot;.  | [optional] 
 **network** | **str**| The network ID the quota is associated with. This field is only required when retrieving a single quota and the scope of quota is \&quot;NETWORK\&quot;.  | [optional] 
 **kafka_cluster** | **str**| The kafka cluster ID the quota is associated with. This field is required only when the scope of quota is \&quot;KAFKA_CLUSTER\&quot;.  | [optional] 

### Return type

[**GetServiceQuotaV1AppliedQuota200Response**](GetServiceQuotaV1AppliedQuota200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applied Quota. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**404** | Not Found |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_service_quota_v1_applied_quotas**
> ListServiceQuotaV1AppliedQuotas200Response list_service_quota_v1_applied_quotas(scope, environment=environment, network=network, kafka_cluster=kafka_cluster, id=id, page_size=page_size, page_token=page_token)

List of Applied Quotas

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a sorted, filtered, paginated list of all applied quotas.  Shows all quotas for a given scope. 

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.list_service_quota_v1_applied_quotas200_response import ListServiceQuotaV1AppliedQuotas200Response
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
    api_instance = openapi_client.AppliedQuotasServiceQuotaV1Api(api_client)
    scope = 'ORGANIZATION' # str | The applied scope the quota belongs to. 
    environment = 'env-00000' # str | The environment ID the quota is associated with.  (optional)
    network = 'n-12034' # str | The network ID the quota is associated with.  (optional)
    kafka_cluster = 'lkc-00000' # str | The kafka cluster ID the quota is associated with.  (optional)
    id = 'iam.max_environments.per_org' # str | The id (quota code) that this quota belongs to.  (optional)
    page_size = 10 # int | A pagination size for collection requests. (optional) (default to 10)
    page_token = 'page_token_example' # str | An opaque pagination token for collection requests. (optional)

    try:
        # List of Applied Quotas
        api_response = api_instance.list_service_quota_v1_applied_quotas(scope, environment=environment, network=network, kafka_cluster=kafka_cluster, id=id, page_size=page_size, page_token=page_token)
        print("The response of AppliedQuotasServiceQuotaV1Api->list_service_quota_v1_applied_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppliedQuotasServiceQuotaV1Api->list_service_quota_v1_applied_quotas: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The applied scope the quota belongs to.  | 
 **environment** | **str**| The environment ID the quota is associated with.  | [optional] 
 **network** | **str**| The network ID the quota is associated with.  | [optional] 
 **kafka_cluster** | **str**| The kafka cluster ID the quota is associated with.  | [optional] 
 **id** | **str**| The id (quota code) that this quota belongs to.  | [optional] 
 **page_size** | **int**| A pagination size for collection requests. | [optional] [default to 10]
 **page_token** | **str**| An opaque pagination token for collection requests. | [optional] 

### Return type

[**ListServiceQuotaV1AppliedQuotas200Response**](ListServiceQuotaV1AppliedQuotas200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applied Quota. |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  |
**400** | Bad Request |  * X-Request-Id - The unique identifier for the API request. <br>  |
**401** | The request lacks valid authentication credentials for this resource. |  * X-Request-Id - The unique identifier for the API request. <br>  * WWW-Authenticate - The unique identifier for the API request. <br>  |
**403** | The access credentials were considered insufficient to grant access |  * X-Request-Id - The unique identifier for the API request. <br>  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Oops, something went wrong! |  * X-Request-Id - The unique identifier for the API request. <br>  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

