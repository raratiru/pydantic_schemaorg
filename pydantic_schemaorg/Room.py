from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Accommodation import Accommodation


class Room(Accommodation):
    """A room is a distinguishable space within a structure, usually separated from other spaces"
     "by interior walls (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Room\">http://en.wikipedia.org/wiki/Room</a>)."
     "<br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated document on the"
     "use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Room
    Model depth: 4
    """
    type_: str = Field(default="Room", alias='@type', const=True)
    
