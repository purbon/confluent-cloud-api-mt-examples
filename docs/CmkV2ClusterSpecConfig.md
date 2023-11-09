# CmkV2ClusterSpecConfig

The configuration of the Kafka cluster.  Note: Clusters can be upgraded from Basic to Standard, but cannot be downgraded from Standard to Basic. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Enterprise cluster type.  | 
**cku** | **int** |  | 
**encryption_key** | **str** | The id of the encryption key that is used to encrypt the data in the Kafka cluster. (e.g. for Amazon Web Services, the Amazon Resource Name of the key).  | [optional] 
**zones** | **List[str]** | The list of zones the cluster is in.  On AWS, zones are AWS [AZ IDs](https://docs.aws.amazon.com/ram/latest/userguide/working-with-az-ids.html)  (e.g. use1-az3)  On GCP, zones are GCP [zones](https://cloud.google.com/compute/docs/regions-zones)  (e.g. us-central1-c).  | [optional] [readonly] 

## Example

```python
from openapi_client.models.cmk_v2_cluster_spec_config import CmkV2ClusterSpecConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CmkV2ClusterSpecConfig from a JSON string
cmk_v2_cluster_spec_config_instance = CmkV2ClusterSpecConfig.from_json(json)
# print the JSON string representation of the object
print CmkV2ClusterSpecConfig.to_json()

# convert the object into a dict
cmk_v2_cluster_spec_config_dict = cmk_v2_cluster_spec_config_instance.to_dict()
# create an instance of CmkV2ClusterSpecConfig from a dict
cmk_v2_cluster_spec_config_form_dict = cmk_v2_cluster_spec_config.from_dict(cmk_v2_cluster_spec_config_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


