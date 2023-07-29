from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class AdultOrientedEnumeration(Enumeration):
    """Enumeration of considerations that make a product relevant or potentially restricted"
     "for adults only.

    See: https://schema.org/AdultOrientedEnumeration
    Model depth: 4
    """
    type_: str = Field(default="AdultOrientedEnumeration", alias='@type', const=True)
    
