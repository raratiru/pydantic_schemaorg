from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictBool, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class PropertyValueSpecification(Intangible):
    """A Property value specification.

    See: https://schema.org/PropertyValueSpecification
    Model depth: 3
    """
    type_: str = Field(default="PropertyValueSpecification", alias='@type', const=True)
    valuePattern: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Specifies a regular expression for testing literal values according to the HTML spec.",
    )
    valueRequired: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether the property must be filled in to complete the action. Default is false.",
    )
    defaultValue: Optional[Union[List[Union[str, 'Text', 'Thing']], str, 'Text', 'Thing']] = Field(
        default=None,
        description="The default value of the input. For properties that expect a literal, the default is a"
     "literal value, for properties that expect an object, it's an ID reference to one of the"
     "current values.",
    )
    readonlyValue: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether or not a property is mutable. Default is false. Specifying this for a property"
     "that also has a value makes it act similar to a \"hidden\" input in an HTML form.",
    )
    stepValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The stepValue attribute indicates the granularity that is expected (and required)"
     "of the value in a PropertyValueSpecification.",
    )
    valueMinLength: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Specifies the minimum allowed range for number of characters in a literal value.",
    )
    valueMaxLength: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Specifies the allowed range for number of characters in a literal value.",
    )
    maxValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The upper value of some characteristic or property.",
    )
    minValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The lower value of some characteristic or property.",
    )
    valueName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates the name of the PropertyValueSpecification to be used in URL templates and"
     "form encoding in a manner analogous to HTML's input@name.",
    )
    multipleValues: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether multiple values are allowed for the property. Default is false.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Number import Number
