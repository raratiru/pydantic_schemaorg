from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class GeoCoordinates(StructuredValue):
    """The geographic coordinates of a place or event.

    See: https://schema.org/GeoCoordinates
    Model depth: 4
    """
    type_: str = Field(default="GeoCoordinates", alias='@type', const=True)
    latitude: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    addressCountry: Optional[Union[List[Union[str, 'Text', 'Country']], str, 'Text', 'Country']] = Field(
        default=None,
        description="The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2"
     "country code](http://en.wikipedia.org/wiki/ISO_3166-1).",
    )
    address: Optional[Union[List[Union[str, 'Text', 'PostalAddress']], str, 'Text', 'PostalAddress']] = Field(
        default=None,
        description="Physical address of the item.",
    )
    postalCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The postal code. For example, 94043.",
    )
    elevation: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System))."
     "Values may be of the form 'NUMBER UNIT\_OF\_MEASUREMENT' (e.g., '1,000 m', '3,200 ft')"
     "while numbers alone should be assumed to be a value in meters.",
    )
    longitude: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.PostalAddress import PostalAddress
