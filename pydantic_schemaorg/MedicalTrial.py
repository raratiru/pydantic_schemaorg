from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalStudy import MedicalStudy


class MedicalTrial(MedicalStudy):
    """A medical trial is a type of medical study that uses a scientific process to compare the"
     "safety and efficacy of medical therapies or medical procedures. In general, medical"
     "trials are controlled and subjects are allocated at random to the different treatment"
     "and/or control groups.

    See: https://schema.org/MedicalTrial
    Model depth: 4
    """
    type_: str = Field(default="MedicalTrial", alias='@type', const=True)
    trialDesign: Optional[Union[List[Union['MedicalTrialDesign', str]], 'MedicalTrialDesign', str]] = Field(
        default=None,
        description="Specifics about the trial design (enumerated).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign
