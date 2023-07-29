from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class SendAction(TransferAction):
    """The act of physically/electronically dispatching an object for transfer from an origin"
     "to a destination. Related actions: * [[ReceiveAction]]: The reciprocal of SendAction."
     "* [[GiveAction]]: Unlike GiveAction, SendAction does not imply the transfer of ownership"
     "(e.g. I can send you my laptop, but I'm not necessarily giving it to you).

    See: https://schema.org/SendAction
    Model depth: 4
    """
    type_: str = Field(default="SendAction", alias='@type', const=True)
    recipient: Optional[Union[List[Union['Audience', 'ContactPoint', 'Person', 'Organization', str]], 'Audience', 'ContactPoint', 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    deliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="A sub property of instrument. The method of delivery.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
