from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class HyperToc(CreativeWork):
    """A HyperToc represents a hypertext table of contents for complex media objects, such"
     "as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated"
     "using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the"
     "same larger work is split into multiple files, [[associatedMedia]] can be used on individual"
     "[[HyperTocEntry]] items.

    See: https://schema.org/HyperToc
    Model depth: 3
    """
    type_: str = Field(default="HyperToc", alias='@type', const=True)
    tocEntry: Optional[Union[List[Union['HyperTocEntry', str]], 'HyperTocEntry', str]] = Field(
        default=None,
        description="Indicates a [[HyperTocEntry]] in a [[HyperToc]].",
    )
    associatedMedia: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        default=None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
    from pydantic_schemaorg.MediaObject import MediaObject
