from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c3(USNonprofitType):
    """Nonprofit501c3: Non-profit type referring to Religious, Educational, Charitable,"
     "Scientific, Literary, Testing for Public Safety, Fostering National or International"
     "Amateur Sports Competition, or Prevention of Cruelty to Children or Animals Organizations.

    See: https://schema.org/Nonprofit501c3
    Model depth: 6
    """
    type_: str = Field(default="Nonprofit501c3", alias='@type', const=True)
    
