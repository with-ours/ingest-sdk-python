# Batch

Types:

```python
from ours_privacy.types import BatchCreateResponse
```

Methods:

- <code title="post /batch">client.batch.<a href="./src/ours_privacy/resources/batch.py">create</a>(\*\*<a href="src/ours_privacy/types/batch_create_params.py">params</a>) -> <a href="./src/ours_privacy/types/batch_create_response.py">BatchCreateResponse</a></code>

# Track

Types:

```python
from ours_privacy.types import TrackEventResponse
```

Methods:

- <code title="post /track">client.track.<a href="./src/ours_privacy/resources/track.py">event</a>(\*\*<a href="src/ours_privacy/types/track_event_params.py">params</a>) -> <a href="./src/ours_privacy/types/track_event_response.py">TrackEventResponse</a></code>

# Visitor

Types:

```python
from ours_privacy.types import VisitorUpsertResponse
```

Methods:

- <code title="post /identify">client.visitor.<a href="./src/ours_privacy/resources/visitor.py">upsert</a>(\*\*<a href="src/ours_privacy/types/visitor_upsert_params.py">params</a>) -> <a href="./src/ours_privacy/types/visitor_upsert_response.py">VisitorUpsertResponse</a></code>

# Experiments

Types:

```python
from ours_privacy.types import ExperimentAssignmentResponse, ExperimentPersonalizationResponse
```

Methods:

- <code title="post /experiments/assignments/{experiment_key}">client.experiments.<a href="./src/ours_privacy/resources/experiments.py">assignment</a>(experiment_key, \*\*<a href="src/ours_privacy/types/experiment_assignment_params.py">params</a>) -> <a href="./src/ours_privacy/types/experiment_assignment_response.py">ExperimentAssignmentResponse</a></code>
- <code title="post /experiments/personalization">client.experiments.<a href="./src/ours_privacy/resources/experiments.py">personalization</a>(\*\*<a href="src/ours_privacy/types/experiment_personalization_params.py">params</a>) -> <a href="./src/ours_privacy/types/experiment_personalization_response.py">ExperimentPersonalizationResponse</a></code>
