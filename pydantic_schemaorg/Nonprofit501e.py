from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501e(USNonprofitType):
    """Nonprofit501e: Non-profit type referring to Cooperative Hospital Service Organizations.

    See: https://schema.org/Nonprofit501e
    Model depth: 6
    """
    type_: str = Field(default="Nonprofit501e", alias='@type', const=True)
    
