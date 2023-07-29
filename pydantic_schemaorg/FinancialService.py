from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FinancialService(LocalBusiness):
    """Financial services business.

    See: https://schema.org/FinancialService
    Model depth: 4
    """
    type_: str = Field(default="FinancialService", alias='@type', const=True)
    feesAndCommissionsSpecification: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
     "product, or by a financial service organization.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
