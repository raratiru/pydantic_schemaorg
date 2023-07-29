from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import time
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class ShippingDeliveryTime(StructuredValue):
    """ShippingDeliveryTime provides various pieces of information about delivery times"
     "for shipping.

    See: https://schema.org/ShippingDeliveryTime
    Model depth: 4
    """
    type_: str = Field(default="ShippingDeliveryTime", alias='@type', const=True)
    cutoffTime: Optional[Union[List[Union[time, 'Time', str]], time, 'Time', str]] = Field(
        default=None,
        description="Order cutoff time allows merchants to describe the time after which they will no longer"
     "process orders received on that day. For orders processed after cutoff time, one day"
     "gets added to the delivery time estimate. This property is expected to be most typically"
     "used via the [[ShippingRateSettings]] publication pattern. The time is indicated"
     "using the ISO-8601 Time format, e.g. \"23:30:00-05:00\" would represent 6:30 pm Eastern"
     "Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).",
    )
    businessDays: Optional[Union[List[Union['OpeningHoursSpecification', str]], 'OpeningHoursSpecification', str]] = Field(
        default=None,
        description="Days of the week when the merchant typically operates, indicated via opening hours markup.",
    )
    transitTime: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The typical delay the order has been sent for delivery and the goods reach the final customer."
     "Typical properties: minValue, maxValue, unitCode (d for DAY).",
    )
    handlingTime: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The typical delay between the receipt of the order and the goods either leaving the warehouse"
     "or being prepared for pickup, in case the delivery method is on site pickup. Typical properties:"
     "minValue, maxValue, unitCode (d for DAY). This is by common convention assumed to mean"
     "business days (if a unitCode is used, coded as \"d\"), i.e. only counting days when the"
     "business normally operates.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
