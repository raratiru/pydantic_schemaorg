from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalGuideline(MedicalEntity):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement"
     "that denotes how to diagnose and treat a particular condition. Note: this type should"
     "be used to tag the actual guideline recommendation; if the guideline recommendation"
     "occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall"
     "article, not this type. Note also: the organization making the recommendation should"
     "be captured in the recognizingAuthority base property of MedicalEntity.

    See: https://schema.org/MedicalGuideline
    Model depth: 3
    """
    type_: str = Field(default="MedicalGuideline", alias='@type', const=True)
    guidelineSubject: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        default=None,
        description="The medical conditions, treatments, etc. that are the subject of the guideline.",
    )
    evidenceLevel: Optional[Union[List[Union['MedicalEvidenceLevel', str]], 'MedicalEvidenceLevel', str]] = Field(
        default=None,
        description="Strength of evidence of the data used to formulate the guideline (enumerated).",
    )
    evidenceOrigin: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.",
    )
    guidelineDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="Date on which this guideline's recommendation was made.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Date import Date
