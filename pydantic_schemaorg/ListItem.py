from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ListItem(Intangible):
    """An list item, e.g. a step in a checklist or how-to description.

    See: https://schema.org/ListItem
    Model depth: 3
    """
    type_: str = Field(default="ListItem", alias='@type', const=True)
    position: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="The position of an item in a series or sequence of items.",
    )
    nextItem: Optional[Union[List[Union['ListItem', str]], 'ListItem', str]] = Field(
        default=None,
        description="A link to the ListItem that follows the current one.",
    )
    item: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').",
    )
    previousItem: Optional[Union[List[Union['ListItem', str]], 'ListItem', str]] = Field(
        default=None,
        description="A link to the ListItem that precedes the current one.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
