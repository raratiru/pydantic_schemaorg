from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Place import Place


class TouristAttraction(Place):
    """A tourist attraction. In principle any Thing can be a [[TouristAttraction]], from a"
     "[[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]]. This"
     "Type can be used on its own to describe a general [[TouristAttraction]], or be used as"
     "an [[additionalType]] to add tourist attraction properties to any other type. (See"
     "examples below)

    See: https://schema.org/TouristAttraction
    Model depth: 3
    """
    type_: str = Field(default="TouristAttraction", alias='@type', const=True)
    availableLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]].",
    )
    touristType: Optional[Union[List[Union[str, 'Text', 'Audience']], str, 'Text', 'Audience']] = Field(
        default=None,
        description="Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular"
     "country, etc.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Audience import Audience
