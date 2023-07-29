from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictBool
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FoodEstablishment(LocalBusiness):
    """A food-related business.

    See: https://schema.org/FoodEstablishment
    Model depth: 4
    """
    type_: str = Field(default="FoodEstablishment", alias='@type', const=True)
    hasMenu: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Menu']], AnyUrl, 'URL', str, 'Text', 'Menu']] = Field(
        default=None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    acceptsReservations: Optional[Union[List[Union[AnyUrl, 'URL', StrictBool, 'Boolean', str, 'Text']], AnyUrl, 'URL', StrictBool, 'Boolean', str, 'Text']] = Field(
        default=None,
        description="Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean,"
     "an URL at which reservations can be made or (for backwards compatibility) the strings"
     "```Yes``` or ```No```.",
    )
    starRating: Optional[Union[List[Union['Rating', str]], 'Rating', str]] = Field(
        default=None,
        description="An official rating for a lodging business or food establishment, e.g. from national"
     "associations or standards bodies. Use the author property to indicate the rating organization,"
     "e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).",
    )
    servesCuisine: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The cuisine of the restaurant.",
    )
    menu: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Menu']], AnyUrl, 'URL', str, 'Text', 'Menu']] = Field(
        default=None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Menu import Menu
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Rating import Rating
