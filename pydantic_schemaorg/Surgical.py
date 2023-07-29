from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Surgical(MedicalSpecialty):
    """A specific branch of medical science that pertains to treating diseases, injuries and"
     "deformities by manual and instrumental means.

    See: https://schema.org/Surgical
    Model depth: 6
    """
    type_: str = Field(default="Surgical", alias='@type', const=True)
    
