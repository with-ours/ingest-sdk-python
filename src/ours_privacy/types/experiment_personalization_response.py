# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExperimentPersonalizationResponse"]


class ExperimentPersonalizationResponse(BaseModel):
    properties: Dict[str, Union[str, float, bool]]
    """
    The visitor traits accumulated by your personalization property rules, keyed by
    property key. Values are always scalars — a string, number, or boolean, or null
    when the captured field was itself empty. Empty for a visitor who has not
    matched any rule yet. These same values are delivered to the visitor's browser
    and are readable by anyone who knows the visitor_id, so never accumulate
    secrets, credentials, PHI, or confidential data into a property.
    """

    success: Literal[True]
