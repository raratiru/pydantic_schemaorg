from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Offer import Offer


class OfferForLease(Offer):
    """An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something,"
     "i.e. an [[Offer]] whose [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.)."
     "See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for background"
     "on the underlying concepts.

    See: https://schema.org/OfferForLease
    Model depth: 4
    """
    type_: str = Field(default="OfferForLease", alias='@type', const=True)
    
