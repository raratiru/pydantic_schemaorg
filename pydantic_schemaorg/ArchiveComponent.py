from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties"
     "required to describe archival items and collections.

    See: https://schema.org/ArchiveComponent
    Model depth: 3
    """
    type_: str = Field(default="ArchiveComponent", alias='@type', const=True)
    holdingArchive: Optional[Union[List[Union['ArchiveOrganization', str]], 'ArchiveOrganization', str]] = Field(
        default=None,
        description="[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].",
    )
    itemLocation: Optional[Union[List[Union[str, 'Text', 'PostalAddress', 'Place']], str, 'Text', 'PostalAddress', 'Place']] = Field(
        default=None,
        description="Current location of the item.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.ArchiveOrganization import ArchiveOrganization
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Place import Place
