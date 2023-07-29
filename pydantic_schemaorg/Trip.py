from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import datetime, time


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Trip(Intangible):
    """A trip or journey. An itinerary of visits to one or more places.

    See: https://schema.org/Trip
    Model depth: 3
    """
    type_: str = Field(default="Trip", alias='@type', const=True)
    offers: Optional[Union[List[Union['Offer', 'Demand', str]], 'Offer', 'Demand', str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    partOfTrip: Optional[Union[List[Union['Trip', str]], 'Trip', str]] = Field(
        default=None,
        description="Identifies that this [[Trip]] is a subTrip of another Trip. For example Day 1, Day 2, etc."
     "of a multi-day trip.",
    )
    arrivalTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The expected arrival time.",
    )
    subTrip: Optional[Union[List[Union['Trip', str]], 'Trip', str]] = Field(
        default=None,
        description="Identifies a [[Trip]] that is a subTrip of this Trip. For example Day 1, Day 2, etc. of a"
     "multi-day trip.",
    )
    tripOrigin: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="The location of origin of the trip, prior to any destination(s).",
    )
    itinerary: Optional[Union[List[Union['Place', 'ItemList', str]], 'Place', 'ItemList', str]] = Field(
        default=None,
        description="Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is"
     "important use [[ItemList]] to specify that order (see examples).",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    departureTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The expected departure time.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
