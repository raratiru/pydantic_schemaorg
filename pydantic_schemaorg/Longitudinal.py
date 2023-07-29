from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Longitudinal(MedicalObservationalStudyDesign):
    """Unlike cross-sectional studies, longitudinal studies track the same people, and therefore"
     "the differences observed in those people are less likely to be the result of cultural"
     "differences across generations. Longitudinal studies are also used in medicine to"
     "uncover predictors of certain diseases.

    See: https://schema.org/Longitudinal
    Model depth: 6
    """
    type_: str = Field(default="Longitudinal", alias='@type', const=True)
    
