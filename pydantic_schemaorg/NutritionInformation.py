from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class NutritionInformation(StructuredValue):
    """Nutritional information about the recipe.

    See: https://schema.org/NutritionInformation
    Model depth: 4
    """
    type_: str = Field(default="NutritionInformation", alias='@type', const=True)
    sodiumContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of milligrams of sodium.",
    )
    carbohydrateContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of carbohydrates.",
    )
    fatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of fat.",
    )
    cholesterolContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of milligrams of cholesterol.",
    )
    calories: Optional[Union[List[Union['Energy', str]], 'Energy', str]] = Field(
        default=None,
        description="The number of calories.",
    )
    unsaturatedFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of unsaturated fat.",
    )
    sugarContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of sugar.",
    )
    transFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of trans fat.",
    )
    proteinContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of protein.",
    )
    saturatedFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of saturated fat.",
    )
    servingSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The serving size, in terms of the number of volume or mass.",
    )
    fiberContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of fiber.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Mass import Mass
    from pydantic_schemaorg.Energy import Energy
    from pydantic_schemaorg.Text import Text
