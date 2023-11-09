# openapi_client.ConnectorsConnectV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connectv1_connector**](ConnectorsConnectV1Api.md#create_connectv1_connector) | **POST** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors | Create a Connector
[**create_or_update_connectv1_connector_config**](ConnectorsConnectV1Api.md#create_or_update_connectv1_connector_config) | **PUT** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/config | Create or Update a Connector Configuration
[**delete_connectv1_connector**](ConnectorsConnectV1Api.md#delete_connectv1_connector) | **DELETE** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name} | Delete a Connector
[**get_connectv1_connector_config**](ConnectorsConnectV1Api.md#get_connectv1_connector_config) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name}/config | Read a Connector Configuration
[**list_connectv1_connectors**](ConnectorsConnectV1Api.md#list_connectv1_connectors) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors | List of Connectors
[**list_connectv1_connectors_with_expansions**](ConnectorsConnectV1Api.md#list_connectv1_connectors_with_expansions) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors?expand&#x3D;info,status,id | List of Connectors with Expansions
[**read_connectv1_connector**](ConnectorsConnectV1Api.md#read_connectv1_connector) | **GET** /connect/v1/environments/{environment_id}/clusters/{kafka_cluster_id}/connectors/{connector_name} | Read a Connector


# **create_connectv1_connector**
> ConnectV1Connector create_connectv1_connector(environment_id, kafka_cluster_id, create_connectv1_connector_request=create_connectv1_connector_request)

Create a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Create a new connector. Returns the new connector information if successful.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.connect_v1_connector import ConnectV1Connector
from openapi_client.models.create_connectv1_connector_request import CreateConnectv1ConnectorRequest
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
    api_instance = openapi_client.ConnectorsConnectV1Api(api_client)
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.
    create_connectv1_connector_request = {"name":"MyGcsLogsBucketConnector","config":{"connector.class":"GcsSink","data.format":"BYTES","flush.size":"1000","gcs.bucket.name":"APILogsBucket","gcs.credentials.config":"****************","kafka.api.key":"****************","kafka.api.secret":"****************","name":"MyGcsLogsBucketConnector","tasks.max":"2","time.interval":"DAILY","topics":"APILogsTopic"}} # CreateConnectv1ConnectorRequest |  (optional)

    try:
        # Create a Connector
        api_response = api_instance.create_connectv1_connector(environment_id, kafka_cluster_id, create_connectv1_connector_request=create_connectv1_connector_request)
        print("The response of ConnectorsConnectV1Api->create_connectv1_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsConnectV1Api->create_connectv1_connector: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 
 **create_connectv1_connector_request** | [**CreateConnectv1ConnectorRequest**](CreateConnectv1ConnectorRequest.md)|  | [optional] 

### Return type

[**ConnectV1Connector**](ConnectV1Connector.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **create_or_update_connectv1_connector_config**
> ConnectV1Connector create_or_update_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id, request_body=request_body)

Create or Update a Connector Configuration

Create a new connector using the given configuration, or update the configuration for an existing connector. Returns information about the connector after the change has been made.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.connect_v1_connector import ConnectV1Connector
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
    api_instance = openapi_client.ConnectorsConnectV1Api(api_client)
    connector_name = 'connector_name_example' # str | The unique name of the connector.
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.
    request_body = {"connector.class":"GcsSink","data.format":"BYTES","flush.size":"1000","gcs.bucket.name":"APILogsBucket","gcs.credentials.config":"****************","kafka.api.key":"****************","kafka.api.secret":"****************","name":"MyGcsLogsBucketConnector","tasks.max":"2","time.interval":"DAILY","topics":"APILogsTopic"} # Dict[str, str] | Configuration parameters for the connector. All values should be strings. (optional)

    try:
        # Create or Update a Connector Configuration
        api_response = api_instance.create_or_update_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id, request_body=request_body)
        print("The response of ConnectorsConnectV1Api->create_or_update_connectv1_connector_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsConnectV1Api->create_or_update_connectv1_connector_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. | 
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 
 **request_body** | [**Dict[str, str]**](str.md)| Configuration parameters for the connector. All values should be strings. | [optional] 

### Return type

[**ConnectV1Connector**](ConnectV1Connector.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_connectv1_connector**
> DeleteConnectv1Connector200Response delete_connectv1_connector(connector_name, environment_id, kafka_cluster_id)

Delete a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete a connector. Halts all tasks and deletes the connector configuration.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.delete_connectv1_connector200_response import DeleteConnectv1Connector200Response
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
    api_instance = openapi_client.ConnectorsConnectV1Api(api_client)
    connector_name = 'connector_name_example' # str | The unique name of the connector.
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.

    try:
        # Delete a Connector
        api_response = api_instance.delete_connectv1_connector(connector_name, environment_id, kafka_cluster_id)
        print("The response of ConnectorsConnectV1Api->delete_connectv1_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsConnectV1Api->delete_connectv1_connector: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. | 
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 

### Return type

[**DeleteConnectv1Connector200Response**](DeleteConnectv1Connector200Response.md)

### Authorization

[cloud-api-key](../ccloud/README.md#cloud-api-key), [confluent-sts-access-token](../ccloud/README.md#confluent-sts-access-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_connectv1_connector_config**
> GetConnectv1ConnectorConfig200Response get_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id)

Read a Connector Configuration

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get the configuration for the connector.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.get_connectv1_connector_config200_response import GetConnectv1ConnectorConfig200Response
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
    api_instance = openapi_client.ConnectorsConnectV1Api(api_client)
    connector_name = 'connector_name_example' # str | The unique name of the connector.
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.

    try:
        # Read a Connector Configuration
        api_response = api_instance.get_connectv1_connector_config(connector_name, environment_id, kafka_cluster_id)
        print("The response of ConnectorsConnectV1Api->get_connectv1_connector_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsConnectV1Api->get_connectv1_connector_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. | 
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 

### Return type

[**GetConnectv1ConnectorConfig200Response**](GetConnectv1ConnectorConfig200Response.md)

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

# **list_connectv1_connectors**
> List[str] list_connectv1_connectors(environment_id, kafka_cluster_id)

List of Connectors

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve a list of \"names\" of the active connectors. You can then make a [read request](#operation/readConnectv1Connector) for a specific connector by name.

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
    api_instance = openapi_client.ConnectorsConnectV1Api(api_client)
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.

    try:
        # List of Connectors
        api_response = api_instance.list_connectv1_connectors(environment_id, kafka_cluster_id)
        print("The response of ConnectorsConnectV1Api->list_connectv1_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsConnectV1Api->list_connectv1_connectors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 

### Return type

**List[str]**

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

# **list_connectv1_connectors_with_expansions**
> Dict[str, ConnectV1ConnectorExpansion] list_connectv1_connectors_with_expansions(environment_id, kafka_cluster_id, expand=expand)

List of Connectors with Expansions

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Retrieve an object with the queried expansions of all connectors. Without `expand` query parameter, this list connector’s endpoint will return a [list of only the connector names](#operation/listConnectv1Connectors).

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.connect_v1_connector_expansion import ConnectV1ConnectorExpansion
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
    api_instance = openapi_client.ConnectorsConnectV1Api(api_client)
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.
    expand = 'expand_example' # str | - id : Returns metadata of each connector such as id and id type. - info : Returns metadata of each connector such as the configuration, task information, and type of connector. - status : Returns additional state information of each connector including their status and tasks. (optional)

    try:
        # List of Connectors with Expansions
        api_response = api_instance.list_connectv1_connectors_with_expansions(environment_id, kafka_cluster_id, expand=expand)
        print("The response of ConnectorsConnectV1Api->list_connectv1_connectors_with_expansions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsConnectV1Api->list_connectv1_connectors_with_expansions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 
 **expand** | **str**| - id : Returns metadata of each connector such as id and id type. - info : Returns metadata of each connector such as the configuration, task information, and type of connector. - status : Returns additional state information of each connector including their status and tasks. | [optional] 

### Return type

[**Dict[str, ConnectV1ConnectorExpansion]**](ConnectV1ConnectorExpansion.md)

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

# **read_connectv1_connector**
> ConnectV1Connector read_connectv1_connector(connector_name, environment_id, kafka_cluster_id)

Read a Connector

[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get information about the connector.

### Example

* Basic Authentication (cloud-api-key):
* OAuth Authentication (confluent-sts-access-token):
```python
import time
import os
import openapi_client
from openapi_client.models.connect_v1_connector import ConnectV1Connector
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
    api_instance = openapi_client.ConnectorsConnectV1Api(api_client)
    connector_name = 'connector_name_example' # str | The unique name of the connector.
    environment_id = 'environment_id_example' # str | The unique identifier of the environment this resource belongs to.
    kafka_cluster_id = 'kafka_cluster_id_example' # str | The unique identifier for the Kafka cluster.

    try:
        # Read a Connector
        api_response = api_instance.read_connectv1_connector(connector_name, environment_id, kafka_cluster_id)
        print("The response of ConnectorsConnectV1Api->read_connectv1_connector:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorsConnectV1Api->read_connectv1_connector: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_name** | **str**| The unique name of the connector. | 
 **environment_id** | **str**| The unique identifier of the environment this resource belongs to. | 
 **kafka_cluster_id** | **str**| The unique identifier for the Kafka cluster. | 

### Return type

[**ConnectV1Connector**](ConnectV1Connector.md)

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

