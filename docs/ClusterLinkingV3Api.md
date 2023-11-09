# openapi_client.ClusterLinkingV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kafka_link**](ClusterLinkingV3Api.md#create_kafka_link) | **POST** /kafka/v3/clusters/{cluster_id}/links | Create a cluster link
[**create_kafka_mirror_topic**](ClusterLinkingV3Api.md#create_kafka_mirror_topic) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors | Create a mirror topic
[**delete_kafka_link**](ClusterLinkingV3Api.md#delete_kafka_link) | **DELETE** /kafka/v3/clusters/{cluster_id}/links/{link_name} | Delete the cluster link
[**delete_kafka_link_config**](ClusterLinkingV3Api.md#delete_kafka_link_config) | **DELETE** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Reset the given config to default value
[**get_kafka_link**](ClusterLinkingV3Api.md#get_kafka_link) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name} | Describe the cluster link
[**get_kafka_link_configs**](ClusterLinkingV3Api.md#get_kafka_link_configs) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Describe the config under the cluster link
[**list_kafka_link_configs**](ClusterLinkingV3Api.md#list_kafka_link_configs) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs | List all configs of the cluster link
[**list_kafka_links**](ClusterLinkingV3Api.md#list_kafka_links) | **GET** /kafka/v3/clusters/{cluster_id}/links | List all cluster links in the dest cluster
[**list_kafka_mirror_topics**](ClusterLinkingV3Api.md#list_kafka_mirror_topics) | **GET** /kafka/v3/clusters/{cluster_id}/links/-/mirrors | List mirror topics
[**list_kafka_mirror_topics_under_link**](ClusterLinkingV3Api.md#list_kafka_mirror_topics_under_link) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors | List mirror topics
[**read_kafka_mirror_topic**](ClusterLinkingV3Api.md#read_kafka_mirror_topic) | **GET** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors/{mirror_topic_name} | Describe the mirror topic
[**update_kafka_link_config**](ClusterLinkingV3Api.md#update_kafka_link_config) | **PUT** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs/{config_name} | Alter the config under the cluster link
[**update_kafka_link_config_batch**](ClusterLinkingV3Api.md#update_kafka_link_config_batch) | **PUT** /kafka/v3/clusters/{cluster_id}/links/{link_name}/configs:alter | Batch Alter Cluster Link Configs
[**update_kafka_mirror_topics_failover**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_failover) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:failover | Failover the mirror topics
[**update_kafka_mirror_topics_pause**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_pause) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:pause | Pause the mirror topics
[**update_kafka_mirror_topics_promote**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_promote) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:promote | Promote the mirror topics
[**update_kafka_mirror_topics_resume**](ClusterLinkingV3Api.md#update_kafka_mirror_topics_resume) | **POST** /kafka/v3/clusters/{cluster_id}/links/{link_name}/mirrors:resume | Resume the mirror topics


# **create_kafka_link**
> create_kafka_link(cluster_id, link_name, validate_only=validate_only, validate_link=validate_link, create_link_request_data=create_link_request_data)

Create a cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_link_request_data import CreateLinkRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    validate_only = false # bool | To validate the action can be performed successfully or not. Default: false (optional)
    validate_link = false # bool | To synchronously validate that the source cluster ID is expected and the dest cluster has the permission to read topics in the source cluster. Default: true (optional)
    create_link_request_data = {"source_cluster_id":"cluster-1","configs":[{"name":"bootstrap.servers","value":"cluster-1-bootstrap-server"},{"name":"acl.sync.enable","value":"false"},{"name":"consumer.offset.sync.ms","value":"30000"}]} # CreateLinkRequestData | Create a cluster link (optional)

    try:
        # Create a cluster link
        api_instance.create_kafka_link(cluster_id, link_name, validate_only=validate_only, validate_link=validate_link, create_link_request_data=create_link_request_data)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->create_kafka_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional] 
 **validate_link** | **bool**| To synchronously validate that the source cluster ID is expected and the dest cluster has the permission to read topics in the source cluster. Default: true | [optional] 
 **create_link_request_data** | [**CreateLinkRequestData**](CreateLinkRequestData.md)| Create a cluster link | [optional] 

### Return type

void (empty response body)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **create_kafka_mirror_topic**
> create_kafka_mirror_topic(cluster_id, link_name, create_mirror_topic_request_data=create_mirror_topic_request_data)

Create a mirror topic

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Create a topic in the destination cluster mirroring a topic in the source cluster

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.create_mirror_topic_request_data import CreateMirrorTopicRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    create_mirror_topic_request_data = {"source_topic_name":"topic-1","configs":[{"name":"unclean.leader.election.enable","value":"true"}],"replication_factor":1} # CreateMirrorTopicRequestData | Name and configs of the topics mirroring from and mirroring to. Note that Confluent Cloud allows only specific replication factor values. Because of that the replication factor field should either be omitted or it should use one of the allowed values (see https://docs.confluent.io/cloud/current/client-apps/optimizing/durability.html). (optional)

    try:
        # Create a mirror topic
        api_instance.create_kafka_mirror_topic(cluster_id, link_name, create_mirror_topic_request_data=create_mirror_topic_request_data)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->create_kafka_mirror_topic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **create_mirror_topic_request_data** | [**CreateMirrorTopicRequestData**](CreateMirrorTopicRequestData.md)| Name and configs of the topics mirroring from and mirroring to. Note that Confluent Cloud allows only specific replication factor values. Because of that the replication factor field should either be omitted or it should use one of the allowed values (see https://docs.confluent.io/cloud/current/client-apps/optimizing/durability.html). | [optional] 

### Return type

void (empty response body)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_kafka_link**
> delete_kafka_link(cluster_id, link_name, force=force, validate_only=validate_only)

Delete the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    force = false # bool | Force the action. Default: false (optional)
    validate_only = false # bool | To validate the action can be performed successfully or not. Default: false (optional)

    try:
        # Delete the cluster link
        api_instance.delete_kafka_link(cluster_id, link_name, force=force, validate_only=validate_only)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->delete_kafka_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **force** | **bool**| Force the action. Default: false | [optional] 
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional] 

### Return type

void (empty response body)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_kafka_link_config**
> delete_kafka_link_config(cluster_id, link_name, config_name)

Reset the given config to default value

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    config_name = 'consumer.offset.sync.enable' # str | The link config name

    try:
        # Reset the given config to default value
        api_instance.delete_kafka_link_config(cluster_id, link_name, config_name)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->delete_kafka_link_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **config_name** | **str**| The link config name | 

### Return type

void (empty response body)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_kafka_link**
> ListLinksResponseData get_kafka_link(cluster_id, link_name)

Describe the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  ``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_links_response_data import ListLinksResponseData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name

    try:
        # Describe the cluster link
        api_response = api_instance.get_kafka_link(cluster_id, link_name)
        print("The response of ClusterLinkingV3Api->get_kafka_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->get_kafka_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 

### Return type

[**ListLinksResponseData**](ListLinksResponseData.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Single link name and properties |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_kafka_link_configs**
> ListLinkConfigsResponseData get_kafka_link_configs(cluster_id, link_name, config_name)

Describe the config under the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_link_configs_response_data import ListLinkConfigsResponseData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    config_name = 'consumer.offset.sync.enable' # str | The link config name

    try:
        # Describe the config under the cluster link
        api_response = api_instance.get_kafka_link_configs(cluster_id, link_name, config_name)
        print("The response of ClusterLinkingV3Api->get_kafka_link_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->get_kafka_link_configs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **config_name** | **str**| The link config name | 

### Return type

[**ListLinkConfigsResponseData**](ListLinkConfigsResponseData.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config name and value |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_kafka_link_configs**
> ListLinkConfigsResponseDataList list_kafka_link_configs(cluster_id, link_name)

List all configs of the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_link_configs_response_data_list import ListLinkConfigsResponseDataList
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name

    try:
        # List all configs of the cluster link
        api_response = api_instance.list_kafka_link_configs(cluster_id, link_name)
        print("The response of ClusterLinkingV3Api->list_kafka_link_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_link_configs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 

### Return type

[**ListLinkConfigsResponseDataList**](ListLinkConfigsResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Config name and value |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_kafka_links**
> ListLinksResponseDataList list_kafka_links(cluster_id)

List all cluster links in the dest cluster

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  ``link_id`` in ``ListLinksResponseData`` is deprecated and may be removed in a future release. Use the new ``cluster_link_id`` instead.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_links_response_data_list import ListLinksResponseDataList
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.

    try:
        # List all cluster links in the dest cluster
        api_response = api_instance.list_kafka_links(cluster_id)
        print("The response of ClusterLinkingV3Api->list_kafka_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_links: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 

### Return type

[**ListLinksResponseDataList**](ListLinksResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of link names and properties |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_kafka_mirror_topics**
> ListMirrorTopicsResponseDataList list_kafka_mirror_topics(cluster_id, mirror_status=mirror_status)

List mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  List all mirror topics in the cluster

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_mirror_topics_response_data_list import ListMirrorTopicsResponseDataList
from openapi_client.models.mirror_topic_status import MirrorTopicStatus
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    mirror_status = openapi_client.MirrorTopicStatus() # MirrorTopicStatus | The status of the mirror topic. If not specified, all mirror topics will be returned. (optional)

    try:
        # List mirror topics
        api_response = api_instance.list_kafka_mirror_topics(cluster_id, mirror_status=mirror_status)
        print("The response of ClusterLinkingV3Api->list_kafka_mirror_topics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_mirror_topics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **mirror_status** | [**MirrorTopicStatus**](.md)| The status of the mirror topic. If not specified, all mirror topics will be returned. | [optional] 

### Return type

[**ListMirrorTopicsResponseDataList**](ListMirrorTopicsResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of mirror topics |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_kafka_mirror_topics_under_link**
> ListMirrorTopicsResponseDataList list_kafka_mirror_topics_under_link(cluster_id, link_name, mirror_status=mirror_status)

List mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  List all mirror topics under the link

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_mirror_topics_response_data_list import ListMirrorTopicsResponseDataList
from openapi_client.models.mirror_topic_status import MirrorTopicStatus
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    mirror_status = openapi_client.MirrorTopicStatus() # MirrorTopicStatus | The status of the mirror topic. If not specified, all mirror topics will be returned. (optional)

    try:
        # List mirror topics
        api_response = api_instance.list_kafka_mirror_topics_under_link(cluster_id, link_name, mirror_status=mirror_status)
        print("The response of ClusterLinkingV3Api->list_kafka_mirror_topics_under_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->list_kafka_mirror_topics_under_link: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **mirror_status** | [**MirrorTopicStatus**](.md)| The status of the mirror topic. If not specified, all mirror topics will be returned. | [optional] 

### Return type

[**ListMirrorTopicsResponseDataList**](ListMirrorTopicsResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of mirror topics |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **read_kafka_mirror_topic**
> ListMirrorTopicsResponseData read_kafka_mirror_topic(cluster_id, link_name, mirror_topic_name)

Describe the mirror topic

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.list_mirror_topics_response_data import ListMirrorTopicsResponseData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    mirror_topic_name = 'topic-1' # str | Cluster Linking mirror topic name

    try:
        # Describe the mirror topic
        api_response = api_instance.read_kafka_mirror_topic(cluster_id, link_name, mirror_topic_name)
        print("The response of ClusterLinkingV3Api->read_kafka_mirror_topic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->read_kafka_mirror_topic: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **mirror_topic_name** | **str**| Cluster Linking mirror topic name | 

### Return type

[**ListMirrorTopicsResponseData**](ListMirrorTopicsResponseData.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of the mirror topic |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_kafka_link_config**
> update_kafka_link_config(cluster_id, link_name, config_name, update_link_config_request_data=update_link_config_request_data)

Alter the config under the cluster link

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.update_link_config_request_data import UpdateLinkConfigRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    config_name = 'consumer.offset.sync.enable' # str | The link config name
    update_link_config_request_data = {"value":"300000"} # UpdateLinkConfigRequestData | Link config value to update (optional)

    try:
        # Alter the config under the cluster link
        api_instance.update_kafka_link_config(cluster_id, link_name, config_name, update_link_config_request_data=update_link_config_request_data)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_link_config: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **config_name** | **str**| The link config name | 
 **update_link_config_request_data** | [**UpdateLinkConfigRequestData**](UpdateLinkConfigRequestData.md)| Link config value to update | [optional] 

### Return type

void (empty response body)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Operation succeeded, no content in the response |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_kafka_link_config_batch**
> update_kafka_link_config_batch(cluster_id, link_name, validate_only=validate_only, alter_config_batch_request_data=alter_config_batch_request_data)

Batch Alter Cluster Link Configs

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Batch Alter Cluster Link Configs

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.alter_config_batch_request_data import AlterConfigBatchRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    validate_only = false # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_config_batch_request_data = {"data":[{"name":"cleanup.policy","operation":"DELETE"},{"name":"compression.type","value":"gzip"}]} # AlterConfigBatchRequestData |  (optional)

    try:
        # Batch Alter Cluster Link Configs
        api_instance.update_kafka_link_config_batch(cluster_id, link_name, validate_only=validate_only, alter_config_batch_request_data=alter_config_batch_request_data)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_link_config_batch: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional] 
 **alter_config_batch_request_data** | [**AlterConfigBatchRequestData**](AlterConfigBatchRequestData.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_kafka_mirror_topics_failover**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_failover(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)

Failover the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
from openapi_client.models.alter_mirrors_request_data import AlterMirrorsRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    validate_only = false # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = {"mirror_topic_names":["topic-1","topic-2"]} # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    try:
        # Failover the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_failover(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        print("The response of ClusterLinkingV3Api->update_kafka_mirror_topics_failover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_failover: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional] 
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional] 

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_kafka_mirror_topics_pause**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_pause(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)

Pause the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
from openapi_client.models.alter_mirrors_request_data import AlterMirrorsRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    validate_only = false # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = {"mirror_topic_names":["topic-1","topic-2"]} # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    try:
        # Pause the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_pause(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        print("The response of ClusterLinkingV3Api->update_kafka_mirror_topics_pause:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_pause: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional] 
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional] 

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_kafka_mirror_topics_promote**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_promote(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)

Promote the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
from openapi_client.models.alter_mirrors_request_data import AlterMirrorsRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    validate_only = false # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = {"mirror_topic_names":["topic-1","topic-2"]} # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    try:
        # Promote the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_promote(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        print("The response of ClusterLinkingV3Api->update_kafka_mirror_topics_promote:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_promote: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional] 
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional] 

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_kafka_mirror_topics_resume**
> AlterMirrorStatusResponseDataList update_kafka_mirror_topics_resume(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)

Resume the mirror topics

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.alter_mirror_status_response_data_list import AlterMirrorStatusResponseDataList
from openapi_client.models.alter_mirrors_request_data import AlterMirrorsRequestData
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure HTTP basic authorization: resource-api-key
configuration = openapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ClusterLinkingV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    link_name = 'link-sb1' # str | The link name
    validate_only = false # bool | To validate the action can be performed successfully or not. Default: false (optional)
    alter_mirrors_request_data = {"mirror_topic_names":["topic-1","topic-2"]} # AlterMirrorsRequestData | Mirror topics to be altered. (optional)

    try:
        # Resume the mirror topics
        api_response = api_instance.update_kafka_mirror_topics_resume(cluster_id, link_name, validate_only=validate_only, alter_mirrors_request_data=alter_mirrors_request_data)
        print("The response of ClusterLinkingV3Api->update_kafka_mirror_topics_resume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterLinkingV3Api->update_kafka_mirror_topics_resume: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **link_name** | **str**| The link name | 
 **validate_only** | **bool**| To validate the action can be performed successfully or not. Default: false | [optional] 
 **alter_mirrors_request_data** | [**AlterMirrorsRequestData**](AlterMirrorsRequestData.md)| Mirror topics to be altered. | [optional] 

### Return type

[**AlterMirrorStatusResponseDataList**](AlterMirrorStatusResponseDataList.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mirror status alternation result |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

