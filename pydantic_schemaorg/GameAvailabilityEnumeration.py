from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class GameAvailabilityEnumeration(Enumeration):
    """For a [[VideoGame]], such as used with a [[PlayGameAction]], an enumeration of the kind"
     "of game availability offered.

    See: https://schema.org/GameAvailabilityEnumeration
    Model depth: 4
    """
    type_: str = Field(default="GameAvailabilityEnumeration", alias='@type', const=True)
    
