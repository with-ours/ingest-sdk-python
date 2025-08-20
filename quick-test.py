from oursprivacy_client import ApiClient, Configuration, OursPrivacyApi, IdentifyRequest, TrackRequest
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()
api_key = os.getenv("API_KEY")

config = Configuration(host = 'https://dev-api.oursprivacy.com/api/v1', ignore_operation_servers=True)
api_client = ApiClient(configuration=config)

api = OursPrivacyApi(api_client)

ireq = IdentifyRequest.from_dict({
  'token': api_key,
  'userId': 'python.developer',
  'userProperties': {}
})

response = api.identify(ireq)
pprint(response)

treq = TrackRequest.from_dict({
  'token': api_key,
  'event': 'Red',
  'userId': 'python.developer'
})

response = api.track(treq)
pprint(response)