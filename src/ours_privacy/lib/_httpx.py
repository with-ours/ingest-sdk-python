from typing import TYPE_CHECKING
from importlib import import_module

if TYPE_CHECKING:
    import httpx2 as httpx
    from httpx2 import (
        URL as URL,
        Proxy as Proxy,
        Timeout as Timeout,
        Response as Response,
        BaseTransport as BaseTransport,
        AsyncBaseTransport as AsyncBaseTransport,
    )
else:
    try:
        # Preserve the public HTTPX types used by existing installations.
        import httpx
    except ModuleNotFoundError as exc:
        if exc.name != "httpx":
            raise
        import httpx2 as httpx

    URL = httpx.URL
    Proxy = httpx.Proxy
    Timeout = httpx.Timeout
    Response = httpx.Response
    BaseTransport = httpx.BaseTransport
    AsyncBaseTransport = httpx.AsyncBaseTransport

HTTPX_DEFAULT_TIMEOUT = import_module(f"{httpx.__name__}._config").DEFAULT_TIMEOUT_CONFIG
