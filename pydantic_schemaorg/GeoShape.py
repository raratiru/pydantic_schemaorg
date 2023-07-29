from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class GeoShape(StructuredValue):
    """The geographic shape of a place. A GeoShape can be described using several properties"
     "whose values are based on latitude/longitude pairs. Either whitespace or commas can"
     "be used to separate latitude and longitude; whitespace should be used when writing a"
     "list of several such points.

    See: https://schema.org/GeoShape
    Model depth: 4
    """
    type_: str = Field(default="GeoShape", alias='@type', const=True)
    addressCountry: Optional[Union[List[Union[str, 'Text', 'Country']], str, 'Text', 'Country']] = Field(
        default=None,
        description="The country. For example, USA. You can also provide the two-letter [ISO 3166-1 alpha-2"
     "country code](http://en.wikipedia.org/wiki/ISO_3166-1).",
    )
    box: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A box is the area enclosed by the rectangle formed by two points. The first point is the"
     "lower corner, the second point is the upper corner. A box is expressed as two points separated"
     "by a space character.",
    )
    address: Optional[Union[List[Union[str, 'Text', 'PostalAddress']], str, 'Text', 'PostalAddress']] = Field(
        default=None,
        description="Physical address of the item.",
    )
    postalCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The postal code. For example, 94043.",
    )
    line: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A line is a point-to-point path consisting of two or more points. A line is expressed as"
     "a series of two or more point objects separated by space.",
    )
    circle: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A circle is the circular region of a specified radius centered at a specified latitude"
     "and longitude. A circle is expressed as a pair followed by a radius in meters.",
    )
    elevation: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The elevation of a location ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System))."
     "Values may be of the form 'NUMBER UNIT\_OF\_MEASUREMENT' (e.g., '1,000 m', '3,200 ft')"
     "while numbers alone should be assumed to be a value in meters.",
    )
    polygon: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A polygon is the area enclosed by a point-to-point path for which the starting and ending"
     "points are the same. A polygon is expressed as a series of four or more space delimited"
     "points where the first and final points are identical.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Number import Number
