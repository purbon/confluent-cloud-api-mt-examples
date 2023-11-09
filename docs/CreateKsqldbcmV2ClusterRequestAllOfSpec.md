# CreateKsqldbcmV2ClusterRequestAllOfSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kafka_cluster** | **object** |  | [optional] 
**credential_identity** | **object** |  | [optional] 
**environment** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.create_ksqldbcm_v2_cluster_request_all_of_spec import CreateKsqldbcmV2ClusterRequestAllOfSpec

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKsqldbcmV2ClusterRequestAllOfSpec from a JSON string
create_ksqldbcm_v2_cluster_request_all_of_spec_instance = CreateKsqldbcmV2ClusterRequestAllOfSpec.from_json(json)
# print the JSON string representation of the object
print CreateKsqldbcmV2ClusterRequestAllOfSpec.to_json()

# convert the object into a dict
create_ksqldbcm_v2_cluster_request_all_of_spec_dict = create_ksqldbcm_v2_cluster_request_all_of_spec_instance.to_dict()
# create an instance of CreateKsqldbcmV2ClusterRequestAllOfSpec from a dict
create_ksqldbcm_v2_cluster_request_all_of_spec_form_dict = create_ksqldbcm_v2_cluster_request_all_of_spec.from_dict(create_ksqldbcm_v2_cluster_request_all_of_spec_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


