"""Backfill historical events through /batch and resend only the rows that failed to queue.

Install the SDK (`pip install oursprivacy-client`), then run:

    OURS_PRIVACY_TOKEN=<source token> python examples/batch_backfill.py

Events go to production unless OURS_PRIVACY_BASE_URL overrides the host. The values below
are samples. The program exits non-zero if any row is left over.

The supported backfill window is 1 year. An older time is moved to the edge of the window,
not rejected. The generated `time` field docs say 7 days, which is out of date. The sample
rows below are a few days old.

A partial failure is HTTP 207, which the SDK returns rather than raises, so check every row.
Resend queue_failed rows unchanged. Correct invalid_event rows before sending them again.
"""

import os
import sys
import time

from ours_privacy import APIError, OursPrivacy
from ours_privacy.types.batch_create_params import Event

DAY_MS = 86_400_000
MAX_ATTEMPTS = 3

token = os.environ.get("OURS_PRIVACY_TOKEN")
if not token:
    sys.exit("Missing OURS_PRIVACY_TOKEN: set it to your Source token.")

client = OursPrivacy()

# distinct_id is required on batch rows. Keep it stable so a resend deduplicates.
now_ms = time.time() * 1000
pending: list[Event] = [
    {
        "event": "Example Import",  # must be an allowed event on your Source
        "distinct_id": f"example-import-{days_ago}",
        "external_id": "example-user-123",
        "time": now_ms - days_ago * DAY_MS,
        "event_properties": {"plan": "example-plan"},
    }
    for days_ago in (3, 4, 5)
]
invalid = 0

for attempt in range(1, MAX_ATTEMPTS + 1):
    if not pending:
        break
    if attempt > 1:
        time.sleep(attempt)

    try:
        response = client.batch.create(token=token, events=pending)
    except APIError as error:  # the whole request failed, after the SDK's own retries
        sys.exit(f"Backfill stopped with {len(pending)} rows not sent: {error}")
    print(f"attempt {attempt}: accepted={response.accepted} failed={response.failed}")

    # `index` points into the rows sent in this request, not the original list.
    retry: list[Event] = []
    for result in response.results:
        if result.success is True:
            continue
        if result.code == "queue_failed":
            retry.append(pending[result.index])
        else:
            invalid += 1
            print(f"row {pending[result.index]['distinct_id']} is invalid: {result.message}", file=sys.stderr)
    pending = retry

if pending or invalid:
    sys.exit(f"Backfill incomplete: {len(pending)} not queued, {invalid} invalid.")
print("backfill complete")
