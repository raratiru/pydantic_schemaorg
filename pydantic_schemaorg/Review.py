from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Review(CreativeWork):
    """A review of an item - for example, of a restaurant, movie, or store.

    See: https://schema.org/Review
    Model depth: 3
    """
    type_: str = Field(default="Review", alias='@type', const=True)
    itemReviewed: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The item that is being reviewed/rated.",
    )
    reviewBody: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The actual body of the review.",
    )
    positiveNotes: Optional[Union[List[Union[str, 'Text', 'ListItem', 'WebContent', 'ItemList']], str, 'Text', 'ListItem', 'WebContent', 'ItemList']] = Field(
        default=None,
        description="Provides positive considerations regarding something, for example product highlights"
     "or (alongside [[negativeNotes]]) pro/con lists for reviews. In the case of a [[Review]],"
     "the property describes the [[itemReviewed]] from the perspective of the review; in"
     "the case of a [[Product]], the product itself is being described. The property values"
     "can be expressed either as unstructured text (repeated as necessary), or if ordered,"
     "as a list (in which case the most positive is at the beginning of the list).",
    )
    associatedReview: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="An associated [[Review]].",
    )
    associatedClaimReview: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="An associated [[ClaimReview]], related by specific common content, topic or claim."
     "The expectation is that this property would be most typically used in cases where a single"
     "activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]]"
     "would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be"
     "used on [[MediaReview]].",
    )
    reviewAspect: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="This Review or Rating is relevant to this part or facet of the itemReviewed.",
    )
    associatedMediaReview: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="An associated [[MediaReview]], related by specific common content, topic or claim."
     "The expectation is that this property would be most typically used in cases where a single"
     "activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]]"
     "would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be"
     "used on [[MediaReview]].",
    )
    reviewRating: Optional[Union[List[Union['Rating', str]], 'Rating', str]] = Field(
        default=None,
        description="The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating```"
     "applies to rating given by the review. The [[aggregateRating]] property applies to"
     "the review itself, as a creative work.",
    )
    negativeNotes: Optional[Union[List[Union[str, 'Text', 'ListItem', 'WebContent', 'ItemList']], str, 'Text', 'ListItem', 'WebContent', 'ItemList']] = Field(
        default=None,
        description="Provides negative considerations regarding something, most typically in pro/con"
     "lists for reviews (alongside [[positiveNotes]]). For symmetry In the case of a [[Review]],"
     "the property describes the [[itemReviewed]] from the perspective of the review; in"
     "the case of a [[Product]], the product itself is being described. Since product descriptions"
     "tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]]"
     "used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used"
     "on [[Product]]. The property values can be expressed either as unstructured text (repeated"
     "as necessary), or if ordered, as a list (in which case the most negative is at the beginning"
     "of the list).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ListItem import ListItem
    from pydantic_schemaorg.WebContent import WebContent
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.Rating import Rating
