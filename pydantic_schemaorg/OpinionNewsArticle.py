from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class OpinionNewsArticle(NewsArticle):
    """An [[OpinionNewsArticle]] is a [[NewsArticle]] that primarily expresses opinions"
     "rather than journalistic reporting of news and events. For example, a [[NewsArticle]]"
     "consisting of a column or [[Blog]]/[[BlogPosting]] entry in the Opinions section of"
     "a news publication.

    See: https://schema.org/OpinionNewsArticle
    Model depth: 5
    """
    type_: str = Field(default="OpinionNewsArticle", alias='@type', const=True)
    
