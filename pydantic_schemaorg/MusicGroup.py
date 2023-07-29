from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.PerformingGroup import PerformingGroup


class MusicGroup(PerformingGroup):
    """A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.

    See: https://schema.org/MusicGroup
    Model depth: 4
    """
    type_: str = Field(default="MusicGroup", alias='@type', const=True)
    tracks: Optional[Union[List[Union['MusicRecording', str]], 'MusicRecording', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    track: Optional[Union[List[Union['ItemList', 'MusicRecording', str]], 'ItemList', 'MusicRecording', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the"
     "list should contain items of type MusicRecording.",
    )
    album: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        default=None,
        description="A music album.",
    )
    genre: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    musicGroupMember: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A member of a music group&#x2014;for example, John, Paul, George, or Ringo.",
    )
    albums: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        default=None,
        description="A collection of music albums.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.MusicAlbum import MusicAlbum
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Person import Person
