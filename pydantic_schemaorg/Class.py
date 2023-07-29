from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Class(Intangible):
    """A class, also often called a 'Type'; equivalent to rdfs:Class.

    See: https://schema.org/Class
    Model depth: 3
    """
    type_: str = Field(default="Class", alias='@type', const=True)
    supersededBy: Optional[Union[List[Union['Enumeration', 'Class', 'Property', str]], 'Enumeration', 'Class', 'Property', str]] = Field(
        default=None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Enumeration import Enumeration
    from pydantic_schemaorg.Property import Property
