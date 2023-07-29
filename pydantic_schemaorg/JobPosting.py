from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class JobPosting(Intangible):
    """A listing that describes a job opening in a certain organization.

    See: https://schema.org/JobPosting
    Model depth: 3
    """
    type_: str = Field(default="JobPosting", alias='@type', const=True)
    applicationContact: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="Contact details for further information relevant to this job posting.",
    )
    jobStartDate: Optional[Union[List[Union[date, 'Date', str, 'Text']], date, 'Date', str, 'Text']] = Field(
        default=None,
        description="The date on which a successful applicant for this job would be expected to start work."
     "Choose a specific date in the future or use the jobImmediateStart property to indicate"
     "the position is to be filled as soon as possible.",
    )
    jobLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="A (typically single) geographic location associated with the job position.",
    )
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
    securityClearanceRequirement: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="A description of any security clearance requirements of the job.",
    )
    baseSalary: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', 'PriceSpecification', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', 'PriceSpecification', str]] = Field(
        default=None,
        description="The base salary of the job or of an employee in an EmployeeRole.",
    )
    qualifications: Optional[Union[List[Union[str, 'Text', 'EducationalOccupationalCredential']], str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="Specific qualifications required for this role or Occupation.",
    )
    workHours: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).",
    )
    benefits: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Description of benefits associated with the job.",
    )
    hiringOrganization: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="Organization or Person offering the job position.",
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
    validThrough: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    estimatedSalary: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmountDistribution', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmountDistribution', 'MonetaryAmount', str]] = Field(
        default=None,
        description="An estimated salary for a job posting or occupation, based on a variety of variables including,"
     "but not limited to industry, job title, and location. Estimated salaries are often computed"
     "by outside organizations rather than the hiring organization, who may not have committed"
     "to the estimated value.",
    )
    employmentUnit: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="Indicates the department, unit and/or facility where the employee reports and/or in"
     "which the job is to be performed.",
    )
    relevantOccupation: Optional[Union[List[Union['Occupation', str]], 'Occupation', str]] = Field(
        default=None,
        description="The Occupation for the JobPosting.",
    )
    incentiveCompensation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Description of bonus and commission compensation aspects of the job.",
    )
    employerOverview: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A description of the employer, career opportunities and work environment for this position.",
    )
    salaryCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217))"
     "used for the main salary information in this job posting or for this employee.",
    )
    experienceInPlaceOfEducation: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates whether a [[JobPosting]] will accept experience (as indicated by [[OccupationalExperienceRequirements]])"
     "in place of its formal educational qualifications (as indicated by [[educationRequirements]])."
     "If true, indicates that satisfying one of these requirements is sufficient.",
    )
    eligibilityToWorkRequirement: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The legal requirements such as citizenship, visa and other documentation required"
     "for an applicant to this job.",
    )
    datePosted: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Publication date of an online listing.",
    )
    applicantLocationRequirements: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The location(s) applicants can apply from. This is usually used for telecommuting jobs"
     "where the applicant does not need to be in a physical office. Note: This should not be used"
     "for citizenship or work visa requirements.",
    )
    jobBenefits: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Description of benefits associated with the job.",
    )
    title: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The title of the job.",
    )
    specialCommitments: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any special commitments associated with this job posting. Valid entries include VeteranCommit,"
     "MilitarySpouseCommit, etc.",
    )
    employmentType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).",
    )
    educationRequirements: Optional[Union[List[Union[str, 'Text', 'EducationalOccupationalCredential']], str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="Educational background needed for the position or Occupation.",
    )
    incentives: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Description of bonus and commission compensation aspects of the job.",
    )
    sensoryRequirement: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A description of any sensory requirements and levels necessary to function on the job,"
     "including hearing and vision. Defined terms such as those in O*net may be used, but note"
     "that there is no way to specify the level of ability as well as its nature when using a defined"
     "term.",
    )
    jobLocationType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A description of the job location (e.g. TELECOMMUTE for telecommute jobs).",
    )
    totalJobOpenings: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of positions open for this job posting. Use a positive integer. Do not use if"
     "the number of positions is unclear or not known.",
    )
    jobImmediateStart: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="An indicator as to whether a position is available for an immediate start.",
    )
    industry: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The industry associated with the job position.",
    )
    physicalRequirement: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A description of the types of physical activity associated with the job. Defined terms"
     "such as those in O*net may be used, but note that there is no way to specify the level of ability"
     "as well as its nature when using a defined term.",
    )
    directApply: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates whether an [[url]] that is associated with a [[JobPosting]] enables direct"
     "application for the job, via the posting website. A job posting is considered to have"
     "directApply of [[True]] if an application process for the specified job can be directly"
     "initiated via the url(s) given (noting that e.g. multiple internet domains might nevertheless"
     "be involved at an implementation level). A value of [[False]] is appropriate if there"
     "is no clear path to applying directly online for the specified job, navigating directly"
     "from the JobPosting url(s) supplied.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.OccupationalExperienceRequirements import OccupationalExperienceRequirements
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
    from pydantic_schemaorg.Occupation import Occupation
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Integer import Integer
