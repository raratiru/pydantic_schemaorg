from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class Eye(PhysicalExam):
    """Eye or ophthalmological function assessment with clinical examination.

    See: https://schema.org/Eye
    Model depth: 5
    """
    type_: str = Field(default="Eye", alias='@type', const=True)
    
