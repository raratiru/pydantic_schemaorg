from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Language(Intangible):
    """Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code"
     "tags expressed in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag)"
     "can be used via the [[alternateName]] property. The Language type previously also covered"
     "programming languages such as Scheme and Lisp, which are now best represented using"
     "[[ComputerLanguage]].

    See: https://schema.org/Language
    Model depth: 3
    """
    type_: str = Field(default="Language", alias='@type', const=True)
    
