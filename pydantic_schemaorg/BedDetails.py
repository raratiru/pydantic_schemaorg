from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class BedDetails(Intangible):
    """An entity holding detailed information about the available bed types, e.g. the quantity"
     "of twin beds for a hotel room. For the single case of just one bed of a certain type, you can"
     "use bed directly with a text. See also [[BedType]] (under development).

    See: https://schema.org/BedDetails
    Model depth: 3
    """
    type_: str = Field(default="BedDetails", alias='@type', const=True)
    numberOfBeds: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The quantity of the given bed type available in the HotelRoom, Suite, House, or Apartment.",
    )
    typeOfBed: Optional[Union[List[Union[str, 'Text', 'BedType']], str, 'Text', 'BedType']] = Field(
        default=None,
        description="The type of bed to which the BedDetail refers, i.e. the type of bed available in the quantity"
     "indicated by quantity.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BedType import BedType
