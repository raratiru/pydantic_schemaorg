from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class Hotel(LodgingBusiness):
    """A hotel is an establishment that provides lodging paid on a short-term basis (source:"
     "Wikipedia, the free encyclopedia, see http://en.wikipedia.org/wiki/Hotel). <br"
     "/><br /> See also the <a href=\"/docs/hotels.html\">dedicated document on the use"
     "of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Hotel
    Model depth: 5
    """
    type_: str = Field(default="Hotel", alias='@type', const=True)
    
