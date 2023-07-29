from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Order(Intangible):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line"
     "items, each represented by an Offer that has been accepted by the customer.

    See: https://schema.org/Order
    Model depth: 3
    """
    type_: str = Field(default="Order", alias='@type', const=True)
    orderedItem: Optional[Union[List[Union['Service', 'OrderItem', 'Product', str]], 'Service', 'OrderItem', 'Product', str]] = Field(
        default=None,
        description="The item ordered.",
    )
    partOfInvoice: Optional[Union[List[Union['Invoice', str]], 'Invoice', str]] = Field(
        default=None,
        description="The order is being paid as part of the referenced Invoice.",
    )
    seller: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    confirmationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",
    )
    paymentDueDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    paymentUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL for sending a payment.",
    )
    orderDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Date order was placed.",
    )
    isGift: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates whether the offer was accepted as a gift for someone other than the buyer.",
    )
    acceptedOffer: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        default=None,
        description="The offer(s) -- e.g., product, quantity and price combinations -- included in the order.",
    )
    discount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="Any discount applied (to an Order).",
    )
    broker: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    orderNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The identifier of the transaction.",
    )
    customer: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",
    )
    paymentMethod: Optional[Union[List[Union['PaymentMethod', str]], 'PaymentMethod', str]] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",
    )
    merchant: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="'merchant' is an out-dated term for 'seller'.",
    )
    paymentDue: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    discountCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency of the discount. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    orderStatus: Optional[Union[List[Union['OrderStatus', str]], 'OrderStatus', str]] = Field(
        default=None,
        description="The current status of the order.",
    )
    paymentMethodId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    discountCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Code used to redeem a discount.",
    )
    billingAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        default=None,
        description="The billing address for the order.",
    )
    orderDelivery: Optional[Union[List[Union['ParcelDelivery', str]], 'ParcelDelivery', str]] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.OrderItem import OrderItem
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Invoice import Invoice
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
    from pydantic_schemaorg.OrderStatus import OrderStatus
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.ParcelDelivery import ParcelDelivery
