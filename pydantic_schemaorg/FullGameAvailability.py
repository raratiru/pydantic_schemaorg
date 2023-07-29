from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GameAvailabilityEnumeration import GameAvailabilityEnumeration


class FullGameAvailability(GameAvailabilityEnumeration):
    """Indicates full game availability.

    See: https://schema.org/FullGameAvailability
    Model depth: 5
    """
    type_: str = Field(default="FullGameAvailability", alias='@type', const=True)
    
