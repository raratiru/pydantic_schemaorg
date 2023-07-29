from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalConditionStage(MedicalIntangible):
    """A stage of a medical condition, such as 'Stage IIIa'.

    See: https://schema.org/MedicalConditionStage
    Model depth: 4
    """
    type_: str = Field(default="MedicalConditionStage", alias='@type', const=True)
    subStageSuffix: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The substage, e.g. 'a' for Stage IIIa.",
    )
    stageAsNumber: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The stage represented as a number, e.g. 3.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
