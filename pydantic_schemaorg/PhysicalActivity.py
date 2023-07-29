from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.LifestyleModification import LifestyleModification


class PhysicalActivity(LifestyleModification):
    """Any bodily activity that enhances or maintains physical fitness and overall health"
     "and wellness. Includes activity that is part of daily living and routine, structured"
     "exercise, and exercise prescribed as part of a medical treatment or recovery plan.

    See: https://schema.org/PhysicalActivity
    Model depth: 4
    """
    type_: str = Field(default="PhysicalActivity", alias='@type', const=True)
    epidemiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The characteristics of associated patients, such as age, gender, race etc.",
    )
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'CategoryCode', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'CategoryCode', 'Thing', 'PhysicalActivityCategory']] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    pathophysiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated"
     "with this activity or condition.",
    )
    associatedAnatomy: Optional[Union[List[Union['AnatomicalSystem', 'AnatomicalStructure', 'SuperficialAnatomy', str]], 'AnatomicalSystem', 'AnatomicalStructure', 'SuperficialAnatomy', str]] = Field(
        default=None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
