from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.MedicalIndication import MedicalIndication


class ApprovedIndication(MedicalIndication):
    """An indication for a medical therapy that has been formally specified or approved by a"
     "regulatory body that regulates use of the therapy; for example, the US FDA approves indications"
     "for most drugs in the US.

    See: https://schema.org/ApprovedIndication
    Model depth: 4
    """
    type_: str = Field(default="ApprovedIndication", alias='@type', const=True)
    
