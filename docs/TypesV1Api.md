# openapi_client.TypesV1Api

All URIs are relative to *https://api.confluent.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_business_metadata_defs**](TypesV1Api.md#create_business_metadata_defs) | **POST** /catalog/v1/types/businessmetadatadefs | Bulk Create Business Metadata Definitions
[**create_tag_defs**](TypesV1Api.md#create_tag_defs) | **POST** /catalog/v1/types/tagdefs | Bulk Create Tag Definitions
[**delete_business_metadata_def**](TypesV1Api.md#delete_business_metadata_def) | **DELETE** /catalog/v1/types/businessmetadatadefs/{bmName} | Delete Business Metadata Definition
[**delete_tag_def**](TypesV1Api.md#delete_tag_def) | **DELETE** /catalog/v1/types/tagdefs/{tagName} | Delete Tag Definition
[**get_all_business_metadata_defs**](TypesV1Api.md#get_all_business_metadata_defs) | **GET** /catalog/v1/types/businessmetadatadefs | Bulk Read Business Metadata Definitions
[**get_all_tag_defs**](TypesV1Api.md#get_all_tag_defs) | **GET** /catalog/v1/types/tagdefs | Bulk Read Tag Definitions
[**get_business_metadata_def_by_name**](TypesV1Api.md#get_business_metadata_def_by_name) | **GET** /catalog/v1/types/businessmetadatadefs/{bmName} | Read Business Metadata Definition
[**get_tag_def_by_name**](TypesV1Api.md#get_tag_def_by_name) | **GET** /catalog/v1/types/tagdefs/{tagName} | Read Tag Definition
[**update_business_metadata_defs**](TypesV1Api.md#update_business_metadata_defs) | **PUT** /catalog/v1/types/businessmetadatadefs | Bulk Update Business Metadata Definitions
[**update_tag_defs**](TypesV1Api.md#update_tag_defs) | **PUT** /catalog/v1/types/tagdefs | Bulk Update Tag Definitions


# **create_business_metadata_defs**
> List[BusinessMetadataDefResponse] create_business_metadata_defs(business_metadata_def=business_metadata_def)

Bulk Create Business Metadata Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk create API for business metadata definitions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.business_metadata_def import BusinessMetadataDef
from openapi_client.models.business_metadata_def_response import BusinessMetadataDefResponse
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
    api_instance = openapi_client.TypesV1Api(api_client)
    business_metadata_def = [openapi_client.BusinessMetadataDef()] # List[BusinessMetadataDef] | The business metadata definitions to create (optional)

    try:
        # Bulk Create Business Metadata Definitions
        api_response = api_instance.create_business_metadata_defs(business_metadata_def=business_metadata_def)
        print("The response of TypesV1Api->create_business_metadata_defs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->create_business_metadata_defs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata_def** | [**List[BusinessMetadataDef]**](BusinessMetadataDef.md)| The business metadata definitions to create | [optional] 

### Return type

[**List[BusinessMetadataDefResponse]**](BusinessMetadataDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definitions. Errored business metadata definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **create_tag_defs**
> List[TagDefResponse] create_tag_defs(tag_def=tag_def)

Bulk Create Tag Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk create API for tag definitions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tag_def import TagDef
from openapi_client.models.tag_def_response import TagDefResponse
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
    api_instance = openapi_client.TypesV1Api(api_client)
    tag_def = [openapi_client.TagDef()] # List[TagDef] | The tag definitions to create (optional)

    try:
        # Bulk Create Tag Definitions
        api_response = api_instance.create_tag_defs(tag_def=tag_def)
        print("The response of TypesV1Api->create_tag_defs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->create_tag_defs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_def** | [**List[TagDef]**](TagDef.md)| The tag definitions to create | [optional] 

### Return type

[**List[TagDefResponse]**](TagDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definitions. Errored tag definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **delete_business_metadata_def**
> delete_business_metadata_def(bm_name)

Delete Business Metadata Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete API for business metadata definition identified by its name.

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
    api_instance = openapi_client.TypesV1Api(api_client)
    bm_name = 'bm_name_example' # str | The name of the business metadata definition

    try:
        # Delete Business Metadata Definition
        api_instance.delete_business_metadata_def(bm_name)
    except Exception as e:
        print("Exception when calling TypesV1Api->delete_business_metadata_def: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_name** | **str**| The name of the business metadata definition | 

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

# **delete_tag_def**
> delete_tag_def(tag_name)

Delete Tag Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Delete API for tag definition identified by its name.

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
    api_instance = openapi_client.TypesV1Api(api_client)
    tag_name = 'tag_name_example' # str | The name of the tag definition

    try:
        # Delete Tag Definition
        api_instance.delete_tag_def(tag_name)
    except Exception as e:
        print("Exception when calling TypesV1Api->delete_tag_def: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The name of the tag definition | 

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

# **get_all_business_metadata_defs**
> List[BusinessMetadataDefResponse] get_all_business_metadata_defs(prefix=prefix)

Bulk Read Business Metadata Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk retrieval API for retrieving business metadata definitions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.business_metadata_def_response import BusinessMetadataDefResponse
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
    api_instance = openapi_client.TypesV1Api(api_client)
    prefix = 'prefix_example' # str | The prefix of a business metadata definition name (optional)

    try:
        # Bulk Read Business Metadata Definitions
        api_response = api_instance.get_all_business_metadata_defs(prefix=prefix)
        print("The response of TypesV1Api->get_all_business_metadata_defs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->get_all_business_metadata_defs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The prefix of a business metadata definition name | [optional] 

### Return type

[**List[BusinessMetadataDefResponse]**](BusinessMetadataDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definitions |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_all_tag_defs**
> List[TagDefResponse] get_all_tag_defs(prefix=prefix)

Bulk Read Tag Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk retrieval API for retrieving tag definitions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tag_def_response import TagDefResponse
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
    api_instance = openapi_client.TypesV1Api(api_client)
    prefix = 'prefix_example' # str | The prefix of a tag definition name (optional)

    try:
        # Bulk Read Tag Definitions
        api_response = api_instance.get_all_tag_defs(prefix=prefix)
        print("The response of TypesV1Api->get_all_tag_defs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->get_all_tag_defs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix** | **str**| The prefix of a tag definition name | [optional] 

### Return type

[**List[TagDefResponse]**](TagDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definitions |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_business_metadata_def_by_name**
> BusinessMetadataDef get_business_metadata_def_by_name(bm_name)

Read Business Metadata Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get the business metadata definition with the given name.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.business_metadata_def import BusinessMetadataDef
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
    api_instance = openapi_client.TypesV1Api(api_client)
    bm_name = 'bm_name_example' # str | The name of the business metadata definition

    try:
        # Read Business Metadata Definition
        api_response = api_instance.get_business_metadata_def_by_name(bm_name)
        print("The response of TypesV1Api->get_business_metadata_def_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->get_business_metadata_def_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bm_name** | **str**| The name of the business metadata definition | 

### Return type

[**BusinessMetadataDef**](BusinessMetadataDef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definition |  -  |
**400** | Bad Request |  -  |
**404** | Business metadata definition not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **get_tag_def_by_name**
> TagDef get_tag_def_by_name(tag_name)

Read Tag Definition

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Get the tag definition with the given name.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tag_def import TagDef
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
    api_instance = openapi_client.TypesV1Api(api_client)
    tag_name = 'tag_name_example' # str | The name of the tag definiton

    try:
        # Read Tag Definition
        api_response = api_instance.get_tag_def_by_name(tag_name)
        print("The response of TypesV1Api->get_tag_def_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->get_tag_def_by_name: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| The name of the tag definiton | 

### Return type

[**TagDef**](TagDef.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definition |  -  |
**400** | Bad Request |  -  |
**404** | Tag definition not found |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_business_metadata_defs**
> List[BusinessMetadataDefResponse] update_business_metadata_defs(business_metadata_def=business_metadata_def)

Bulk Update Business Metadata Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk update API for business metadata definitions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.business_metadata_def import BusinessMetadataDef
from openapi_client.models.business_metadata_def_response import BusinessMetadataDefResponse
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
    api_instance = openapi_client.TypesV1Api(api_client)
    business_metadata_def = [openapi_client.BusinessMetadataDef()] # List[BusinessMetadataDef] | The business metadata definitions to update (optional)

    try:
        # Bulk Update Business Metadata Definitions
        api_response = api_instance.update_business_metadata_defs(business_metadata_def=business_metadata_def)
        print("The response of TypesV1Api->update_business_metadata_defs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->update_business_metadata_defs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_metadata_def** | [**List[BusinessMetadataDef]**](BusinessMetadataDef.md)| The business metadata definitions to update | [optional] 

### Return type

[**List[BusinessMetadataDefResponse]**](BusinessMetadataDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The business metadata definitions. Errored business metadata definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

# **update_tag_defs**
> List[TagDefResponse] update_tag_defs(tag_def=tag_def)

Bulk Update Tag Definitions

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)  Bulk update API for tag definitions.

### Example

```python
import time
import os
import openapi_client
from openapi_client.models.tag_def import TagDef
from openapi_client.models.tag_def_response import TagDefResponse
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
    api_instance = openapi_client.TypesV1Api(api_client)
    tag_def = [openapi_client.TagDef()] # List[TagDef] | The tag definitions to update (optional)

    try:
        # Bulk Update Tag Definitions
        api_response = api_instance.update_tag_defs(tag_def=tag_def)
        print("The response of TypesV1Api->update_tag_defs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TypesV1Api->update_tag_defs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_def** | [**List[TagDef]**](TagDef.md)| The tag definitions to update | [optional] 

### Return type

[**List[TagDefResponse]**](TagDefResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tag definitions. Errored tag definitions will have an additional error property. |  -  |
**400** | Bad Request |  -  |
**429** | Rate Limit Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to README]](../ccloud/README.md)

