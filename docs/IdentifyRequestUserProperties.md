# IdentifyRequestUserProperties

User properties to associate with this user. The existing user properties will be updated. And all future events will have these properties associated with them.

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
from oursprivacy_client.models.identify_request_user_properties import IdentifyRequestUserProperties

# TODO update the JSON string below
json = "{}"
# create an instance of IdentifyRequestUserProperties from a JSON string
identify_request_user_properties_instance = IdentifyRequestUserProperties.from_json(json)
# print the JSON string representation of the object
print(IdentifyRequestUserProperties.to_json())

# convert the object into a dict
identify_request_user_properties_dict = identify_request_user_properties_instance.to_dict()
# create an instance of IdentifyRequestUserProperties from a dict
identify_request_user_properties_from_dict = IdentifyRequestUserProperties.from_dict(identify_request_user_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


