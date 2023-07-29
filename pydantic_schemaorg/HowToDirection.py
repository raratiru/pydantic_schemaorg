from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToDirection(ListItem, CreativeWork):
    """A direction indicating a single action to do in the instructions for how to achieve a result.

    See: https://schema.org/HowToDirection
    Model depth: 3
    """
    type_: str = Field(default="HowToDirection", alias='@type', const=True)
    tool: Optional[Union[List[Union[str, 'Text', 'HowToTool']], str, 'Text', 'HowToTool']] = Field(
        default=None,
        description="A sub property of instrument. An object used (but not consumed) when performing instructions"
     "or a direction.",
    )
    totalTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The total time required to perform instructions or a direction (including time to prepare"
     "the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    prepTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The length of time it takes to prepare the items to be used in instructions or a direction,"
     "in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    duringMedia: Optional[Union[List[Union[AnyUrl, 'URL', 'MediaObject', str]], AnyUrl, 'URL', 'MediaObject', str]] = Field(
        default=None,
        description="A media object representing the circumstances while performing this direction.",
    )
    supply: Optional[Union[List[Union[str, 'Text', 'HowToSupply']], str, 'Text', 'HowToSupply']] = Field(
        default=None,
        description="A sub-property of instrument. A supply consumed when performing instructions or a direction.",
    )
    performTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The length of time it takes to perform instructions or a direction (not including time"
     "to prepare the supplies), in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    beforeMedia: Optional[Union[List[Union[AnyUrl, 'URL', 'MediaObject', str]], AnyUrl, 'URL', 'MediaObject', str]] = Field(
        default=None,
        description="A media object representing the circumstances before performing this direction.",
    )
    afterMedia: Optional[Union[List[Union[AnyUrl, 'URL', 'MediaObject', str]], AnyUrl, 'URL', 'MediaObject', str]] = Field(
        default=None,
        description="A media object representing the circumstances after performing this direction.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.HowToTool import HowToTool
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.HowToSupply import HowToSupply
