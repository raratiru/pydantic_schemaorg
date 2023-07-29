from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class BioChemEntity(Thing):
    """Any biological, chemical, or biochemical thing. For example: a protein; a gene; a chemical;"
     "a synthetic chemical.

    See: https://schema.org/BioChemEntity
    Model depth: 2
    """
    type_: str = Field(default="BioChemEntity", alias='@type', const=True)
    isEncodedByBioChemEntity: Optional[Union[List[Union['Gene', str]], 'Gene', str]] = Field(
        default=None,
        description="Another BioChemEntity encoding by this one.",
    )
    hasMolecularFunction: Optional[Union[List[Union[AnyUrl, 'URL', 'PropertyValue', 'DefinedTerm', str]], AnyUrl, 'URL', 'PropertyValue', 'DefinedTerm', str]] = Field(
        default=None,
        description="Molecular function performed by this BioChemEntity; please use PropertyValue if you"
     "want to include any evidence.",
    )
    bioChemSimilarity: Optional[Union[List[Union['BioChemEntity', str]], 'BioChemEntity', str]] = Field(
        default=None,
        description="A similar BioChemEntity, e.g., obtained by fingerprint similarity algorithms.",
    )
    hasBioChemEntityPart: Optional[Union[List[Union['BioChemEntity', str]], 'BioChemEntity', str]] = Field(
        default=None,
        description="Indicates a BioChemEntity that (in some sense) has this BioChemEntity as a part.",
    )
    isPartOfBioChemEntity: Optional[Union[List[Union['BioChemEntity', str]], 'BioChemEntity', str]] = Field(
        default=None,
        description="Indicates a BioChemEntity that is (in some sense) a part of this BioChemEntity.",
    )
    biologicalRole: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="A role played by the BioChemEntity within a biological context.",
    )
    bioChemInteraction: Optional[Union[List[Union['BioChemEntity', str]], 'BioChemEntity', str]] = Field(
        default=None,
        description="A BioChemEntity that is known to interact with this item.",
    )
    isLocatedInSubcellularLocation: Optional[Union[List[Union[AnyUrl, 'URL', 'PropertyValue', 'DefinedTerm', str]], AnyUrl, 'URL', 'PropertyValue', 'DefinedTerm', str]] = Field(
        default=None,
        description="Subcellular location where this BioChemEntity is located; please use PropertyValue"
     "if you want to include any evidence.",
    )
    hasRepresentation: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'PropertyValue']], AnyUrl, 'URL', str, 'Text', 'PropertyValue']] = Field(
        default=None,
        description="A common representation such as a protein sequence or chemical structure for this entity."
     "For images use schema.org/image.",
    )
    funding: Optional[Union[List[Union['Grant', str]], 'Grant', str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    isInvolvedInBiologicalProcess: Optional[Union[List[Union[AnyUrl, 'URL', 'PropertyValue', 'DefinedTerm', str]], AnyUrl, 'URL', 'PropertyValue', 'DefinedTerm', str]] = Field(
        default=None,
        description="Biological process this BioChemEntity is involved in; please use PropertyValue if"
     "you want to include any evidence.",
    )
    taxonomicRange: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Taxon', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'Taxon', 'DefinedTerm']] = Field(
        default=None,
        description="The taxonomic grouping of the organism that expresses, encodes, or in some way related"
     "to the BioChemEntity.",
    )
    associatedDisease: Optional[Union[List[Union[AnyUrl, 'URL', 'PropertyValue', 'MedicalCondition', str]], AnyUrl, 'URL', 'PropertyValue', 'MedicalCondition', str]] = Field(
        default=None,
        description="Disease associated to this BioChemEntity. Such disease can be a MedicalCondition or"
     "a URL. If you want to add an evidence supporting the association, please use PropertyValue.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Gene import Gene
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.Taxon import Taxon
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
