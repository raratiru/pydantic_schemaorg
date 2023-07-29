from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Service import Service


class BroadcastService(Service):
    """A delivery service through which content is provided via broadcast over the air or online.

    See: https://schema.org/BroadcastService
    Model depth: 4
    """
    type_: str = Field(default="BroadcastService", alias='@type', const=True)
    broadcastFrequency: Optional[Union[List[Union[str, 'Text', 'BroadcastFrequencySpecification']], str, 'Text', 'BroadcastFrequencySpecification']] = Field(
        default=None,
        description="The frequency used for over-the-air broadcasts. Numeric values or simple ranges, e.g."
     "87-99. In addition a shortcut idiom is supported for frequences of AM and FM radio channels,"
     "e.g. \"87 FM\".",
    )
    inLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    parentService: Optional[Union[List[Union['BroadcastService', str]], 'BroadcastService', str]] = Field(
        default=None,
        description="A broadcast service to which the broadcast service may belong to such as regional variations"
     "of a national channel.",
    )
    broadcastTimezone: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The timezone in [ISO 8601 format](http://en.wikipedia.org/wiki/ISO_8601) for which"
     "the service bases its broadcasts.",
    )
    hasBroadcastChannel: Optional[Union[List[Union['BroadcastChannel', str]], 'BroadcastChannel', str]] = Field(
        default=None,
        description="A broadcast channel of a broadcast service.",
    )
    area: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="The area within which users can expect to reach the broadcast service.",
    )
    broadcastDisplayName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name displayed in the channel guide. For many US affiliates, it is the network name.",
    )
    broadcastAffiliateOf: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The media network(s) whose content is broadcast on this station.",
    )
    broadcaster: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The organization owning or operating the broadcast service.",
    )
    videoFormat: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    callSign: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BroadcastFrequencySpecification import BroadcastFrequencySpecification
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.BroadcastChannel import BroadcastChannel
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.Organization import Organization
