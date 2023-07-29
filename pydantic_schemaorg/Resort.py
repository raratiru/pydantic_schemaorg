from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class Resort(LodgingBusiness):
    """A resort is a place used for relaxation or recreation, attracting visitors for holidays"
     "or vacations. Resorts are places, towns or sometimes commercial establishments operated"
     "by a single company (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Resort\">http://en.wikipedia.org/wiki/Resort</a>)."
     "<br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated document on the"
     "use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Resort
    Model depth: 5
    """
    type_: str = Field(default="Resort", alias='@type', const=True)
    
