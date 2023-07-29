from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.Event import Event


class PublicationEvent(Event):
    """A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork"
     "of any type, e.g. a broadcast event, an on-demand event, a book/journal publication"
     "via a variety of delivery media.

    See: https://schema.org/PublicationEvent
    Model depth: 3
    """
    type_: str = Field(default="PublicationEvent", alias='@type', const=True)
    publishedBy: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An agent associated with the publication event.",
    )
    free: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    publishedOn: Optional[Union[List[Union['BroadcastService', str]], 'BroadcastService', str]] = Field(
        default=None,
        description="A broadcast service associated with the publication event.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.BroadcastService import BroadcastService
