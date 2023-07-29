from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalGuideline import MedicalGuideline


class MedicalGuidelineRecommendation(MedicalGuideline):
    """A guideline recommendation that is regarded as efficacious and where quality of the"
     "data supporting the recommendation is sound.

    See: https://schema.org/MedicalGuidelineRecommendation
    Model depth: 4
    """
    type_: str = Field(default="MedicalGuidelineRecommendation", alias='@type', const=True)
    recommendationStrength: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Strength of the guideline's recommendation (e.g. 'class I').",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
