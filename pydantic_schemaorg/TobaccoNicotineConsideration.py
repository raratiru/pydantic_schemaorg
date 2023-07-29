from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class TobaccoNicotineConsideration(AdultOrientedEnumeration):
    """Item contains tobacco and/or nicotine, for example cigars, cigarettes, chewing tobacco,"
     "e-cigarettes, or hookahs.

    See: https://schema.org/TobaccoNicotineConsideration
    Model depth: 5
    """
    type_: str = Field(default="TobaccoNicotineConsideration", alias='@type', const=True)
    
