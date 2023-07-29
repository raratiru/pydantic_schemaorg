from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class Periodical(CreativeWorkSeries):
    """A publication in any medium issued in successive parts bearing numerical or chronological"
     "designations and intended to continue indefinitely, such as a magazine, scholarly"
     "journal, or newspaper. See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    See: https://schema.org/Periodical
    Model depth: 4
    """
    type_: str = Field(default="Periodical", alias='@type', const=True)
    
