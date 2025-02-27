# TrackRequestDefaultProperties

These properties are used throughout the Ours app to pass known values onto destinations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_bot** | **bool** |  | [optional] 
**ad_id** | **str** |  | [optional] 
**encoding** | **str** | The character encoding of the page. Ex: UTF-8 | [optional] 
**browser_name** | **str** |  | [optional] 
**browser_version** | **str** |  | [optional] 
**cpu_architecture** | **str** |  | [optional] 
**device_type** | **str** | \&quot;mobile\&quot; | \&quot;tablet\&quot; | \&quot;console\&quot; | \&quot;smarttv\&quot; | \&quot;wearable\&quot; | \&quot;xr\&quot; | \&quot;embedded\&quot; | [optional] 
**device_model** | **str** |  | [optional] 
**device_vendor** | **str** |  | [optional] 
**engine_name** | **str** |  | [optional] 
**engine_version** | **str** |  | [optional] 
**os_name** | **str** |  | [optional] 
**os_version** | **str** |  | [optional] 
**browser_language** | **str** |  | [optional] 
**current_url** | **str** | The full url (including query params) of the current page | [optional] 
**webview** | **bool** |  | [optional] 
**iframe** | **bool** |  | [optional] 
**session_count** | **float** |  | [optional] 
**active_duration** | **float** | The active time in milliseconds that the user had this tab active | [optional] 
**duration** | **float** | The time in milliseconds since the page was loaded // script was loaded | [optional] 
**epik** | **str** |  | [optional] 
**sacid** | **str** |  | [optional] 
**fbc** | **str** |  | [optional] 
**fbclid** | **str** |  | [optional] 
**fbclid_creation_time** | **float** |  | [optional] 
**fbp** | **str** |  | [optional] 
**gad_source** | **str** |  | [optional] 
**gbraid** | **str** |  | [optional] 
**gc_id** | **str** |  | [optional] 
**gclid** | **str** |  | [optional] 
**rdt_cid** | **str** |  | [optional] 
**host** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**msclkid** | **str** | The MSCLKID that led to the conversion (see below for click ID information). The MSCLKID is a GUID (32 characters) that is unique for each ad click | [optional] 
**li_fat_id** | **str** | The LinkedIn Fat ID that led to the conversion (see below for click ID information). The Fat ID is a GUID (32 characters) that is unique for each ad click | [optional] 
**pathname** | **str** |  | [optional] 
**referrer** | **str** | The referrer URL of the current page | [optional] 
**screen_height** | **float** |  | [optional] 
**screen_width** | **float** |  | [optional] 
**title** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**user_agent_full_list** | **str** |  | [optional] 
**utm_campaign** | **str** |  | [optional] 
**utm_content** | **str** |  | [optional] 
**utm_medium** | **str** |  | [optional] 
**utm_name** | **str** |  | [optional] 
**ttclid** | **str** |  | [optional] 
**utm_source** | **str** |  | [optional] 
**utm_term** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**wbraid** | **str** | ?wbraid&#x3D;1 | [optional] 

## Example

```python
from oursprivacy_client.models.track_request_default_properties import TrackRequestDefaultProperties

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRequestDefaultProperties from a JSON string
track_request_default_properties_instance = TrackRequestDefaultProperties.from_json(json)
# print the JSON string representation of the object
print(TrackRequestDefaultProperties.to_json())

# convert the object into a dict
track_request_default_properties_dict = track_request_default_properties_instance.to_dict()
# create an instance of TrackRequestDefaultProperties from a dict
track_request_default_properties_from_dict = TrackRequestDefaultProperties.from_dict(track_request_default_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


