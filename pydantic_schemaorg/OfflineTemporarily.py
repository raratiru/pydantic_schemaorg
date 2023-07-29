from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.GameServerStatus import GameServerStatus


class OfflineTemporarily(GameServerStatus):
    """Game server status: OfflineTemporarily. Server is offline now but it can be online soon.

    See: https://schema.org/OfflineTemporarily
    Model depth: 6
    """
    type_: str = Field(default="OfflineTemporarily", alias='@type', const=True)
    
