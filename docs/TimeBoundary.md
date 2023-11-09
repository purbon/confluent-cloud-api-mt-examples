# TimeBoundary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_time** | **str** | The start time of format yyyy/MM/dd HH:mm:ss | [optional] 
**end_time** | **str** | The end time of format yyyy/MM/dd HH:mm:ss | [optional] 
**time_zone** | **str** | The time zone (see java.util.TimeZone) | [optional] 

## Example

```python
from openapi_client.models.time_boundary import TimeBoundary

# TODO update the JSON string below
json = "{}"
# create an instance of TimeBoundary from a JSON string
time_boundary_instance = TimeBoundary.from_json(json)
# print the JSON string representation of the object
print TimeBoundary.to_json()

# convert the object into a dict
time_boundary_dict = time_boundary_instance.to_dict()
# create an instance of TimeBoundary from a dict
time_boundary_form_dict = time_boundary.from_dict(time_boundary_dict)
```
[[Back to Model list]](../ccloud/README.md#documentation-for-models) [[Back to API list]](../ccloud/README.md#documentation-for-api-endpoints) [[Back to README]](../ccloud/README.md)


