from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Invoice(Intangible):
    """A statement of the money due for goods or services; a bill.

    See: https://schema.org/Invoice
    Model depth: 3
    """
    type_: str = Field(default="Invoice", alias='@type', const=True)
    accountId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The identifier for the account the payment will be applied to.",
    )
    referencesOrder: Optional[Union[List[Union['Order', str]], 'Order', str]] = Field(
        default=None,
        description="The Order(s) related to this Invoice. One or more Orders may be combined into a single"
     "Invoice.",
    )
    confirmationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",
    )
    paymentDueDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'CategoryCode', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'CategoryCode', 'Thing', 'PhysicalActivityCategory']] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    billingPeriod: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The time interval used to compute the invoice.",
    )
    totalPaymentDue: Optional[Union[List[Union['MonetaryAmount', 'PriceSpecification', str]], 'MonetaryAmount', 'PriceSpecification', str]] = Field(
        default=None,
        description="The total amount due.",
    )
    broker: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    customer: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",
    )
    paymentMethod: Optional[Union[List[Union['PaymentMethod', str]], 'PaymentMethod', str]] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",
    )
    paymentDue: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    paymentStatus: Optional[Union[List[Union[str, 'Text', 'PaymentStatusType']], str, 'Text', 'PaymentStatusType']] = Field(
        default=None,
        description="The status of payment; whether the invoice has been paid or not.",
    )
    paymentMethodId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    scheduledPaymentDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date the invoice is scheduled to be paid.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    minimumPaymentDue: Optional[Union[List[Union['MonetaryAmount', 'PriceSpecification', str]], 'MonetaryAmount', 'PriceSpecification', str]] = Field(
        default=None,
        description="The minimum payment required at this time.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Order import Order
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
    from pydantic_schemaorg.PaymentStatusType import PaymentStatusType
