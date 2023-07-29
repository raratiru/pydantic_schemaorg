from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.LearningResource import LearningResource
from pydantic_schemaorg.CreativeWork import CreativeWork


class Course(LearningResource, CreativeWork):
    """A description of an educational course which may be offered as distinct instances which"
     "take place at different times or take place at different locations, or be offered through"
     "different media or modes of study. An educational course is a sequence of one or more educational"
     "events and/or creative works which aims to build knowledge, competence or ability of"
     "learners.

    See: https://schema.org/Course
    Model depth: 3
    """
    type_: str = Field(default="Course", alias='@type', const=True)
    courseCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The identifier for the [[Course]] used by the course [[provider]] (e.g. CS101 or 6.001).",
    )
    syllabusSections: Optional[Union[List[Union['Syllabus', str]], 'Syllabus', str]] = Field(
        default=None,
        description="Indicates (typically several) Syllabus entities that lay out what each section of the"
     "overall course will cover.",
    )
    totalHistoricalEnrollment: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The total number of students that have enrolled in the history of the course.",
    )
    availableLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]].",
    )
    coursePrerequisites: Optional[Union[List[Union[str, 'Text', 'Course', 'AlignmentObject']], str, 'Text', 'Course', 'AlignmentObject']] = Field(
        default=None,
        description="Requirements for taking the Course. May be completion of another [[Course]] or a textual"
     "description like \"permission of instructor\". Requirements may be a pre-requisite"
     "competency, referenced using [[AlignmentObject]].",
    )
    numberOfCredits: Optional[Union[List[Union[int, 'Integer', 'StructuredValue', str]], int, 'Integer', 'StructuredValue', str]] = Field(
        default=None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    financialAidEligible: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A financial aid type or program which students may use to pay for tuition or fees associated"
     "with the program.",
    )
    occupationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']], AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    hasCourseInstance: Optional[Union[List[Union['CourseInstance', str]], 'CourseInstance', str]] = Field(
        default=None,
        description="An offering of the course at a specific time and place or through specific media or mode"
     "of study or to a specific section of students.",
    )
    educationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']], AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other educational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Syllabus import Syllabus
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.AlignmentObject import AlignmentObject
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.CourseInstance import CourseInstance
