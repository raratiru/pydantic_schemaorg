from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryC(DrugPregnancyCategory):
    """A designation by the US FDA signifying that animal reproduction studies have shown an"
     "adverse effect on the fetus and there are no adequate and well-controlled studies in"
     "humans, but potential benefits may warrant use of the drug in pregnant women despite"
     "potential risks.

    See: https://schema.org/FDAcategoryC
    Model depth: 6
    """
    type_: str = Field(default="FDAcategoryC", alias='@type', const=True)
    
