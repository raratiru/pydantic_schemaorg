from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MediaObject import MediaObject


class VideoObject(MediaObject):
    """A video file.

    See: https://schema.org/VideoObject
    Model depth: 4
    """
    type_: str = Field(default="VideoObject", alias='@type', const=True)
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    embeddedTextCaption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    videoQuality: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The quality of the video.",
    )
    caption: Optional[Union[List[Union[str, 'Text', 'MediaObject']], str, 'Text', 'MediaObject']] = Field(
        default=None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    videoFrameSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The frame size of the video.",
    )
    transcript: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If this MediaObject is an AudioObject or VideoObject, the transcript of that object.",
    )
    musicBy: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )
    directors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    director: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    actor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.MusicGroup import MusicGroup
