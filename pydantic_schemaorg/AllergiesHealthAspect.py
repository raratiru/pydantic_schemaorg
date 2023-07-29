from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class AllergiesHealthAspect(HealthAspectEnumeration):
    """Content about the allergy-related aspects of a health topic.

    See: https://schema.org/AllergiesHealthAspect
    Model depth: 5
    """
    type_: str = Field(default="AllergiesHealthAspect", alias='@type', const=True)
    
