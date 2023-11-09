# openapi_client.EntityV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_metadata**](EntityV1Api.md#create_business_metadata) | **POST** /catalog/v1/entity/businessmetadata | Bulk Create Business Metadata
[**create_tags**](EntityV1Api.md#create_tags) | **POST** /catalog/v1/entity/tags | Bulk Create Tags
[**delete_business_metadata**](EntityV1Api.md#delete_business_metadata) | **DELETE** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/businessmetadata/{bmName} | Delete a Business Metadata for an Entity
[**delete_tag**](EntityV1Api.md#delete_tag) | **DELETE** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/tags/{tagName} | Delete a Tag for an Entity
[**get_business_metadata**](EntityV1Api.md#get_business_metadata) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/businessmetadata | Read Business Metadata for an Entity
[**get_by_unique_attributes**](EntityV1Api.md#get_by_unique_attributes) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName} | Read an Entity
[**get_tags**](EntityV1Api.md#get_tags) | **GET** /catalog/v1/entity/type/{typeName}/name/{qualifiedName}/tags | Read Tags for an Entity
[**partial_entity_update**](EntityV1Api.md#partial_entity_update) | **PUT** /catalog/v1/entity | Update an Entity Attribute
[**update_business_metadata**](EntityV1Api.md#update_business_metadata) | **PUT** /catalog/v1/entity/businessmetadata | Bulk Update Business Metadata
[**update_tags**](EntityV1Api.md#update_tags) | **PUT** /catalog/v1/entity/tags | Bulk Update Tags


# **create_business_metadata**
> List[BusinessMetadataResponse] create_business_metadata(business_metadata=business_metadata)

Bulk Create Business Metadata

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to create multiple business metadata.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.business_metadata import BusinessMetadata
from openapi_client.models.business_metadata_response import BusinessMetadataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    business_metadata = [openapi_client.BusinessMetadata()] # List[BusinessMetadata] | The business metadata (optional)

    try:
        # Bulk Create Business Metadata
        api_response = api_instance.create_business_metadata(business_metadata=business_metadata)
        print("The response of EntityV1Api->create_business_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->create_business_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata** | [**List[BusinessMetadata]**](BusinessMetadata.md)| The business metadata | [optional] 

### Return type

[**List[BusinessMetadataResponse]**](BusinessMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata. Errored business metadata will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **create_tags**
> List[TagResponse] create_tags(tag=tag)

Bulk Create Tags

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to create multiple tags.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tag import Tag
from openapi_client.models.tag_response import TagResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    tag = [openapi_client.Tag()] # List[Tag] | The tags (optional)

    try:
        # Bulk Create Tags
        api_response = api_instance.create_tags(tag=tag)
        print("The response of EntityV1Api->create_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->create_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**List[Tag]**](Tag.md)| The tags | [optional] 

### Return type

[**List[TagResponse]**](TagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tags. Errored tags will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_business_metadata**
> delete_business_metadata(type_name, qualified_name, bm_name)

Delete a Business Metadata for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete a business metadata on an entity.

### Example

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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    type_name = 'type_name_example' # str | The type of the entity
    qualified_name = 'qualified_name_example' # str | The qualified name of the entity
    bm_name = 'bm_name_example' # str | The name of the business metadata

    try:
        # Delete a Business Metadata for an Entity
        api_instance.delete_business_metadata(type_name, qualified_name, bm_name)
    except Exception as e:
        print("Exception when calling EntityV1Api->delete_business_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity | 
 **qualified_name** | **str**| The qualified name of the entity | 
 **bm_name** | **str**| The name of the business metadata | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_tag**
> delete_tag(type_name, qualified_name, tag_name)

Delete a Tag for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete a tag for an entity.

### Example

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


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    type_name = 'type_name_example' # str | The type of the entity
    qualified_name = 'qualified_name_example' # str | The qualified name of the entity
    tag_name = 'tag_name_example' # str | The name of the tag

    try:
        # Delete a Tag for an Entity
        api_instance.delete_tag(type_name, qualified_name, tag_name)
    except Exception as e:
        print("Exception when calling EntityV1Api->delete_tag: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity | 
 **qualified_name** | **str**| The qualified name of the entity | 
 **tag_name** | **str**| The name of the tag | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_business_metadata**
> List[BusinessMetadataResponse] get_business_metadata(type_name, qualified_name)

Read Business Metadata for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Gets the list of business metadata for a given entity represented by a qualified name.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.business_metadata_response import BusinessMetadataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    type_name = 'type_name_example' # str | The type of the entity
    qualified_name = 'qualified_name_example' # str | The qualified name of the entity

    try:
        # Read Business Metadata for an Entity
        api_response = api_instance.get_business_metadata(type_name, qualified_name)
        print("The response of EntityV1Api->get_business_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->get_business_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity | 
 **qualified_name** | **str**| The qualified name of the entity | 

### Return type

[**List[BusinessMetadataResponse]**](BusinessMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_by_unique_attributes**
> EntityWithExtInfo get_by_unique_attributes(type_name, qualified_name, min_ext_info=min_ext_info, ignore_relationships=ignore_relationships)

Read an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Fetch complete definition of an entity given its type and unique attribute.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity_with_ext_info import EntityWithExtInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    type_name = 'type_name_example' # str | The type of the entity
    qualified_name = 'qualified_name_example' # str | The qualified name of the entity
    min_ext_info = False # bool | Whether to populate on header and schema attributes (optional) (default to False)
    ignore_relationships = False # bool | Whether to ignore relationships (optional) (default to False)

    try:
        # Read an Entity
        api_response = api_instance.get_by_unique_attributes(type_name, qualified_name, min_ext_info=min_ext_info, ignore_relationships=ignore_relationships)
        print("The response of EntityV1Api->get_by_unique_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->get_by_unique_attributes: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity | 
 **qualified_name** | **str**| The qualified name of the entity | 
 **min_ext_info** | **bool**| Whether to populate on header and schema attributes | [optional] [default to False]
 **ignore_relationships** | **bool**| Whether to ignore relationships | [optional] [default to False]

### Return type

[**EntityWithExtInfo**](EntityWithExtInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The entity |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_tags**
> List[TagResponse] get_tags(type_name, qualified_name)

Read Tags for an Entity

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Gets the list of tags for a given entity represented by a qualified name.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tag_response import TagResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    type_name = 'type_name_example' # str | The type of the entity
    qualified_name = 'qualified_name_example' # str | The qualified name of the entity

    try:
        # Read Tags for an Entity
        api_response = api_instance.get_tags(type_name, qualified_name)
        print("The response of EntityV1Api->get_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->get_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type_name** | **str**| The type of the entity | 
 **qualified_name** | **str**| The qualified name of the entity | 

### Return type

[**List[TagResponse]**](TagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tags |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **partial_entity_update**
> EntityPartialUpdateResponse partial_entity_update(entity_with_ext_info=entity_with_ext_info)

Update an Entity Attribute

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Partially update an entity attribute.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.entity_partial_update_response import EntityPartialUpdateResponse
from openapi_client.models.entity_with_ext_info import EntityWithExtInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    entity_with_ext_info = openapi_client.EntityWithExtInfo() # EntityWithExtInfo | The entity to update (optional)

    try:
        # Update an Entity Attribute
        api_response = api_instance.partial_entity_update(entity_with_ext_info=entity_with_ext_info)
        print("The response of EntityV1Api->partial_entity_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->partial_entity_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_with_ext_info** | [**EntityWithExtInfo**](EntityWithExtInfo.md)| The entity to update | [optional] 

### Return type

[**EntityPartialUpdateResponse**](EntityPartialUpdateResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated entity |  -  |
**400** | Bad Request |  -  |
**404** | Entity not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_business_metadata**
> List[BusinessMetadataResponse] update_business_metadata(business_metadata=business_metadata)

Bulk Update Business Metadata

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to update multiple business metadata.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.business_metadata import BusinessMetadata
from openapi_client.models.business_metadata_response import BusinessMetadataResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    business_metadata = [openapi_client.BusinessMetadata()] # List[BusinessMetadata] | The business metadata (optional)

    try:
        # Bulk Update Business Metadata
        api_response = api_instance.update_business_metadata(business_metadata=business_metadata)
        print("The response of EntityV1Api->update_business_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->update_business_metadata: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata** | [**List[BusinessMetadata]**](BusinessMetadata.md)| The business metadata | [optional] 

### Return type

[**List[BusinessMetadataResponse]**](BusinessMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata. Errored business metadata will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_tags**
> List[TagResponse] update_tags(tag=tag)

Bulk Update Tags

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk API to update multiple tags.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tag import Tag
from openapi_client.models.tag_response import TagResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.confluent.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.confluent.cloud"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EntityV1Api(api_client)
    tag = [openapi_client.Tag()] # List[Tag] | The tags (optional)

    try:
        # Bulk Update Tags
        api_response = api_instance.update_tags(tag=tag)
        print("The response of EntityV1Api->update_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EntityV1Api->update_tags: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | [**List[Tag]**](Tag.md)| The tags | [optional] 

### Return type

[**List[TagResponse]**](TagResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tags. Errored tags will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

