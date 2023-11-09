# openapi_client.SubjectsV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_schema_version**](SubjectsV1Api.md#delete_schema_version) | **DELETE** /subjects/{subject}/versions/{version} | Delete schema version
[**delete_subject**](SubjectsV1Api.md#delete_subject) | **DELETE** /subjects/{subject} | Delete subject
[**get_referenced_by**](SubjectsV1Api.md#get_referenced_by) | **GET** /subjects/{subject}/versions/{version}/referencedby | List schemas referencing a schema
[**get_schema_by_version**](SubjectsV1Api.md#get_schema_by_version) | **GET** /subjects/{subject}/versions/{version} | Get schema by version
[**get_schema_only1**](SubjectsV1Api.md#get_schema_only1) | **GET** /subjects/{subject}/versions/{version}/schema | Get schema string by version
[**list**](SubjectsV1Api.md#list) | **GET** /subjects | List subjects
[**list_versions**](SubjectsV1Api.md#list_versions) | **GET** /subjects/{subject}/versions | List versions under subject
[**look_up_schema_under_subject**](SubjectsV1Api.md#look_up_schema_under_subject) | **POST** /subjects/{subject} | Lookup schema under subject
[**register**](SubjectsV1Api.md#register) | **POST** /subjects/{subject}/versions | Register schema under a subject


# **delete_schema_version**
> int delete_schema_version(subject, version, permanent=permanent)

Delete schema version

Deletes a specific version of the schema registered under this subject. This only deletes the version and the schema ID remains intact making it still possible to decode data using the schema ID. This API is recommended to be used only in development environments or under extreme circumstances where-in, its required to delete a previously registered schema for compatibility purposes or re-register previously registered schema.

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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Name of the subject
    version = 'version_example' # str | Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \"latest\". \"latest\" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.
    permanent = True # bool | Whether to perform a permanent delete (optional)

    try:
        # Delete schema version
        api_response = api_instance.delete_schema_version(subject, version, permanent=permanent)
        print("The response of SubjectsV1Api->delete_schema_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->delete_schema_version: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject | 
 **version** | **str**| Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \&quot;latest\&quot;. \&quot;latest\&quot; returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served. | 
 **permanent** | **bool**| Whether to perform a permanent delete | [optional] 

### Return type

**int**

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation succeeded. Returns the schema version. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. Error code 40402 indicates version not found. |  -  |
**422** | Unprocessable Entity. Error code 42202 indicates an invalid version. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_subject**
> List[int] delete_subject(subject, permanent=permanent)

Delete subject

Deletes the specified subject and its associated compatibility level if registered. It is recommended to use this API only when a topic needs to be recycled or in development environment.

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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Name of the subject
    permanent = True # bool | Whether to perform a permanent delete (optional)

    try:
        # Delete subject
        api_response = api_instance.delete_subject(subject, permanent=permanent)
        print("The response of SubjectsV1Api->delete_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->delete_subject: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject | 
 **permanent** | **bool**| Whether to perform a permanent delete | [optional] 

### Return type

**List[int]**

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation succeeded. Returns list of schema versions deleted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_referenced_by**
> List[int] get_referenced_by(subject, version)

List schemas referencing a schema

Retrieves the IDs of schemas that reference the specified schema.

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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Name of the subject
    version = 'version_example' # str | Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \"latest\". \"latest\" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.

    try:
        # List schemas referencing a schema
        api_response = api_instance.get_referenced_by(subject, version)
        print("The response of SubjectsV1Api->get_referenced_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->get_referenced_by: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject | 
 **version** | **str**| Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \&quot;latest\&quot;. \&quot;latest\&quot; returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served. | 

### Return type

**List[int]**

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of IDs for schemas that reference the specified schema. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. Error code 40402 indicates version not found. |  -  |
**422** | Unprocessable Entity. Error code 42202 indicates an invalid version. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_schema_by_version**
> ModelSchema get_schema_by_version(subject, version, deleted=deleted)

Get schema by version

Retrieves a specific version of the schema registered under this subject.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.model_schema import ModelSchema
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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Name of the subject
    version = 'version_example' # str | Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \"latest\". \"latest\" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.
    deleted = True # bool | Whether to include deleted schema (optional)

    try:
        # Get schema by version
        api_response = api_instance.get_schema_by_version(subject, version, deleted=deleted)
        print("The response of SubjectsV1Api->get_schema_by_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->get_schema_by_version: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject | 
 **version** | **str**| Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \&quot;latest\&quot;. \&quot;latest\&quot; returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served. | 
 **deleted** | **bool**| Whether to include deleted schema | [optional] 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The schema. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. Error code 40402 indicates version not found. |  -  |
**422** | Unprocessable Entity. Error code 42202 indicates an invalid version. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_schema_only1**
> str get_schema_only1(subject, version, deleted=deleted)

Get schema string by version

Retrieves the schema for the specified version of this subject. Only the unescaped schema string is returned.

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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Name of the subject
    version = 'version_example' # str | Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \"latest\". \"latest\" returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served.
    deleted = True # bool | Whether to include deleted schema (optional)

    try:
        # Get schema string by version
        api_response = api_instance.get_schema_only1(subject, version, deleted=deleted)
        print("The response of SubjectsV1Api->get_schema_only1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->get_schema_only1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject | 
 **version** | **str**| Version of the schema to be returned. Valid values for versionId are between [1,2^31-1] or the string \&quot;latest\&quot;. \&quot;latest\&quot; returns the last registered schema under the specified subject. Note that there may be a new latest schema that gets registered right after this request is served. | 
 **deleted** | **bool**| Whether to include deleted schema | [optional] 

### Return type

**str**

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The schema string. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. Error code 40402 indicates version not found. |  -  |
**422** | Unprocessable Entity. Error code 42202 indicates an invalid version. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list**
> List[str] list(subject_prefix=subject_prefix, deleted=deleted)

List subjects

Retrieves a list of registered subjects matching specified parameters.

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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject_prefix = ':*:' # str | Subject name prefix (optional) (default to ':*:')
    deleted = True # bool | Whether to look up deleted subjects (optional)

    try:
        # List subjects
        api_response = api_instance.list(subject_prefix=subject_prefix, deleted=deleted)
        print("The response of SubjectsV1Api->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject_prefix** | **str**| Subject name prefix | [optional] [default to &#39;:*:&#39;]
 **deleted** | **bool**| Whether to look up deleted subjects | [optional] 

### Return type

**List[str]**

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of subjects matching the specified parameters. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **list_versions**
> List[int] list_versions(subject, deleted=deleted)

List versions under subject

Retrieves a list of versions registered under the specified subject.

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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Name of the subject
    deleted = True # bool | Whether to include deleted schemas (optional)

    try:
        # List versions under subject
        api_response = api_instance.list_versions(subject, deleted=deleted)
        print("The response of SubjectsV1Api->list_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->list_versions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject | 
 **deleted** | **bool**| Whether to include deleted schemas | [optional] 

### Return type

**List[int]**

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of version numbers matching the specified parameters. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found.  |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **look_up_schema_under_subject**
> ModelSchema look_up_schema_under_subject(subject, register_schema_request, normalize=normalize, deleted=deleted)

Lookup schema under subject

Check if a schema has already been registered under the specified subject. If so, this returns the schema string along with its globally unique identifier, its version under this subject and the subject name.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.model_schema import ModelSchema
from openapi_client.models.register_schema_request import RegisterSchemaRequest
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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Subject under which the schema will be registered
    register_schema_request = openapi_client.RegisterSchemaRequest() # RegisterSchemaRequest | Schema
    normalize = True # bool | Whether to lookup the normalized schema (optional)
    deleted = True # bool | Whether to lookup deleted schemas (optional)

    try:
        # Lookup schema under subject
        api_response = api_instance.look_up_schema_under_subject(subject, register_schema_request, normalize=normalize, deleted=deleted)
        print("The response of SubjectsV1Api->look_up_schema_under_subject:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->look_up_schema_under_subject: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Subject under which the schema will be registered | 
 **register_schema_request** | [**RegisterSchemaRequest**](RegisterSchemaRequest.md)| Schema | 
 **normalize** | **bool**| Whether to lookup the normalized schema | [optional] 
 **deleted** | **bool**| Whether to lookup deleted schemas | [optional] 

### Return type

[**ModelSchema**](ModelSchema.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json, application/octet-stream
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The schema. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found. Error code 40401 indicates subject not found. Error code 40403 indicates schema not found. |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **register**
> RegisterSchemaResponse register(subject, register_schema_request, normalize=normalize)

Register schema under a subject

Register a new schema under the specified subject. If successfully registered, this returns the unique identifier of this schema in the registry. The returned identifier should be used to retrieve this schema from the schemas resource and is different from the schema's version which is associated with the subject. If the same schema is registered under a different subject, the same identifier will be returned. However, the version of the schema may be different under different subjects. A schema should be compatible with the previously registered schema or schemas (if there are any) as per the configured compatibility level. The configured compatibility level can be obtained by issuing a GET http:get:: /config/(string: subject). If that returns null, then GET http:get:: /config When there are multiple instances of Schema Registry running in the same cluster, the schema registration request will be forwarded to one of the instances designated as the primary. If the primary is not available, the client will get an error code indicating that the forwarding has failed.

### Example

* OAuth Authentication (external-access-token):
* Basic Authentication (resource-api-key):
```python
import time
import os
import openapi_client
from openapi_client.models.register_schema_request import RegisterSchemaRequest
from openapi_client.models.register_schema_response import RegisterSchemaResponse
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
    api_instance = openapi_client.SubjectsV1Api(api_client)
    subject = 'subject_example' # str | Name of the subject
    register_schema_request = openapi_client.RegisterSchemaRequest() # RegisterSchemaRequest | Schema
    normalize = True # bool | Whether to register the normalized schema (optional)

    try:
        # Register schema under a subject
        api_response = api_instance.register(subject, register_schema_request, normalize=normalize)
        print("The response of SubjectsV1Api->register:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubjectsV1Api->register: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subject** | **str**| Name of the subject | 
 **register_schema_request** | [**RegisterSchemaRequest**](RegisterSchemaRequest.md)| Schema | 
 **normalize** | **bool**| Whether to register the normalized schema | [optional] 

### Return type

[**RegisterSchemaResponse**](RegisterSchemaResponse.md)

### Authorization

[external-access-token](../ccloud/README.md#external-access-token), [resource-api-key](../ccloud/README.md#resource-api-key)

### HTTP request headers

 - **Content-Type**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json, application/json, application/octet-stream
 - **Accept**: application/vnd.schemaregistry.v1+json, application/vnd.schemaregistry+json; qs=0.9, application/json; qs=0.5, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Schema successfully registered. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict. Incompatible schema. |  -  |
**422** | Unprocessable entity. Error code 42201 indicates an invalid schema or schema type.  |  -  |
**429** | Rate Limit Exceeded |  * X-Request-Id - The unique identifier for the API request. <br>  * X-RateLimit-Limit - The maximum number of requests you&#39;re permitted to make per time period. <br>  * X-RateLimit-Remaining - The number of requests remaining in the current rate limit window. <br>  * X-RateLimit-Reset - The relative time in seconds until the current rate-limit window resets.      **Important:** This differs from Github and Twitter&#39;s same-named header which uses UTC epoch seconds. We use relative time to avoid client/server time synchronization issues. <br>  * Retry-After - The number of seconds to wait until the rate limit window resets. Only sent when the rate limit is reached. <br>  |
**500** | Internal Server Error. Error code 50001 indicates a failure in the backend data store.Error code 50002 indicates operation timed out. Error code 50003 indicates a failure forwarding the request to the primary. |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

