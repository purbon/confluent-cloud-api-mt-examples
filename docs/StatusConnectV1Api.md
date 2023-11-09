# openapi_client.StatusConnectV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_connectv1_connector_tasks**](StatusConnectV1Api.md#list_connectv1_connector_tasks) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/tasks | List of Connector Tasks
[**read_connectv1_connector_status**](StatusConnectV1Api.md#read_connectv1_connector_status) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/status | Read a Connector Status


# **list_connectv1_connector_tasks**
> List[ConnectV1ConnectorsInner] list_connectv1_connector_tasks(connector_name, environment_id, kafka_cluster_id)

List of Connector Tasks

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get a list of tasks currently running for the connector.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.connect_v1_connectors_inner import ConnectV1ConnectorsInner
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
    api_instance = openapi_client.StatusConnectV1Api(api_client)
    connector_name = 'connector_name_example' # str | The unique name of the connector.
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.

    try:
        # List of Connector Tasks
        api_response = api_instance.list_connectv1_connector_tasks(connector_name, environment_id, kafka_cluster_id)
        print("The response of StatusConnectV1Api->list_connectv1_connector_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusConnectV1Api->list_connectv1_connector_tasks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. | 
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 

### Return type

[**List[ConnectV1ConnectorsInner]**](ConnectV1ConnectorsInner.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector Task. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **read_connectv1_connector_status**
> ReadConnectv1ConnectorStatus200Response read_connectv1_connector_status(connector_name, environment_id, kafka_cluster_id)

Read a Connector Status

Get current status of the connector. This includes whether it is running, failed, or paused. Also includes which worker it is assigned to, error information if it has failed, and the state of all its tasks.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.read_connectv1_connector_status200_response import ReadConnectv1ConnectorStatus200Response
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
    api_instance = openapi_client.StatusConnectV1Api(api_client)
    connector_name = 'connector_name_example' # str | The unique name of the connector.
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.

    try:
        # Read a Connector Status
        api_response = api_instance.read_connectv1_connector_status(connector_name, environment_id, kafka_cluster_id)
        print("The response of StatusConnectV1Api->read_connectv1_connector_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusConnectV1Api->read_connectv1_connector_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. | 
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 

### Return type

[**ReadConnectv1ConnectorStatus200Response**](ReadConnectv1ConnectorStatus200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connector. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

