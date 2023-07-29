from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl
from datetime import date


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Legislation(CreativeWork):
    """A legal document such as an act, decree, bill, etc. (enforceable or not) or a component"
     "of a legal act (like an article).

    See: https://schema.org/Legislation
    Model depth: 3
    """
    type_: str = Field(default="Legislation", alias='@type', const=True)
    legislationPassedBy: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The person or organization that originally passed or made the law: typically parliament"
     "(for primary legislation) or government (for secondary legislation). This indicates"
     "the \"legal author\" of the law, as opposed to its physical author.",
    )
    legislationIdentifier: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="An identifier for the legislation. This can be either a string-based identifier, like"
     "the CELEX at EU level or the NOR in France, or a web-based, URL/URI identifier, like an"
     "ELI (European Legislation Identifier) or an URN-Lex.",
    )
    legislationTransposes: Optional[Union[List[Union['Legislation', str]], 'Legislation', str]] = Field(
        default=None,
        description="Indicates that this legislation (or part of legislation) fulfills the objectives set"
     "by another legislation, by passing appropriate implementation measures. Typically,"
     "some legislations of European Union's member states or regions transpose European"
     "Directives. This indicates a legally binding link between the 2 legislations.",
    )
    legislationApplies: Optional[Union[List[Union['Legislation', str]], 'Legislation', str]] = Field(
        default=None,
        description="Indicates that this legislation (or part of a legislation) somehow transfers another"
     "legislation in a different legislative context. This is an informative link, and it"
     "has no legal value. For legally-binding links of transposition, use the <a href=\"/legislationTransposes\">legislationTransposes</a>"
     "property. For example an informative consolidated law of a European Union's member"
     "state \"applies\" the consolidated version of the European Directive implemented"
     "in it.",
    )
    jurisdiction: Optional[Union[List[Union[str, 'Text', 'AdministrativeArea']], str, 'Text', 'AdministrativeArea']] = Field(
        default=None,
        description="Indicates a legal jurisdiction, e.g. of some legislation, or where some government"
     "service is based.",
    )
    legislationConsolidates: Optional[Union[List[Union['Legislation', str]], 'Legislation', str]] = Field(
        default=None,
        description="Indicates another legislation taken into account in this consolidated legislation"
     "(which is usually the product of an editorial process that revises the legislation)."
     "This property should be used multiple times to refer to both the original version or the"
     "previous consolidated version, and to the legislations making the change.",
    )
    legislationResponsible: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An individual or organization that has some kind of responsibility for the legislation."
     "Typically the ministry who is/was in charge of elaborating the legislation, or the adressee"
     "for potential questions about the legislation once it is published.",
    )
    legislationLegalForce: Optional[Union[List[Union['LegalForceStatus', str]], 'LegalForceStatus', str]] = Field(
        default=None,
        description="Whether the legislation is currently in force, not in force, or partially in force.",
    )
    legislationDateVersion: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The point-in-time at which the provided description of the legislation is valid (e.g.:"
     "when looking at the law on the 2016-04-07 (= dateVersion), I get the consolidation of"
     "2015-04-12 of the \"National Insurance Contributions Act 2015\")",
    )
    legislationChanges: Optional[Union[List[Union['Legislation', str]], 'Legislation', str]] = Field(
        default=None,
        description="Another legislation that this legislation changes. This encompasses the notions of"
     "amendment, replacement, correction, repeal, or other types of change. This may be a"
     "direct change (textual or non-textual amendment) or a consequential or indirect change."
     "The property is to be used to express the existence of a change relationship between two"
     "acts rather than the existence of a consolidated version of the text that shows the result"
     "of the change. For consolidation relationships, use the <a href=\"/legislationConsolidates\">legislationConsolidates</a>"
     "property.",
    )
    legislationJurisdiction: Optional[Union[List[Union[str, 'Text', 'AdministrativeArea']], str, 'Text', 'AdministrativeArea']] = Field(
        default=None,
        description="The jurisdiction from which the legislation originates.",
    )
    legislationType: Optional[Union[List[Union[str, 'Text', 'CategoryCode']], str, 'Text', 'CategoryCode']] = Field(
        default=None,
        description="The type of the legislation. Examples of values are \"law\", \"act\", \"directive\","
     "\"decree\", \"regulation\", \"statutory instrument\", \"loi organique\", \"règlement"
     "grand-ducal\", etc., depending on the country.",
    )
    legislationDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date of adoption or signature of the legislation. This is the date at which the text"
     "is officially aknowledged to be a legislation, even though it might not even be published"
     "or in force.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.LegalForceStatus import LegalForceStatus
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.CategoryCode import CategoryCode
