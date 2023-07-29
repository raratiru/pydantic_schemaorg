from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass.

    See: https://schema.org/Permit
    Model depth: 3
    """
    type_: str = Field(default="Permit", alias='@type', const=True)
    validFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    validIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The geographic area where a permit or similar thing is valid.",
    )
    issuedThrough: Optional[Union[List[Union['Service', str]], 'Service', str]] = Field(
        default=None,
        description="The service through which the permit was granted.",
    )
    validFor: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The duration of validity of a permit or similar thing.",
    )
    issuedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The organization issuing the ticket or permit.",
    )
    permitAudience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        default=None,
        description="The target audience for this permit.",
    )
    validUntil: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date when the item is no longer valid.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Audience import Audience
