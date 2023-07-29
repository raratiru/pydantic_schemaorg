from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Clip(CreativeWork):
    """A short TV or radio program or a segment/part of a program.

    See: https://schema.org/Clip
    Model depth: 3
    """
    type_: str = Field(default="Clip", alias='@type', const=True)
    partOfSeries: Optional[Union[List[Union['CreativeWorkSeries', str]], 'CreativeWorkSeries', str]] = Field(
        default=None,
        description="The series to which this episode or season belongs.",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    clipNumber: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="Position of the clip within an ordered group of clips.",
    )
    startOffset: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]], StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]] = Field(
        default=None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    endOffset: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]], StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]] = Field(
        default=None,
        description="The end time of the clip expressed as the number of seconds from the beginning of the work.",
    )
    partOfEpisode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="The episode to which this clip belongs.",
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
    partOfSeason: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="The season to which this episode belongs.",
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
    from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.MusicGroup import MusicGroup
    from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
