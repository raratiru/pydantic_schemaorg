from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalCondition(MedicalEntity):
    """Any condition of the human body that affects the normal functioning of a person, whether"
     "physically or mentally. Includes diseases, injuries, disabilities, disorders, syndromes,"
     "etc.

    See: https://schema.org/MedicalCondition
    Model depth: 3
    """
    type_: str = Field(default="MedicalCondition", alias='@type', const=True)
    signOrSymptom: Optional[Union[List[Union['MedicalSignOrSymptom', str]], 'MedicalSignOrSymptom', str]] = Field(
        default=None,
        description="A sign or symptom of this condition. Signs are objective or physically observable manifestations"
     "of the medical condition while symptoms are the subjective experience of the medical"
     "condition.",
    )
    naturalProgression: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The expected progression of the condition if it is not treated and allowed to progress"
     "naturally.",
    )
    secondaryPrevention: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A preventative therapy used to prevent reoccurrence of the medical condition after"
     "an initial episode of the condition.",
    )
    epidemiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The characteristics of associated patients, such as age, gender, race etc.",
    )
    possibleTreatment: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A possible treatment to address this condition, sign or symptom.",
    )
    riskFactor: Optional[Union[List[Union['MedicalRiskFactor', str]], 'MedicalRiskFactor', str]] = Field(
        default=None,
        description="A modifiable or non-modifiable factor that increases the risk of a patient contracting"
     "this condition, e.g. age, coexisting condition.",
    )
    status: Optional[Union[List[Union[str, 'Text', 'EventStatusType', 'MedicalStudyStatus']], str, 'Text', 'EventStatusType', 'MedicalStudyStatus']] = Field(
        default=None,
        description="The status of the study (enumerated).",
    )
    pathophysiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated"
     "with this activity or condition.",
    )
    typicalTest: Optional[Union[List[Union['MedicalTest', str]], 'MedicalTest', str]] = Field(
        default=None,
        description="A medical test typically performed given this condition.",
    )
    differentialDiagnosis: Optional[Union[List[Union['DDxElement', str]], 'DDxElement', str]] = Field(
        default=None,
        description="One of a set of differential diagnoses for the condition. Specifically, a closely-related"
     "or competing diagnosis typically considered later in the cognitive process whereby"
     "this medical condition is distinguished from others most likely responsible for a similar"
     "collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses"
     "in a patient.",
    )
    drug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    associatedAnatomy: Optional[Union[List[Union['AnatomicalSystem', 'AnatomicalStructure', 'SuperficialAnatomy', str]], 'AnatomicalSystem', 'AnatomicalStructure', 'SuperficialAnatomy', str]] = Field(
        default=None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",
    )
    possibleComplication: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A possible unexpected and unfavorable evolution of a medical condition. Complications"
     "may include worsening of the signs or symptoms of the disease, extension of the condition"
     "to other organ systems, etc.",
    )
    expectedPrognosis: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The likely outcome in either the short term or long term of the medical condition.",
    )
    stage: Optional[Union[List[Union['MedicalConditionStage', str]], 'MedicalConditionStage', str]] = Field(
        default=None,
        description="The stage of the condition, if applicable.",
    )
    primaryPrevention: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A preventative therapy used to prevent an initial occurrence of the medical condition,"
     "such as vaccination.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.MedicalRiskFactor import MedicalRiskFactor
    from pydantic_schemaorg.EventStatusType import EventStatusType
    from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
    from pydantic_schemaorg.MedicalTest import MedicalTest
    from pydantic_schemaorg.DDxElement import DDxElement
    from pydantic_schemaorg.Drug import Drug
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
    from pydantic_schemaorg.MedicalConditionStage import MedicalConditionStage
