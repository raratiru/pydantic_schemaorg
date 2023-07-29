from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game.

    See: https://schema.org/GameServer
    Model depth: 3
    """
    type_: str = Field(default="GameServer", alias='@type', const=True)
    playersOnline: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Number of players on the server.",
    )
    game: Optional[Union[List[Union['VideoGame', str]], 'VideoGame', str]] = Field(
        default=None,
        description="Video game which is played on this server.",
    )
    serverStatus: Optional[Union[List[Union['GameServerStatus', str]], 'GameServerStatus', str]] = Field(
        default=None,
        description="Status of a game server.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.VideoGame import VideoGame
    from pydantic_schemaorg.GameServerStatus import GameServerStatus
