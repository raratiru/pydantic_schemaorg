from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.InformAction import InformAction


class RsvpAction(InformAction):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    See: https://schema.org/RsvpAction
    Model depth: 6
    """
    type_: str = Field(default="RsvpAction", alias='@type', const=True)
    rsvpResponse: Optional[Union[List[Union['RsvpResponseType', str]], 'RsvpResponseType', str]] = Field(
        default=None,
        description="The response (yes, no, maybe) to the RSVP.",
    )
    additionalNumberOfGuests: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="If responding yes, the number of guests who will attend in addition to the invitee.",
    )
    comment: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        default=None,
        description="Comments, typically from users.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.RsvpResponseType import RsvpResponseType
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Comment import Comment
