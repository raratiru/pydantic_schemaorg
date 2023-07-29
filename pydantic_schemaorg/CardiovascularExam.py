from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.PhysicalExam import PhysicalExam


class CardiovascularExam(PhysicalExam):
    """Cardiovascular system assessment with clinical examination.

    See: https://schema.org/CardiovascularExam
    Model depth: 5
    """
    type_: str = Field(default="CardiovascularExam", alias='@type', const=True)
    
