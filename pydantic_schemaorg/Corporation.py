from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class Corporation(Organization):
    """Organization: A business corporation.

    See: https://schema.org/Corporation
    Model depth: 3
    """
    type_: str = Field(default="Corporation", alias='@type', const=True)
    tickerSymbol: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The exchange traded instrument associated with a Corporation object. The tickerSymbol"
     "is expressed as an exchange and an instrument name separated by a space character. For"
     "the exchange component of the tickerSymbol attribute, we recommend using the controlled"
     "vocabulary of Market Identifier Codes (MIC) specified in ISO 15022.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
