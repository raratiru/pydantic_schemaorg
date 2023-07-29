from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowTo(CreativeWork):
    """Instructions that explain how to achieve a result by performing a sequence of steps.

    See: https://schema.org/HowTo
    Model depth: 3
    """
    type_: str = Field(default="HowTo", alias='@type', const=True)
    tool: Optional[Union[List[Union[str, 'Text', 'HowToTool']], str, 'Text', 'HowToTool']] = Field(
        default=None,
        description="A sub property of instrument. An object used (but not consumed) when performing instructions"
     "or a direction.",
    )
    totalTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The total time required to perform instructions or a direction (including time to prepare"
     "the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    steps: Optional[Union[List[Union[str, 'Text', 'ItemList', 'CreativeWork']], str, 'Text', 'ItemList', 'CreativeWork']] = Field(
        default=None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally"
     "misnamed 'steps'; 'step' is preferred).",
    )
    prepTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The length of time it takes to prepare the items to be used in instructions or a direction,"
     "in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    supply: Optional[Union[List[Union[str, 'Text', 'HowToSupply']], str, 'Text', 'HowToSupply']] = Field(
        default=None,
        description="A sub-property of instrument. A supply consumed when performing instructions or a direction.",
    )
    performTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The length of time it takes to perform instructions or a direction (not including time"
     "to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    estimatedCost: Optional[Union[List[Union[str, 'Text', 'MonetaryAmount']], str, 'Text', 'MonetaryAmount']] = Field(
        default=None,
        description="The estimated cost of the supply or supplies consumed when performing instructions.",
    )
    step: Optional[Union[List[Union[str, 'Text', 'CreativeWork', 'HowToStep', 'HowToSection']], str, 'Text', 'CreativeWork', 'HowToStep', 'HowToSection']] = Field(
        default=None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection.",
    )
    yield_: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        default=None,alias="yield",
        description="The quantity that results by performing instructions. For example, a paper airplane,"
     "10 personalized candles.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.HowToTool import HowToTool
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.HowToSupply import HowToSupply
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.HowToStep import HowToStep
    from pydantic_schemaorg.HowToSection import HowToSection
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
