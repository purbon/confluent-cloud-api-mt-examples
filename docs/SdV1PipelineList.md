# SdV1PipelineList

`Pipeline` objects represent information about a user-defined pipeline of Confluent Cloud components. The pipeline's content is available separately.  The API allows you to create, retrieve, update, and delete your pipelines, as well as list all of your pipelines for the particular environment and Kafka cluster.   Related guide: [Pipelines in Confluent Cloud](https://docs.confluent.io/cloud/current/stream-designer/).  ## The Pipelines Model <SchemaDefinition schemaRef=\"#/components/schemas/sd.v1.Pipeline\" />  ## Quotas and Limits This resource is subject to the following quotas:  | Quota | Description | | --- | --- | | `pipelines_per_org` | Pipelines in one Confluent Cloud organization | | `pipelines_per_cluster` | Pipelines in one Confluent Cloud Kafka cluster |

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the schema version of this representation of a resource. | [readonly] 
**kind** | **str** | Kind defines the object this REST resource represents. | [readonly] 
**metadata** | [**SdV1PipelineListMetadata**](SdV1PipelineListMetadata.md) |  | 
**data** | [**List[SdV1PipelineListDataInner]**](SdV1PipelineListDataInner.md) | A data property that contains an array of resource items. Each entry in the array is a separate resource. | 

## Example

```python
from openapi_client.models.sd_v1_pipeline_list import SdV1PipelineList

# TODO update the JSON string below
json = "{}"
# create an instance of SdV1PipelineList from a JSON string
sd_v1_pipeline_list_instance = SdV1PipelineList.from_json(json)
# print the JSON string representation of the object
print SdV1PipelineList.to_json()

# convert the object into a dict
sd_v1_pipeline_list_dict = sd_v1_pipeline_list_instance.to_dict()
# create an instance of SdV1PipelineList from a dict
sd_v1_pipeline_list_form_dict = sd_v1_pipeline_list.from_dict(sd_v1_pipeline_list_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


