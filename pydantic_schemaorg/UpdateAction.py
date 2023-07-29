from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Action import Action


class UpdateAction(Action):
    """The act of managing by changing/editing the state of the object.

    See: https://schema.org/UpdateAction
    Model depth: 3
    """
    type_: str = Field(default="UpdateAction", alias='@type', const=True)
    targetCollection: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The collection target of the action.",
    )
    collection: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The collection target of the action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
