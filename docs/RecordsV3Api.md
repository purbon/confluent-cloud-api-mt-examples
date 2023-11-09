# openapi_client.RecordsV3Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**produce_record**](RecordsV3Api.md#produce_record) | **POST** /kafka/v3/clusters/{cluster_id}/topics/{topic_name}/records | Produce Records


# **produce_record**
> ProduceResponse produce_record(cluster_id, topic_name, produce_request=produce_request)

Produce Records

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Produce records to the given topic, returning delivery reports for each record produced. This API can be used in streaming mode by setting \"Transfer-Encoding: chunked\" header. For as long as the connection is kept open, the server will keep accepting records. Records are streamed to and from the server as Concatenated JSON. For each record sent to the server, the server will asynchronously send back a delivery report, in the same order, each with its own error_code. An error_code of 200 indicates success. The HTTP status code will be HTTP 200 OK as long as the connection is successfully established. To identify records that have encountered an error, check the error_code of each delivery report.  This API currently does not support Schema Registry integration. Sending schemas is not supported. Only BINARY, JSON, and STRING formats are supported.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.produce_request import ProduceRequest
from openapi_client.models.produce_response import ProduceResponse
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
    api_instance = openapi_client.RecordsV3Api(api_client)
    cluster_id = 'cluster-1' # str | The Kafka cluster ID.
    topic_name = 'topic-1' # str | The topic name.
    produce_request = {"partition_id":1,"headers":[{"name":"Header-1","value":"SGVhZGVyLTE="},{"name":"Header-2","value":"SGVhZGVyLTI="}],"key":{"type":"BINARY","data":"Zm9vYmFy"},"value":{"type":"JSON","data":{"foo":"bar"}},"timestamp":"2021-02-05T19:14:42Z"} # ProduceRequest | A single record to be produced to Kafka. To produce multiple records in the same request, simply concatenate the records. The delivery reports are concatenated in the same order as the records are sent. (optional)

    try:
        # Produce Records
        api_response = api_instance.produce_record(cluster_id, topic_name, produce_request=produce_request)
        print("The response of RecordsV3Api->produce_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordsV3Api->produce_record: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| The Kafka cluster ID. | 
 **topic_name** | **str**| The topic name. | 
 **produce_request** | [**ProduceRequest**](ProduceRequest.md)| A single record to be produced to Kafka. To produce multiple records in the same request, simply concatenate the records. The delivery reports are concatenated in the same order as the records are sent. | [optional] 

### Return type

[**ProduceResponse**](ProduceResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response containing a delivery report for a record produced to a topic. In streaming mode, for each record sent, a separate delivery report will be returned, in the same order, each with its own error_code. |  -  |
**400** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**401** | Indicates a client authentication error. Kafka authentication failures will contain error code 40101 in the response body. |  -  |
**403** | Indicates a client authorization error. Kafka authorization failures will contain error code 40301 in the response body. |  -  |
**404** | Indicates attempted access to an unreachable or non-existing resource like e.g. an unknown topic or partition. GET requests to endpoints not allowed in the accesslists will also result in this response. |  -  |
**413** | This implies the client is sending a request payload that is larger than the maximum message size the server can accept. |  -  |
**415** | This implies the client is sending the request payload format in an unsupported format. |  -  |
**422** | Indicates a bad request error. It could be caused by an unexpected request body format or other forms of request validation failure. |  -  |
**429** | Indicates that a rate limit threshold has been reached, and the client should retry again later. |  -  |
**5XX** | A server-side problem that might not be addressable from the client side. Retriable Kafka errors will contain error code 50003 in the response body. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

