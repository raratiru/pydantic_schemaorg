from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class AnatomicalStructure(MedicalEntity):
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues,"
     "and cells are all anatomical structures.

    See: https://schema.org/AnatomicalStructure
    Model depth: 3
    """
    type_: str = Field(default="AnatomicalStructure", alias='@type', const=True)
    bodyLocation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Location in the body of the anatomical structure.",
    )
    partOfSystem: Optional[Union[List[Union['AnatomicalSystem', str]], 'AnatomicalSystem', str]] = Field(
        default=None,
        description="The anatomical or organ system that this structure is part of.",
    )
    subStructure: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Component (sub-)structure(s) that comprise this anatomical structure.",
    )
    relatedCondition: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        default=None,
        description="A medical condition associated with this anatomy.",
    )
    connectedTo: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Other anatomical structures to which this structure is connected.",
    )
    relatedTherapy: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A medical therapy related to this anatomy.",
    )
    associatedPathophysiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",
    )
    diagram: Optional[Union[List[Union['ImageObject', str]], 'ImageObject', str]] = Field(
        default=None,
        description="An image containing a diagram that illustrates the structure and/or its component substructures"
     "and/or connections with other structures.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.ImageObject import ImageObject
