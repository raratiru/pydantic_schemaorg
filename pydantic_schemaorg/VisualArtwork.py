from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class VisualArtwork(CreativeWork):
    """A work of art that is primarily visual in character.

    See: https://schema.org/VisualArtwork
    Model depth: 3
    """
    type_: str = Field(default="VisualArtwork", alias='@type', const=True)
    inker: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who traces over the pencil drawings in ink after pencils are complete.",
    )
    artworkSurface: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.",
    )
    colorist: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who adds color to inked drawings.",
    )
    artist: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The primary artist for a work in a medium other than pencils or digital line art--for example,"
     "if the primary artwork is done in watercolors or digital paints.",
    )
    letterer: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who adds lettering, including speech balloons and sound effects, to"
     "artwork.",
    )
    depth: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The depth of the item.",
    )
    height: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    artMedium: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The material used. (E.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype,"
     "Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)",
    )
    surface: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="A material used as a surface in some artwork, e.g. Canvas, Paper, Wood, Board, etc.",
    )
    artEdition: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="The number of copies when multiple copies of a piece of artwork are produced - e.g. for"
     "a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in"
     "this example \"20\").",
    )
    width: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The width of the item.",
    )
    penciler: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who draws the primary narrative artwork.",
    )
    artform: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Integer import Integer
