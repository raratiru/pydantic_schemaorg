from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class ArchiveOrganization(LocalBusiness):
    """An organization with archival holdings. An organization which keeps and preserves"
     "archival material and typically makes it accessible to the public.

    See: https://schema.org/ArchiveOrganization
    Model depth: 4
    """
    type_: str = Field(default="ArchiveOrganization", alias='@type', const=True)
    archiveHeld: Optional[Union[List[Union['ArchiveComponent', str]], 'ArchiveComponent', str]] = Field(
        default=None,
        description="Collection, [fonds](https://en.wikipedia.org/wiki/Fonds), or item held, kept"
     "or maintained by an [[ArchiveOrganization]].",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.ArchiveComponent import ArchiveComponent
