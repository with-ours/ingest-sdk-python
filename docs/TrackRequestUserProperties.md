# TrackRequestUserProperties

Additional user properties you want to pass along to the destinations. (optional) You can also update these properties via the identify endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**date_of_birth** | **str** |  | [optional] 
**phone_number** | **object** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**zip** | **object** |  | [optional] 
**country** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**ip** | **str** | The IP address of the user | [optional] 
**custom_properties** | **Dict[str, Optional[object]]** |  | [optional] 

## Example

```python
from oursprivacy_client.models.track_request_user_properties import TrackRequestUserProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRequestUserProperties from a JSON string
track_request_user_properties_instance = TrackRequestUserProperties.from_json(json)
# print the JSON string representation of the object
print(TrackRequestUserProperties.to_json())

# convert the object into a dict
track_request_user_properties_dict = track_request_user_properties_instance.to_dict()
# create an instance of TrackRequestUserProperties from a dict
track_request_user_properties_from_dict = TrackRequestUserProperties.from_dict(track_request_user_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


