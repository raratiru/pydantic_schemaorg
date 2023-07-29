from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.EUEnergyEfficiencyEnumeration import EUEnergyEfficiencyEnumeration


class EUEnergyEfficiencyCategoryA2Plus(EUEnergyEfficiencyEnumeration):
    """Represents EU Energy Efficiency Class A++ as defined in EU energy labeling regulations.

    See: https://schema.org/EUEnergyEfficiencyCategoryA2Plus
    Model depth: 6
    """
    type_: str = Field(default="EUEnergyEfficiencyCategoryA2Plus", alias='@type', const=True)
    
