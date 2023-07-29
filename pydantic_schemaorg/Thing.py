from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase


class Thing(SchemaOrgBase):
    """The most generic type of item.

    See: https://schema.org/Thing
    Model depth: 1
    """
    type_: str = Field(default="Thing", alias='@type', const=True)
    alternateName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An alias for the item.",
    )
    potentialAction: Optional[Union[List[Union['Action', str]], 'Action', str]] = Field(
        default=None,
        description="Indicates a potential Action, which describes an idealized action in which this thing"
     "would play an 'object' role.",
    )
    sameAs: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="URL of a reference Web page that unambiguously indicates the item's identity. E.g. the"
     "URL of the item's Wikipedia page, Wikidata entry, or official website.",
    )
    subjectOf: Optional[Union[List[Union['CreativeWork', 'Event', str]], 'CreativeWork', 'Event', str]] = Field(
        default=None,
        description="A CreativeWork or Event about this Thing.",
    )
    disambiguatingDescription: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A sub property of description. A short description of the item used to disambiguate from"
     "other, similar items. Information from other properties (in particular, name) may"
     "be necessary for the description to be useful for disambiguation.",
    )
    name: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name of the item.",
    )
    description: Optional[Union[List[Union[str, 'Text', 'TextObject']], str, 'Text', 'TextObject']] = Field(
        default=None,
        description="A description of the item.",
    )
    image: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        default=None,
        description="An image of the item. This can be a [[URL]] or a fully described [[ImageObject]].",
    )
    url: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="URL of the item.",
    )
    identifier: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'PropertyValue']], AnyUrl, 'URL', str, 'Text', 'PropertyValue']] = Field(
        default=None,
        description="The identifier property represents any kind of identifier for any kind of [[Thing]],"
     "such as ISBNs, GTIN codes, UUIDs etc. Schema.org provides dedicated properties for"
     "representing many of these, either as textual strings or as URL (URI) links. See [background"
     "notes](/docs/datamodel.html#identifierBg) for more details.",
    )
    mainEntityOfPage: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="Indicates a page (or other CreativeWork) for which this thing is the main entity being"
     "described. See [background notes](/docs/datamodel.html#mainEntityBackground)"
     "for details.",
    )
    additionalType: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="An additional type for the item, typically used for adding more specific types from external"
     "vocabularies in microdata syntax. This is a relationship between something and a class"
     "that the thing is in. Typically the value is a URI-identified RDF class, and in this case"
     "corresponds to the use of rdf:type in RDF. Text values can be used sparingly, for cases"
     "where useful information can be added without their being an appropriate schema to reference."
     "In the case of text values, the class label should follow the schema.org <a href=\"https://schema.org/docs/styleguide.html\">style"
     "guide</a>",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Action import Action
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.TextObject import TextObject
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.PropertyValue import PropertyValue
