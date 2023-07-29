from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class HealthInsurancePlan(Intangible):
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs.

    See: https://schema.org/HealthInsurancePlan
    Model depth: 3
    """
    type_: str = Field(default="HealthInsurancePlan", alias='@type', const=True)
    includesHealthPlanFormulary: Optional[Union[List[Union['HealthPlanFormulary', str]], 'HealthPlanFormulary', str]] = Field(
        default=None,
        description="Formularies covered by this plan.",
    )
    healthPlanMarketingUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL that goes directly to the plan brochure for the specific standard plan or plan"
     "variation.",
    )
    usesHealthPlanIdStandard: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The standard for interpreting the Plan ID. The preferred is \"HIOS\". See the Centers"
     "for Medicare & Medicaid Services for more details.",
    )
    contactPoint: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    healthPlanDrugTier: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The tier(s) of drugs offered by this formulary or insurance plan.",
    )
    healthPlanDrugOption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="TODO.",
    )
    benefitsSummaryUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL that goes directly to the summary of benefits and coverage for the specific standard"
     "plan or plan variation.",
    )
    includesHealthPlanNetwork: Optional[Union[List[Union['HealthPlanNetwork', str]], 'HealthPlanNetwork', str]] = Field(
        default=None,
        description="Networks covered by this plan.",
    )
    healthPlanId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The 14-character, HIOS-generated Plan ID number. (Plan IDs must be unique, even across"
     "different markets.)",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.HealthPlanFormulary import HealthPlanFormulary
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.HealthPlanNetwork import HealthPlanNetwork
