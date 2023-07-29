from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OfferShippingDetails(StructuredValue):
    """OfferShippingDetails represents information about shipping destinations. Multiple"
     "of these entities can be used to represent different shipping rates for different destinations:"
     "One entity for Alaska/Hawaii. A different one for continental US. A different one for"
     "all France. Multiple of these entities can be used to represent different shipping costs"
     "and delivery times. Two entities that are identical but differ in rate and time: E.g."
     "Cheaper and slower: $5 in 5-7 days or Fast and expensive: $15 in 1-2 days.

    See: https://schema.org/OfferShippingDetails
    Model depth: 4
    """
    type_: str = Field(default="OfferShippingDetails", alias='@type', const=True)
    doesNotShip: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    shippingDestination: Optional[Union[List[Union['DefinedRegion', str]], 'DefinedRegion', str]] = Field(
        default=None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
     "ways, e.g. postalCode ranges.",
    )
    shippingLabel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    shippingSettingsLink: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Link to a page containing [[ShippingRateSettings]] and [[DeliveryTimeSettings]]"
     "details.",
    )
    shippingOrigin: Optional[Union[List[Union['DefinedRegion', str]], 'DefinedRegion', str]] = Field(
        default=None,
        description="Indicates the origin of a shipment, i.e. where it should be coming from.",
    )
    transitTimeLabel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within"
     "the context of a [[shippingSettingsLink]] cross-reference).",
    )
    depth: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The depth of the item.",
    )
    height: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    shippingRate: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="The shipping rate is the cost of shipping to the specified destination. Typically, the"
     "maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.",
    )
    width: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The width of the item.",
    )
    deliveryTime: Optional[Union[List[Union['ShippingDeliveryTime', str]], 'ShippingDeliveryTime', str]] = Field(
        default=None,
        description="The total delay between the receipt of the order and the goods reaching the final customer.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.DefinedRegion import DefinedRegion
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.ShippingDeliveryTime import ShippingDeliveryTime
