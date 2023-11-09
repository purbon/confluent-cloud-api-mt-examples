# CreateConnectv1Connector500Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_connectv1_connector500_response import CreateConnectv1Connector500Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectv1Connector500Response from a JSON string
create_connectv1_connector500_response_instance = CreateConnectv1Connector500Response.from_json(json)
# print the JSON string representation of the object
print CreateConnectv1Connector500Response.to_json()

# convert the object into a dict
create_connectv1_connector500_response_dict = create_connectv1_connector500_response_instance.to_dict()
# create an instance of CreateConnectv1Connector500Response from a dict
create_connectv1_connector500_response_form_dict = create_connectv1_connector500_response.from_dict(create_connectv1_connector500_response_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


