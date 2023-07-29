from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class CreativeWorkSeason(CreativeWork):
    """A media season, e.g. TV, radio, video game etc.

    See: https://schema.org/CreativeWorkSeason
    Model depth: 3
    """
    type_: str = Field(default="CreativeWorkSeason", alias='@type', const=True)
    partOfSeries: Optional[Union[List[Union['CreativeWorkSeries', str]], 'CreativeWorkSeries', str]] = Field(
        default=None,
        description="The series to which this episode or season belongs.",
    )
    episodes: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="An episode of a TV/radio series or season.",
    )
    startDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    seasonNumber: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="Position of the season within an ordered group of seasons.",
    )
    trailer: Optional[Union[List[Union['VideoObject', str]], 'VideoObject', str]] = Field(
        default=None,
        description="The trailer of a movie or TV/radio series, season, episode, etc.",
    )
    productionCompany: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The production company or studio responsible for the item, e.g. series, video game,"
     "episode etc.",
    )
    episode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="An episode of a TV, radio or game media within a series or season.",
    )
    director: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    numberOfEpisodes: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of episodes in this season or series.",
    )
    actor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    endDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
