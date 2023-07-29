from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class MerchantReturnPolicy(Intangible):
    """A MerchantReturnPolicy provides information about product return policies associated"
     "with an [[Organization]], [[Product]], or [[Offer]].

    See: https://schema.org/MerchantReturnPolicy
    Model depth: 3
    """
    type_: str = Field(default="MerchantReturnPolicy", alias='@type', const=True)
    inStoreReturnsOffered: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Are in-store returns offered? (For more advanced return methods use the [[returnMethod]]"
     "property.)",
    )
    itemCondition: Optional[Union[List[Union['OfferItemCondition', str]], 'OfferItemCondition', str]] = Field(
        default=None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",
    )
    merchantReturnLink: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Specifies a Web page or service by URL, for product returns.",
    )
    returnPolicyCategory: Optional[Union[List[Union['MerchantReturnEnumeration', str]], 'MerchantReturnEnumeration', str]] = Field(
        default=None,
        description="Specifies an applicable return policy (from an enumeration).",
    )
    returnMethod: Optional[Union[List[Union['ReturnMethodEnumeration', str]], 'ReturnMethodEnumeration', str]] = Field(
        default=None,
        description="The type of return method offered, specified from an enumeration.",
    )
    itemDefectReturnFees: Optional[Union[List[Union['ReturnFeesEnumeration', str]], 'ReturnFeesEnumeration', str]] = Field(
        default=None,
        description="The type of return fees for returns of defect products.",
    )
    merchantReturnDays: Optional[Union[List[Union[datetime, 'DateTime', int, 'Integer', date, 'Date', str]], datetime, 'DateTime', int, 'Integer', date, 'Date', str]] = Field(
        default=None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that"
     "a product can be returned. Used when the [[returnPolicyCategory]] property is specified"
     "as [[MerchantReturnFiniteReturnWindow]].",
    )
    additionalProperty: Optional[Union[List[Union['PropertyValue', str]], 'PropertyValue', str]] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g."
     "a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    refundType: Optional[Union[List[Union['RefundTypeEnumeration', str]], 'RefundTypeEnumeration', str]] = Field(
        default=None,
        description="A refund type, from an enumerated list.",
    )
    returnLabelSource: Optional[Union[List[Union['ReturnLabelSourceEnumeration', str]], 'ReturnLabelSourceEnumeration', str]] = Field(
        default=None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a product returned for any reason.",
    )
    customerRemorseReturnFees: Optional[Union[List[Union['ReturnFeesEnumeration', str]], 'ReturnFeesEnumeration', str]] = Field(
        default=None,
        description="The type of return fees if the product is returned due to customer remorse.",
    )
    restockingFee: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]] = Field(
        default=None,
        description="Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use"
     "[[Number]] to specify a percentage of the product price paid by the customer.",
    )
    itemDefectReturnShippingFeesAmount: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="Amount of shipping costs for defect product returns. Applicable when property [[itemDefectReturnFees]]"
     "equals [[ReturnShippingFees]].",
    )
    returnFees: Optional[Union[List[Union['ReturnFeesEnumeration', str]], 'ReturnFeesEnumeration', str]] = Field(
        default=None,
        description="The type of return fees for purchased products (for any return reason).",
    )
    customerRemorseReturnLabelSource: Optional[Union[List[Union['ReturnLabelSourceEnumeration', str]], 'ReturnLabelSourceEnumeration', str]] = Field(
        default=None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a product returned due to customer remorse.",
    )
    itemDefectReturnLabelSource: Optional[Union[List[Union['ReturnLabelSourceEnumeration', str]], 'ReturnLabelSourceEnumeration', str]] = Field(
        default=None,
        description="The method (from an enumeration) by which the customer obtains a return shipping label"
     "for a defect product.",
    )
    applicableCountry: Optional[Union[List[Union[str, 'Text', 'Country']], str, 'Text', 'Country']] = Field(
        default=None,
        description="A country where a particular merchant return policy applies to, for example the two-letter"
     "ISO 3166-1 alpha-2 country code.",
    )
    customerRemorseReturnShippingFeesAmount: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="The amount of shipping costs if a product is returned due to customer remorse. Applicable"
     "when property [[customerRemorseReturnFees]] equals [[ReturnShippingFees]].",
    )
    returnPolicySeasonalOverride: Optional[Union[List[Union['MerchantReturnPolicySeasonalOverride', str]], 'MerchantReturnPolicySeasonalOverride', str]] = Field(
        default=None,
        description="Seasonal override of a return policy.",
    )
    returnShippingFeesAmount: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="Amount of shipping costs for product returns (for any reason). Applicable when property"
     "[[returnFees]] equals [[ReturnShippingFees]].",
    )
    returnPolicyCountry: Optional[Union[List[Union[str, 'Text', 'Country']], str, 'Text', 'Country']] = Field(
        default=None,
        description="The country where the product has to be sent to for returns, for example \"Ireland\" using"
     "the [[name]] property of [[Country]]. You can also provide the two-letter [ISO 3166-1"
     "alpha-2 country code](http://en.wikipedia.org/wiki/ISO_3166-1). Note that this"
     "can be different from the country where the product was originally shipped from or sent"
     "to.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.OfferItemCondition import OfferItemCondition
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration
    from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration
    from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration
    from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.MerchantReturnPolicySeasonalOverride import MerchantReturnPolicySeasonalOverride
