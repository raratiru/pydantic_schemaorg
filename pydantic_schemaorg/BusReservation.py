from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class BusReservation(Reservation):
    """A reservation for bus travel. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See: https://schema.org/BusReservation
    Model depth: 4
    """
    type_: str = Field(default="BusReservation", alias='@type', const=True)
    
