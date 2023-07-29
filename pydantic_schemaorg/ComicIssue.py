from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.PublicationIssue import PublicationIssue


class ComicIssue(PublicationIssue):
    """Individual comic issues are serially published as part of a larger series. For the sake"
     "of consistency, even one-shot issues belong to a series comprised of a single issue."
     "All comic issues can be uniquely identified by: the combination of the name and volume"
     "number of the series to which the issue belongs; the issue number; and the variant description"
     "of the issue (if any).

    See: https://schema.org/ComicIssue
    Model depth: 4
    """
    type_: str = Field(default="ComicIssue", alias='@type', const=True)
    inker: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who traces over the pencil drawings in ink after pencils are complete.",
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
    variantCover: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A description of the variant cover for the issue, if the issue is a variant printing. For"
     "example, \"Bryan Hitch Variant Cover\" or \"2nd Printing Variant\".",
    )
    penciler: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The individual who draws the primary narrative artwork.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Text import Text
