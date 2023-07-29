from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime
from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Dataset(CreativeWork):
    """A body of structured information describing some topic(s) of interest.

    See: https://schema.org/Dataset
    Model depth: 3
    """
    type_: str = Field(default="Dataset", alias='@type', const=True)
    datasetTimeInterval: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the"
     "year 2011 (in ISO 8601 time interval format).",
    )
    includedDataCatalog: Optional[Union[List[Union['DataCatalog', str]], 'DataCatalog', str]] = Field(
        default=None,
        description="A data catalog which contains this dataset (this property was previously 'catalog',"
     "preferred name is now 'includedInDataCatalog').",
    )
    variableMeasured: Optional[Union[List[Union[str, 'Text', 'PropertyValue', 'StatisticalVariable', 'Property']], str, 'Text', 'PropertyValue', 'StatisticalVariable', 'Property']] = Field(
        default=None,
        description="The variableMeasured property can indicate (repeated as necessary) the variables"
     "that are measured in some dataset, either described as text or as pairs of identifier"
     "and description using PropertyValue, or more explicitly as a [[StatisticalVariable]].",
    )
    measurementTechnique: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']] = Field(
        default=None,
        description="A technique, method or technology used in an [[Observation]], [[StatisticalVariable]]"
     "or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method"
     "used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]];"
     "for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each"
     "[[variableMeasured]] will have an explicit representation as (or mapping to) an property"
     "such as those defined in Schema.org, or other RDF vocabularies and \"knowledge graphs\"."
     "In that case the subproperty of [[variableMeasured]] called [[measuredProperty]]"
     "is applicable. The [[measurementTechnique]] property helps when extra clarification"
     "is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific"
     "and scholarly dataset publication but may have broader applicability; it is not intended"
     "as a full representation of measurement, but can often serve as a high level summary for"
     "dataset discovery. For example, if [[variableMeasured]] is: molecule concentration,"
     "[[measurementTechnique]] could be: \"mass spectrometry\" or \"nmr spectroscopy\""
     "or \"colorimetry\" or \"immunofluorescence\". If the [[variableMeasured]] is \"depression"
     "rating\", the [[measurementTechnique]] could be \"Zung Scale\" or \"HAM-D\" or \"Beck"
     "Depression Inventory\". If there are several [[variableMeasured]] properties recorded"
     "for some given data object, use a [[PropertyValue]] for each [[variableMeasured]]"
     "and attach the corresponding [[measurementTechnique]]. The value can also be from"
     "an enumeration, organized as a [[MeasurementMetholdEnumeration]].",
    )
    catalog: Optional[Union[List[Union['DataCatalog', str]], 'DataCatalog', str]] = Field(
        default=None,
        description="A data catalog which contains this dataset.",
    )
    issn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    measurementMethod: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']] = Field(
        default=None,
        description="A subproperty of [[measurementTechnique]] that can be used for specifying specific"
     "methods, in particular via [[MeasurementMethodEnum]].",
    )
    distribution: Optional[Union[List[Union['DataDownload', str]], 'DataDownload', str]] = Field(
        default=None,
        description="A downloadable form of this dataset, at a specific location, in a specific format. This"
     "property can be repeated if different variations are available. There is no expectation"
     "that different downloadable distributions must contain exactly equivalent information"
     "(see also [DCAT](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution) on"
     "this point). Different distributions might include or exclude different subsets of"
     "the entire dataset, for example.",
    )
    includedInDataCatalog: Optional[Union[List[Union['DataCatalog', str]], 'DataCatalog', str]] = Field(
        default=None,
        description="A data catalog which contains this dataset.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.DataCatalog import DataCatalog
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PropertyValue import PropertyValue
    from pydantic_schemaorg.StatisticalVariable import StatisticalVariable
    from pydantic_schemaorg.Property import Property
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.MeasurementMethodEnum import MeasurementMethodEnum
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.DataDownload import DataDownload
