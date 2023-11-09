# ListKsqldbcmV2Clusters200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**KsqldbcmV2ClusterListMetadata**](KsqldbcmV2ClusterListMetadata.md) |  | 
**data** | [**List[ListKsqldbcmV2Clusters200ResponseAllOfDataInner]**](ListKsqldbcmV2Clusters200ResponseAllOfDataInner.md) |  | 

## Example

```python
from openapi_client.models.list_ksqldbcm_v2_clusters200_response import ListKsqldbcmV2Clusters200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListKsqldbcmV2Clusters200Response from a JSON string
list_ksqldbcm_v2_clusters200_response_instance = ListKsqldbcmV2Clusters200Response.from_json(json)
# print the JSON string representation of the object
print ListKsqldbcmV2Clusters200Response.to_json()

# convert the object into a dict
list_ksqldbcm_v2_clusters200_response_dict = list_ksqldbcm_v2_clusters200_response_instance.to_dict()
# create an instance of ListKsqldbcmV2Clusters200Response from a dict
list_ksqldbcm_v2_clusters200_response_form_dict = list_ksqldbcm_v2_clusters200_response.from_dict(list_ksqldbcm_v2_clusters200_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


