from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Joint(AnatomicalStructure):
    """The anatomical location at which two or more bones make contact.

    See: https://schema.org/Joint
    Model depth: 4
    """
    type_: str = Field(default="Joint", alias='@type', const=True)
    functionalClass: Optional[Union[List[Union[str, 'Text', 'MedicalEntity']], str, 'Text', 'MedicalEntity']] = Field(
        default=None,
        description="The degree of mobility the joint allows.",
    )
    biomechnicalClass: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The biomechanical properties of the bone.",
    )
    structuralClass: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name given to how bone physically connects to each other.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
