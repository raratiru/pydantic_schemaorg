from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MusicReleaseFormatType(Enumeration):
    """Format of this release (the type of recording media used, i.e. compact disc, digital"
     "media, LP, etc.).

    See: https://schema.org/MusicReleaseFormatType
    Model depth: 4
    """
    type_: str = Field(default="MusicReleaseFormatType", alias='@type', const=True)
    
