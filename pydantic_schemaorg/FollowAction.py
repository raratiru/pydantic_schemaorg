from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class FollowAction(InteractAction):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically"
     "to get updates polled from. Related actions: * [[BefriendAction]]: Unlike BefriendAction,"
     "FollowAction implies that the connection is *not* necessarily reciprocal. * [[SubscribeAction]]:"
     "Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent"
     "constantly/actively polling for updates. * [[RegisterAction]]: Unlike RegisterAction,"
     "FollowAction implies that the agent is interested in continuing receiving updates"
     "from the object. * [[JoinAction]]: Unlike JoinAction, FollowAction implies that the"
     "agent is interested in getting updates from the object. * [[TrackAction]]: Unlike TrackAction,"
     "FollowAction refers to the polling of updates of all aspects of animate objects rather"
     "than the location of inanimate objects (e.g. you track a package, but you don't follow"
     "it).

    See: https://schema.org/FollowAction
    Model depth: 4
    """
    type_: str = Field(default="FollowAction", alias='@type', const=True)
    followee: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of object. The person or organization being followed.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
