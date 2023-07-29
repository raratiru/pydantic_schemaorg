from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.PeopleAudience import PeopleAudience


class ParentAudience(PeopleAudience):
    """A set of characteristics describing parents, who can be interested in viewing some content.

    See: https://schema.org/ParentAudience
    Model depth: 5
    """
    type_: str = Field(default="ParentAudience", alias='@type', const=True)
    childMaxAge: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Maximal age of the child.",
    )
    childMinAge: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Minimal age of the child.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
