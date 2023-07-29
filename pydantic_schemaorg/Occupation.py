from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Occupation(Intangible):
    """A profession, may involve prolonged training and/or a formal qualification.

    See: https://schema.org/Occupation
    Model depth: 3
    """
    type_: str = Field(default="Occupation", alias='@type', const=True)
    responsibilities: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Responsibilities associated with this role or Occupation.",
    )
    occupationalCategory: Optional[Union[List[Union[str, 'Text', 'CategoryCode']], str, 'Text', 'CategoryCode']] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    qualifications: Optional[Union[List[Union[str, 'Text', 'EducationalOccupationalCredential']], str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="Specific qualifications required for this role or Occupation.",
    )
    skills: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A statement of knowledge, skill, ability, task or any other assertion expressing a competency"
     "that is desired or required to fulfill this role or to work in this occupation.",
    )
    experienceRequirements: Optional[Union[List[Union[str, 'Text', 'OccupationalExperienceRequirements']], str, 'Text', 'OccupationalExperienceRequirements']] = Field(
        default=None,
        description="Description of skills and experience needed for the position or Occupation.",
    )
    estimatedSalary: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmountDistribution', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmountDistribution', 'MonetaryAmount', str]] = Field(
        default=None,
        description="An estimated salary for a job posting or occupation, based on a variety of variables including,"
     "but not limited to industry, job title, and location. Estimated salaries are often computed"
     "by outside organizations rather than the hiring organization, who may not have committed"
     "to the estimated value.",
    )
    occupationLocation: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The region/country for which this occupational description is appropriate. Note that"
     "educational requirements and qualifications can vary between jurisdictions.",
    )
    educationRequirements: Optional[Union[List[Union[str, 'Text', 'EducationalOccupationalCredential']], str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="Educational background needed for the position or Occupation.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.OccupationalExperienceRequirements import OccupationalExperienceRequirements
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
