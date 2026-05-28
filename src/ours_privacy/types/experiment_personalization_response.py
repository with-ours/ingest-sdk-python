# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExperimentPersonalizationResponse", "Personalization"]


class Personalization(BaseModel):
    assigned_at: float

    experiment_id: str

    variant_id: str

    experiment_key: Optional[str] = None

    experiment_name: Optional[str] = None

    variant_name: Optional[str] = None


class ExperimentPersonalizationResponse(BaseModel):
    personalizations: List[Personalization]

    success: Literal[True]
