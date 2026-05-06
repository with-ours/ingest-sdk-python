# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BatchCreateResponse", "Result"]


class Result(BaseModel):
    index: int

    success: Literal[True]


class BatchCreateResponse(BaseModel):
    accepted: int

    failed: Literal[0]

    results: List[Result]

    success: Literal[True]
