from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class DigitalDocument(CreativeWork):
    """An electronic file or document.

    See: https://schema.org/DigitalDocument
    Model depth: 3
    """
    type_: str = Field(default="DigitalDocument", alias='@type', const=True)
    hasDigitalDocumentPermission: Optional[Union[List[Union['DigitalDocumentPermission', str]], 'DigitalDocumentPermission', str]] = Field(
        default=None,
        description="A permission related to the access to this document (e.g. permission to read or write"
     "an electronic document). For a public document, specify a grantee with an Audience with"
     "audienceType equal to \"public\".",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DigitalDocumentPermission import DigitalDocumentPermission
