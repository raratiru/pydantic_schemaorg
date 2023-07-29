from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class ReceiveAction(TransferAction):
    """The act of physically/electronically taking delivery of an object that has been transferred"
     "from an origin to a destination. Reciprocal of SendAction. Related actions: * [[SendAction]]:"
     "The reciprocal of ReceiveAction. * [[TakeAction]]: Unlike TakeAction, ReceiveAction"
     "does not imply that the ownership has been transferred (e.g. I can receive a package,"
     "but it does not mean the package is now mine).

    See: https://schema.org/ReceiveAction
    Model depth: 4
    """
    type_: str = Field(default="ReceiveAction", alias='@type', const=True)
    deliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="A sub property of instrument. The method of delivery.",
    )
    sender: Optional[Union[List[Union['Organization', 'Person', 'Audience', str]], 'Organization', 'Person', 'Audience', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Audience import Audience
