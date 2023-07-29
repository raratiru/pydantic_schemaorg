from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class QualitativeValue(Enumeration):
    """A predefined value for a product characteristic, e.g. the power cord plug type 'US' or"
     "the garment sizes 'S', 'M', 'L', and 'XL'.

    See: https://schema.org/QualitativeValue
    Model depth: 4
    """
    type_: str = Field(default="QualitativeValue", alias='@type', const=True)
    lesser: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than the object.",
    )
    greaterOrEqual: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than or equal to the object.",
    )
    nonEqual: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is not equal"
     "to the object.",
    )
    greater: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is greater"
     "than the object.",
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
    lesserOrEqual: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is lesser"
     "than or equal to the object.",
    )
    valueReference: Optional[Union[List[Union[str, 'Text', 'DefinedTerm', 'QualitativeValue', 'MeasurementTypeEnumeration', 'PropertyValue', 'QuantitativeValue', 'Enumeration', 'StructuredValue']], str, 'Text', 'DefinedTerm', 'QualitativeValue', 'MeasurementTypeEnumeration', 'PropertyValue', 'QuantitativeValue', 'Enumeration', 'StructuredValue']] = Field(
        default=None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",
    )
    equal: Optional[Union[List[Union['QualitativeValue', str]], 'QualitativeValue', str]] = Field(
        default=None,
        description="This ordering relation for qualitative values indicates that the subject is equal to"
     "the object.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Enumeration import Enumeration
    from pydantic_schemaorg.StructuredValue import StructuredValue
