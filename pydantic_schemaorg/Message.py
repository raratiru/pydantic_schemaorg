from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    See: https://schema.org/Message
    Model depth: 3
    """
    type_: str = Field(default="Message", alias='@type', const=True)
    ccRecipient: Optional[Union[List[Union['ContactPoint', 'Person', 'Organization', str]], 'ContactPoint', 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of recipient. The recipient copied on a message.",
    )
    bccRecipient: Optional[Union[List[Union['ContactPoint', 'Person', 'Organization', str]], 'ContactPoint', 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of recipient. The recipient blind copied on a message.",
    )
    dateReceived: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date/time the message was received if a single recipient exists.",
    )
    recipient: Optional[Union[List[Union['Audience', 'ContactPoint', 'Person', 'Organization', str]], 'Audience', 'ContactPoint', 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    toRecipient: Optional[Union[List[Union['Organization', 'Person', 'ContactPoint', 'Audience', str]], 'Organization', 'Person', 'ContactPoint', 'Audience', str]] = Field(
        default=None,
        description="A sub property of recipient. The recipient who was directly sent the message.",
    )
    dateRead: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date/time at which the message has been read by the recipient if a single recipient"
     "exists.",
    )
    sender: Optional[Union[List[Union['Organization', 'Person', 'Audience', str]], 'Organization', 'Person', 'Audience', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    messageAttachment: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="A CreativeWork attached to the message.",
    )
    dateSent: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date/time at which the message was sent.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.CreativeWork import CreativeWork
