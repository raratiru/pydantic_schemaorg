from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MusicPlaylist import MusicPlaylist


class MusicRelease(MusicPlaylist):
    """A MusicRelease is a specific release of a music album.

    See: https://schema.org/MusicRelease
    Model depth: 4
    """
    type_: str = Field(default="MusicRelease", alias='@type', const=True)
    creditedTo: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The group the release is credited to if different than the byArtist. For example, Red"
     "and Blue is credited to \"Stefani Germanotta Band\", but by Lady Gaga.",
    )
    catalogNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The catalog number for the release.",
    )
    musicReleaseFormat: Optional[Union[List[Union['MusicReleaseFormatType', str]], 'MusicReleaseFormatType', str]] = Field(
        default=None,
        description="Format of this release (the type of recording media used, i.e. compact disc, digital"
     "media, LP, etc.).",
    )
    duration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    recordLabel: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The label that issued the release.",
    )
    releaseOf: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        default=None,
        description="The album this is a release of.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.MusicAlbum import MusicAlbum
