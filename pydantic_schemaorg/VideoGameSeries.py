from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class VideoGameSeries(CreativeWorkSeries):
    """A video game series.

    See: https://schema.org/VideoGameSeries
    Model depth: 4
    """
    type_: str = Field(default="VideoGameSeries", alias='@type', const=True)
    characterAttribute: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A piece of data that represents a particular aspect of a fictional character (skill,"
     "power, character points, advantage, disadvantage).",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    gamePlatform: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing']], AnyUrl, 'URL', str, 'Text', 'Thing']] = Field(
        default=None,
        description="The electronic systems used to play <a href=\"http://en.wikipedia.org/wiki/Category:Video_game_platforms\">video"
     "games</a>.",
    )
    episodes: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="An episode of a TV/radio series or season.",
    )
    season: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWorkSeason', str]], AnyUrl, 'URL', 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="A season in a media series.",
    )
    cheatCode: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="Cheat codes to the game.",
    )
    containsSeason: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="A season that is part of the media series.",
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
    seasons: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="A season in a media series.",
    )
    numberOfSeasons: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of seasons in this series.",
    )
    gameLocation: Optional[Union[List[Union[AnyUrl, 'URL', 'PostalAddress', 'Place', str]], AnyUrl, 'URL', 'PostalAddress', 'Place', str]] = Field(
        default=None,
        description="Real or fictional location of the game (or part of game).",
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
    quest: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The task that a player-controlled character, or group of characters may complete in"
     "order to gain a reward.",
    )
    numberOfPlayers: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="Indicate how many people can play this game (minimum, maximum, or range).",
    )
    playMode: Optional[Union[List[Union['GamePlayMode', str]], 'GamePlayMode', str]] = Field(
        default=None,
        description="Indicates whether this game is multi-player, co-op or single-player. The game can be"
     "marked as multi-player, co-op and single-player at the same time.",
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
    gameItem: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="An item is an object within the game world that can be collected by a player or, occasionally,"
     "a non-player character.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.MusicGroup import MusicGroup
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.GamePlayMode import GamePlayMode
