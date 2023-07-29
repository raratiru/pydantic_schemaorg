from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class MusicPlaylist(CreativeWork):
    """A collection of music tracks in playlist form.

    See: https://schema.org/MusicPlaylist
    Model depth: 3
    """
    type_: str = Field(default="MusicPlaylist", alias='@type', const=True)
    tracks: Optional[Union[List[Union['MusicRecording', str]], 'MusicRecording', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    track: Optional[Union[List[Union['ItemList', 'MusicRecording', str]], 'ItemList', 'MusicRecording', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the"
     "list should contain items of type MusicRecording.",
    )
    numTracks: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of tracks in this album or playlist.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.Integer import Integer
