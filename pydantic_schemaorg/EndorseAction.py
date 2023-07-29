from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class EndorseAction(ReactAction):
    """An agent approves/certifies/likes/supports/sanctions an object.

    See: https://schema.org/EndorseAction
    Model depth: 5
    """
    type_: str = Field(default="EndorseAction", alias='@type', const=True)
    endorsee: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The person/organization being supported.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
