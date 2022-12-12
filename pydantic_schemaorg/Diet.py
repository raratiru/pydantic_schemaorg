from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.LifestyleModification import LifestyleModification
from pydantic_schemaorg.CreativeWork import CreativeWork


class Diet(LifestyleModification, CreativeWork):
    """A strategy of regulating the intake of food to achieve or maintain a specific health-related"
     "goal.

    See: https://schema.org/Diet
    Model depth: 3
    """
    type_: str = Field(default="Diet", alias='@type', const=True)
    endorsers: Optional[Union[List[Union['Organization', 'Person', str]], 'Organization', 'Person', str]] = Field(
        default=None,
        description="People or organizations that endorse the plan.",
    )
    dietFeatures: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Nutritional information specific to the dietary plan. May include dietary recommendations"
     "on what foods to avoid, what foods to consume, and specific alterations/deviations"
     "from the USDA or other regulatory body's approved dietary guidelines.",
    )
    physiologicalBenefits: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Specific physiologic benefits associated to the plan.",
    )
    expertConsiderations: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Medical expert advice related to the plan.",
    )
    risks: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Specific physiologic risks associated to the diet plan.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Text import Text
