"""Send one server-side event for a known visitor.

Install the SDK (`pip install oursprivacy-client`), then run:

    OURS_PRIVACY_TOKEN=<source token> python examples/track_event.py

Events go to production unless OURS_PRIVACY_BASE_URL overrides the host. The values below
are samples. Don't put personal or health data or credentials in event properties.
"""

import os
import sys
import uuid

from ours_privacy import OursPrivacy

token = os.environ.get("OURS_PRIVACY_TOKEN")
if not token:
    sys.exit("Missing OURS_PRIVACY_TOKEN: set it to your Source token.")

client = OursPrivacy()
response = client.track.event(
    token=token,
    event="Example Signup",  # must be an allowed event on your Source
    external_id="example-user-123",  # your own identifier for this visitor
    distinct_id=str(uuid.uuid4()),  # reuse this value if you resend, so the event deduplicates
    event_properties={"plan": "example-plan"},
)
print("tracked:", response.success)
