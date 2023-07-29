from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.SportsOrganization import SportsOrganization


class SportsTeam(SportsOrganization):
    """Organization: Sports team.

    See: https://schema.org/SportsTeam
    Model depth: 4
    """
    type_: str = Field(default="SportsTeam", alias='@type', const=True)
    athlete: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person that acts as performing member of a sports team; a player as opposed to a coach.",
    )
    gender: Optional[Union[List[Union[str, 'Text', 'GenderType']], str, 'Text', 'GenderType']] = Field(
        default=None,
        description="Gender of something, typically a [[Person]], but possibly also fictional characters,"
     "animals, etc. While https://schema.org/Male and https://schema.org/Female may"
     "be used, text strings are also acceptable for people who do not identify as a binary gender."
     "The [[gender]] property can also be used in an extended sense to cover e.g. the gender"
     "of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities."
     "A mixed-gender [[SportsTeam]] can be indicated with a text value of \"Mixed\".",
    )
    coach: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person that acts in a coaching role for a sports team.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GenderType import GenderType
