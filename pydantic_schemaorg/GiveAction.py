from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class GiveAction(TransferAction):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction."
     "Related actions: * [[TakeAction]]: Reciprocal of GiveAction. * [[SendAction]]: Unlike"
     "SendAction, GiveAction implies that ownership is being transferred (e.g. I may send"
     "my laptop to you, but that doesn't mean I'm giving it to you).

    See: https://schema.org/GiveAction
    Model depth: 4
    """
    type_: str = Field(default="GiveAction", alias='@type', const=True)
    recipient: Optional[Union[List[Union['Audience', 'ContactPoint', 'Person', 'Organization', str]], 'Audience', 'ContactPoint', 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
