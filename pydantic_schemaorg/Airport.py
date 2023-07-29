from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class Airport(CivicStructure):
    """An airport.

    See: https://schema.org/Airport
    Model depth: 4
    """
    type_: str = Field(default="Airport", alias='@type', const=True)
    icaoCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="ICAO identifier for an airport.",
    )
    iataCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="IATA identifier for an airline or airport.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
