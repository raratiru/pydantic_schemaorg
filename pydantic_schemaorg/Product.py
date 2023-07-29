from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from datetime import date
from pydantic import AnyUrl, StrictBool


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Product(Thing):
    """Any offered product or service. For example: a pair of shoes; a concert ticket; the rental"
     "of a car; a haircut; or an episode of a TV show streamed online.

    See: https://schema.org/Product
    Model depth: 2
    """
    type_: str = Field(default="Product", alias='@type', const=True)
    mobileUrl: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The [[mobileUrl]] property is provided for specific situations in which data consumers"
     "need to determine whether one of several provided URLs is a dedicated 'mobile site'."
     "To discourage over-use, and reflecting intial usecases, the property is expected only"
     "on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology"
     "is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design)"
     "in which content can be flexibly adapted to a wide range of browsing environments. Pages"
     "and sites referenced with the long-established [[url]] property should ideally also"
     "be usable on a wide variety of devices, including mobile phones. In most cases, it would"
     "be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]]"
     "for more mobile-oriented pages. The property is intended for the case when items (primarily"
     "[[Product]] and [[Offer]]) have extra URLs hosted on an additional \"mobile site\""
     "alongside the main one. It should not be taken as an endorsement of this publication style.",
    )
    purchaseDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date the item, e.g. vehicle, was purchased by the current owner.",
    )
    hasAdultConsideration: Optional[Union[List[Union['AdultOrientedEnumeration', str]], 'AdultOrientedEnumeration', str]] = Field(
        default=None,
        description="Used to tag an item to be intended or suitable for consumption or use by adults only.",
    )
    offers: Optional[Union[List[Union['Offer', 'Demand', str]], 'Offer', 'Demand', str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    itemCondition: Optional[Union[List[Union['OfferItemCondition', str]], 'OfferItemCondition', str]] = Field(
        default=None,
        description="A predefined value from OfferItemCondition specifying the condition of the product"
     "or service, or the products or services included in the offer. Also used for product return"
     "policies to specify the condition of products accepted for returns.",
    )
    color: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The color of the product.",
    )
    gtin12: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12"
     "is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference,"
     "and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    awards: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Awards won by or for this item.",
    )
    countryOfAssembly: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The place where the product was assembled.",
    )
    countryOfOrigin: Optional[Union[List[Union['Country', str]], 'Country', str]] = Field(
        default=None,
        description="The country of origin of something, including products as well as creative works such"
     "as movie and TV content. In the case of TV and movie, this would be the country of the principle"
     "offices of the production company or individual responsible for the movie. For other"
     "kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties"
     "such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the"
     "case of products, the country of origin of the product. The exact interpretation of this"
     "may vary by context and product type, and cannot be fully enumerated here.",
    )
    keywords: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",
    )
    material: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Product']], AnyUrl, 'URL', str, 'Text', 'Product']] = Field(
        default=None,
        description="A material that something is made from, e.g. leather, wool, cotton, paper.",
    )
    productID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The product identifier, such as ISBN. For example: ``` meta itemprop=\"productID\""
     "content=\"isbn:123-456-789\" ```.",
    )
    aggregateRating: Optional[Union[List[Union['AggregateRating', str]], 'AggregateRating', str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
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
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'CategoryCode', 'Thing', 'PhysicalActivityCategory']], AnyUrl, 'URL', str, 'Text', 'CategoryCode', 'Thing', 'PhysicalActivityCategory']] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    releaseDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The release date of a product or product model. This can be used to distinguish the exact"
     "variant of a product.",
    )
    sku: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service,"
     "or the product to which the offer refers.",
    )
    productionDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date of production of the item, e.g. vehicle.",
    )
    gtin8: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The GTIN-8 code of the product, or the product to which the offer refers. This code is also"
     "known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    isVariantOf: Optional[Union[List[Union['ProductModel', 'ProductGroup', str]], 'ProductModel', 'ProductGroup', str]] = Field(
        default=None,
        description="Indicates the kind of product that this is a variant of. In the case of [[ProductModel]],"
     "this is a pointer (from a ProductModel) to a base product from which this product is a variant."
     "It is safe to infer that the variant inherits all product features from the base model,"
     "unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the"
     "group description also serves as a template, representing a set of Products that vary"
     "on explicitly defined, specific dimensions only (so it defines both a set of variants,"
     "as well as which values distinguish amongst those variants). When used with [[ProductGroup]],"
     "this property can apply to any [[Product]] included in the group.",
    )
    depth: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The depth of the item.",
    )
    award: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    additionalProperty: Optional[Union[List[Union['PropertyValue', str]], 'PropertyValue', str]] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g."
     "a product feature or another characteristic for which there is no matching property"
     "in schema.org. Note: Publishers should be aware that applications designed to use specific"
     "schema.org properties (e.g. https://schema.org/width, https://schema.org/color,"
     "https://schema.org/gtin13, ...) will typically expect such data to be provided using"
     "those properties, rather than using the generic property/value mechanism.",
    )
    height: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    gtin13: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent"
     "to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into"
     "a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "for more details.",
    )
    isSimilarTo: Optional[Union[List[Union['Service', 'Product', str]], 'Service', 'Product', str]] = Field(
        default=None,
        description="A pointer to another, functionally similar product (or multiple products).",
    )
    asin: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique"
     "identifier assigned by Amazon.com and its partners for product identification within"
     "the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s"
     "article). Note also that this is a definition for how to include ASINs in Schema.org data,"
     "and not a definition of ASINs in general - see documentation from Amazon for authoritative"
     "details. ASINs are most commonly encoded as text strings, but the [asin] property supports"
     "URL/URI as potential values too.",
    )
    isFamilyFriendly: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates whether this content is family friendly.",
    )
    isConsumableFor: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        default=None,
        description="A pointer to another product (or multiple products) for which this product is a consumable.",
    )
    logo: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        default=None,
        description="An associated logo.",
    )
    inProductGroupWithID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]].",
    )
    manufacturer: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The manufacturer of the product.",
    )
    gtin14: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN"
     "Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.",
    )
    isAccessoryOrSparePartFor: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        default=None,
        description="A pointer to another product (or multiple products) for which this product is an accessory"
     "or spare part.",
    )
    isRelatedTo: Optional[Union[List[Union['Service', 'Product', str]], 'Service', 'Product', str]] = Field(
        default=None,
        description="A pointer to another, somehow related product (or multiple products).",
    )
    funding: Optional[Union[List[Union['Grant', str]], 'Grant', str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    slogan: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    audience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    model: Optional[Union[List[Union[str, 'Text', 'ProductModel']], str, 'Text', 'ProductModel']] = Field(
        default=None,
        description="The model of the product. Use with the URL of a ProductModel or a textual representation"
     "of the model identifier. The URL of the ProductModel can be from an external source. It"
     "is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14"
     "and mpn properties.",
    )
    width: Optional[Union[List[Union['Distance', 'QuantitativeValue', str]], 'Distance', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The width of the item.",
    )
    hasMeasurement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="A product measurement, for example the inseam of pants, the wheel size of a bicycle, or"
     "the gauge of a screw. Usually an exact measurement, but can also be a range of measurements"
     "for adjustable products, for example belts and ski bindings.",
    )
    reviews: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="Review of the item.",
    )
    pattern: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'."
     "Values are typically expressed as text, although links to controlled value schemes"
     "are also supported.",
    )
    brand: Optional[Union[List[Union['Brand', 'Organization', str]], 'Brand', 'Organization', str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    hasMerchantReturnPolicy: Optional[Union[List[Union['MerchantReturnPolicy', str]], 'MerchantReturnPolicy', str]] = Field(
        default=None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    gtin: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin))."
     "GTINs identify trade items, including products and services, using numeric identification"
     "codes. The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/)"
     "express GTINs as URLs (URIs, IRIs, etc.). Details including regular expression examples"
     "can be found in, Section 6 of the GS1 URI Syntax specification; see also [schema.org tracking"
     "issue](https://github.com/schemaorg/schemaorg/issues/3156#issuecomment-1209522809)"
     "for schema.org-specific discussion. A correct [[gtin]] value should be a valid GTIN,"
     "which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or"
     "a \"GS1 Digital Link\" URL based on such a string. The numeric component should also have"
     "a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator)"
     "and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin)"
     "and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for"
     "more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]]"
     "property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]]"
     "properties. Note also that this is a definition for how to include GTINs in Schema.org"
     "data, and not a definition of GTINs in general - see the GS1 documentation for authoritative"
     "details.",
    )
    review: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="A review of the item.",
    )
    mpn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.",
    )
    nsn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number)"
     "(nsn) of a [[Product]].",
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
    countryOfLastProcessing: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The place where the item (typically [[Product]]) was last processed and tested before"
     "importation.",
    )
    hasEnergyConsumptionDetails: Optional[Union[List[Union['EnergyConsumptionDetails', str]], 'EnergyConsumptionDetails', str]] = Field(
        default=None,
        description="Defines the energy efficiency Category (also known as \"class\" or \"rating\") for"
     "a product according to an international energy efficiency standard.",
    )
    size: Optional[Union[List[Union[str, 'Text', 'DefinedTerm', 'SizeSpecification', 'QuantitativeValue']], str, 'Text', 'DefinedTerm', 'SizeSpecification', 'QuantitativeValue']] = Field(
        default=None,
        description="A standardized size of a product or creative work, specified either through a simple"
     "textual string (for example 'XL', '32Wx34L'), a QuantitativeValue with a unitCode,"
     "or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]],"
     "[[height]], [[depth]] and [[weight]] properties may be more applicable.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.OfferItemCondition import OfferItemCondition
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.AggregateRating import AggregateRating
    from pydantic_schemaorg.ListItem import ListItem
    from pydantic_schemaorg.WebContent import WebContent
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.ProductModel import ProductModel
    from pydantic_schemaorg.ProductGroup import ProductGroup
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
    from pydantic_schemaorg.EnergyConsumptionDetails import EnergyConsumptionDetails
    from pydantic_schemaorg.SizeSpecification import SizeSpecification
