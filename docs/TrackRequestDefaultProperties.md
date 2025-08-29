# TrackRequestDefaultProperties

These properties are used throughout the Ours app to pass known values onto destinations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_bot** | **bool** | Whether we have detected that the user is a bot. This is set automatically by the Ours server primarily for events tracked through the web SDK. | [optional] 
**ad_id** | **str** | The ad id for detected in the session. This is set by the web sdk automatically. | [optional] 
**adset_id** | **str** | The adset id for detected in the session. This is set by the web sdk automatically. | [optional] 
**campaign_id** | **str** | The campaign id for detected in the session. This is set by the web sdk automatically. | [optional] 
**encoding** | **str** | The browsers encoding. Ex: UTF-8 | [optional] 
**browser_name** | **str** | The name of the browser. Ex: Chrome | [optional] 
**browser_version** | **str** | The version of the browser. Ex: 114.0 | [optional] 
**cpu_architecture** | **str** | The architecture of the CPU. Ex: x64 | [optional] 
**device_type** | **str** | The type of device the user is using. Ex: mobile | [optional] 
**device_model** | **str** | The model of the device. Ex: iPhone 13 | [optional] 
**device_vendor** | **str** | The vendor of the device. Ex: Apple | [optional] 
**engine_name** | **str** | The name of the browser engine. Ex: Blink | [optional] 
**engine_version** | **str** | The version of the browser engine. Ex: 114.0 | [optional] 
**os_name** | **str** | The name of the operating system. Ex: Windows | [optional] 
**os_version** | **str** | The version of the operating system. Ex: 10.0 | [optional] 
**browser_language** | **str** | The language of the browser. Ex: en-US | [optional] 
**current_url** | **str** | The full url (including query params) of the current page | [optional] 
**webview** | **bool** | Whether the user is in a webview. Ex: true | [optional] 
**iframe** | **bool** | Whether the user is in an iframe. Ex: true | [optional] 
**session_count** | **float** | The number of sessions the user has had. Ex: 3 | [optional] 
**active_duration** | **float** | The active time in milliseconds that the user had this tab active | [optional] 
**duration** | **float** | The time in milliseconds since the page was loaded // script was loaded | [optional] 
**epik** | **str** | The Pinterest Click ID. Ex: epik456 | [optional] 
**sacid** | **str** | The StackAdapt Tracking ID. Ex: sacid123 | [optional] 
**fbc** | **str** | Facebook Click ID with prefix format for Conversions API tracking. Ex: fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890 | [optional] 
**fbclid** | **str** | Raw Facebook Click ID query parameter without prefix from ad clicks. Ex: AbCdEfGhIjKlMnOpQrStUvWxYz1234567890 | [optional] 
**fbp** | **str** | Facebook Browser ID parameter for identifying browsers and attributing events. Ex: fb.1.1554763741205.1098115397 | [optional] 
**gad_source** | **str** | The Google Ad Source. Ex: google | [optional] 
**gbraid** | **str** | The Google Braid ID. Ex: gbraid123 | [optional] 
**gclid** | **str** | The Google Click ID. Ex: gclid123 | [optional] 
**ndclid** | **str** | The NextDoor Click ID. Ex: ndclid123 | [optional] 
**dclid** | **str** | The DoubleClick Click ID. Ex: dclid123 | [optional] 
**qclid** | **str** | The Quora Click ID. Ex: qclid123 | [optional] 
**rdt_cid** | **str** | The Reddit Click ID. Ex: rdt_cid123 | [optional] 
**host** | **str** | The host of the current page. Ex: example.com | [optional] 
**ip** | **str** | The IP address of the user. Ex: 127.0.0.1 | [optional] 
**msclkid** | **str** | The Microsoft Click ID. Ex: msclkid123 | [optional] 
**li_fat_id** | **str** | The LinkedIn Click ID. Ex: li_fat_id123 | [optional] 
**pathname** | **str** | The pathname of the current page. Ex: /home | [optional] 
**referrer** | **str** | The referrer URL of the current page | [optional] 
**screen_height** | **float** | The height of the screen. Ex: 1080 | [optional] 
**screen_width** | **float** | The width of the screen. Ex: 1920 | [optional] 
**title** | **str** | The title of the current page | [optional] 
**user_agent** | **str** | The user agent of the browser | [optional] 
**utm_campaign** | **str** | The UTM Campaign. The web SDK automatically captures this from the query params. | [optional] 
**utm_content** | **str** | The UTM Content. The web SDK automatically captures this from the query params. | [optional] 
**utm_medium** | **str** | The UTM Medium. The web SDK automatically captures this from the query params. | [optional] 
**utm_name** | **str** | The UTM Name. The web SDK automatically captures this from the query params. | [optional] 
**ttclid** | **str** | The TikTok Click ID. Ex: ttclid123 | [optional] 
**twclid** | **str** | The Twitter Click ID. Ex: twclid123 | [optional] 
**clickid** | **str** | The Click ID. Ex: clickid123 | [optional] 
**clid** | **str** | The Generic Click ID. Ex: clid123 | [optional] 
**sccid** | **str** | The SnapChat Click ID. Ex: sccid123 | [optional] 
**utm_source** | **str** | The UTM Source. The web SDK automatically captures this from the query params. | [optional] 
**utm_term** | **str** | The UTM Term. The web SDK automatically captures this from the query params. | [optional] 
**version** | **str** | The version of the web SDK | [optional] 
**wbraid** | **str** | The WBRAID Identifier. The web SDK automatically captures this from the query params. | [optional] 
**uafvl** | **str** | User agent as a full list of strings. | [optional] 
**page_hash** | **float** | A random set of numbers for the page load | [optional] 
**sid** | **str** | The session ID as assigned automatically by the web SDK. | [optional] 
**new_s** | **bool** | Deprecated | [optional] 
**fv** | **bool** | Deprecated | [optional] 
**sr** | **str** |  | [optional] 

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


