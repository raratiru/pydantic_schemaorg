from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Collection(CreativeWork):
    """A collection of items, e.g. creative works or products.

    See: https://schema.org/Collection
    Model depth: 3
    """
    type_: str = Field(default="Collection", alias='@type', const=True)
    collectionSize: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of items in the [[Collection]].",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
