from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ParcelDelivery(Intangible):
    """The delivery of a parcel either via the postal service or a commercial service.

    See: https://schema.org/ParcelDelivery
    Model depth: 3
    """
    type_: str = Field(default="ParcelDelivery", alias='@type', const=True)
    expectedArrivalUntil: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The latest date the package may arrive.",
    )
    originAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        default=None,
        description="Shipper's address.",
    )
    trackingNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Shipper tracking number.",
    )
    partOfOrder: Optional[Union[List[Union['Order', str]], 'Order', str]] = Field(
        default=None,
        description="The overall order the items in this delivery were included in.",
    )
    expectedArrivalFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The earliest date the package may arrive.",
    )
    hasDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="Method used for delivery or shipping.",
    )
    carrier: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    trackingUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Tracking url for the parcel delivery.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    deliveryStatus: Optional[Union[List[Union['DeliveryEvent', str]], 'DeliveryEvent', str]] = Field(
        default=None,
        description="New entry added as the package passes through each leg of its journey (from shipment to"
     "final delivery).",
    )
    itemShipped: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        default=None,
        description="Item(s) being shipped.",
    )
    deliveryAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        default=None,
        description="Destination address.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Order import Order
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.DeliveryEvent import DeliveryEvent
    from pydantic_schemaorg.Product import Product
