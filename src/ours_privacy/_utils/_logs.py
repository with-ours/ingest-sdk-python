import os
import logging
from typing import Mapping, Sequence, cast

# Names whose values never reach debug output, ignoring case, underscores and hyphens.
SENSITIVE_NAMES = frozenset(
    [
        "accesstoken",
        "apikey",
        "authorization",
        "clientsecret",
        "cookie",
        "password",
        "refreshtoken",
        "setcookie",
        "token",
        "xapikey",
    ]
)

logger: logging.Logger = logging.getLogger("ours_privacy")
httpx_logger: logging.Logger = logging.getLogger("httpx")


def redact_sensitive(value: object) -> object:
    """Returns a copy of `value` with sensitive values replaced, for debug output only."""
    if isinstance(value, Mapping):
        return {
            key: "***"
            if isinstance(key, str) and key.lower().replace("_", "").replace("-", "") in SENSITIVE_NAMES
            else redact_sensitive(item)
            for key, item in cast("Mapping[object, object]", value).items()
        }
    if isinstance(value, (list, tuple)):
        return [redact_sensitive(item) for item in cast("Sequence[object]", value)]
    return value


def _basic_config() -> None:
    # e.g. [2023-10-05 14:12:26 - ours_privacy._base_client:818 - DEBUG] HTTP Request: POST http://127.0.0.1:4010/foo/bar "200 OK"
    logging.basicConfig(
        format="[%(asctime)s - %(name)s:%(lineno)d - %(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )


def setup_logging() -> None:
    env = os.environ.get("OURS_PRIVACY_LOG")
    if env == "debug":
        _basic_config()
        logger.setLevel(logging.DEBUG)
        httpx_logger.setLevel(logging.DEBUG)
    elif env == "info":
        _basic_config()
        logger.setLevel(logging.INFO)
        httpx_logger.setLevel(logging.INFO)
