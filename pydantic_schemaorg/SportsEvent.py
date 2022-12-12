from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Event import Event


class SportsEvent(Event):
    """Event type: Sports event.

    See: https://schema.org/SportsEvent
    Model depth: 3
    """

    type_: str = Field(default="SportsEvent", alias="@type", const=True)
    competitor: Optional[
        Union[List[Union["SportsTeam", "Person", str]], "SportsTeam", "Person", str]
    ] = Field(
        default=None,
        description="A competitor in a sports event.",
    )
    awayTeam: Optional[
        Union[List[Union["SportsTeam", "Person", str]], "SportsTeam", "Person", str]
    ] = Field(
        default=None,
        description="The away team in a sports event.",
    )
    sport: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="A type of sport (e.g. Baseball).",
    )
    homeTeam: Optional[
        Union[List[Union["SportsTeam", "Person", str]], "SportsTeam", "Person", str]
    ] = Field(
        default=None,
        description="The home team in a sports event.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.SportsTeam import SportsTeam
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
