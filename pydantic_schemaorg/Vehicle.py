from __future__ import annotations
from typing import TYPE_CHECKING

from pydantic import AnyUrl, StrictInt, StrictFloat
from typing import List, Optional, Union
from datetime import date


from pydantic import Field
from pydantic_schemaorg.Product import Product


class Vehicle(Product):
    """A vehicle is a device that is designed or used to transport people or cargo over land, water,"
     "air, or through space.

    See: https://schema.org/Vehicle
    Model depth: 3
    """
    type_: str = Field(default="Vehicle", alias='@type', const=True)
    numberOfPreviousOwners: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of owners of the vehicle, including the current one. Typical unit code(s):"
     "C62",
    )
    vehicleConfiguration: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5"
     "MT 225 hp' or 'limited edition'.",
    )
    purchaseDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date the item, e.g. vehicle, was purchased by the current owner.",
    )
    driveWheelConfiguration: Optional[Union[List[Union[str, 'Text', 'DriveWheelConfigurationValue']], str, 'Text', 'DriveWheelConfigurationValue']] = Field(
        default=None,
        description="The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's"
     "engine via the drivetrain.",
    )
    vehicleSeatingCapacity: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of passengers that can be seated in the vehicle, both in terms of the physical"
     "space available, and in terms of limitations set by law. Typical unit code(s): C62 for"
     "persons.",
    )
    dateVehicleFirstRegistered: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date of the first registration of the vehicle with the respective public authorities.",
    )
    knownVehicleDamages: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A textual description of known damages, both repaired and unrepaired.",
    )
    vehicleTransmission: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'QualitativeValue']], AnyUrl, 'URL', str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="The type of component used for transmitting the power from a rotating power source to"
     "the wheels or other relevant component(s) (\"gearbox\" for cars).",
    )
    wheelbase: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The distance between the centers of the front and rear wheels. Typical unit code(s):"
     "CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet",
    )
    mileageFromOdometer: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The total distance travelled by the particular vehicle since its initial production,"
     "as read from its odometer. Typical unit code(s): KMT for kilometers, SMI for statute"
     "miles",
    )
    vehicleSpecialUsage: Optional[Union[List[Union[str, 'Text', 'CarUsageType']], str, 'Text', 'CarUsageType']] = Field(
        default=None,
        description="Indicates whether the vehicle has been used for special purposes, like commercial rental,"
     "driving school, or as a taxi. The legislation in many countries requires this information"
     "to be revealed when offering a car for sale.",
    )
    numberOfDoors: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of doors. Typical unit code(s): C62",
    )
    meetsEmissionStandard: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'QualitativeValue']], AnyUrl, 'URL', str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="Indicates that the vehicle meets the respective emission standard.",
    )
    cargoVolume: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The available volume for cargo or luggage. For automobiles, this is usually the trunk"
     "volume. Typical unit code(s): LTR for liters, FTQ for cubic foot/feet Note: You can use"
     "[[minValue]] and [[maxValue]] to indicate ranges.",
    )
    vehicleInteriorType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type or material of the interior of the vehicle (e.g. synthetic fabric, leather,"
     "wood, etc.). While most interior types are characterized by the material used, an interior"
     "type can also be based on vehicle usage or target audience.",
    )
    weightTotal: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The permitted total weight of the loaded vehicle, including passengers and cargo and"
     "the weight of the empty vehicle. Typical unit code(s): KGM for kilogram, LBR for pound"
     "* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]]"
     "node. * Note 2: You may also link to a [[QualitativeValue]] node that provides additional"
     "information using [[valueReference]]. * Note 3: Note that you can use [[minValue]]"
     "and [[maxValue]] to indicate ranges.",
    )
    fuelConsumption: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The amount of fuel consumed for traveling a particular distance or temporal duration"
     "with the given vehicle (e.g. liters per 100 km). * Note 1: There are unfortunately no standard"
     "unit codes for liters per 100 km. Use [[unitText]] to indicate the unit of measurement,"
     "e.g. L/100 km. * Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]]"
     "(e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are"
     "reciprocal. * Note 3: Often, the absolute value is useful only when related to driving"
     "speed (\"at 80 km/h\") or usage pattern (\"city traffic\"). You can use [[valueReference]]"
     "to link the value for the fuel consumption to another value.",
    )
    accelerationTime: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The time needed to accelerate the vehicle from a given start velocity to a given target"
     "velocity. Typical unit code(s): SEC for seconds * Note: There are unfortunately no standard"
     "unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use \"SEC\" for seconds"
     "and indicate the velocities in the [[name]] of the [[QuantitativeValue]], or use [[valueReference]]"
     "with a [[QuantitativeValue]] of 0..60 mph or 0..100 km/h to specify the reference speeds.",
    )
    productionDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date of production of the item, e.g. vehicle.",
    )
    vehicleInteriorColor: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The color or color combination of the interior of the vehicle.",
    )
    bodyType: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'QualitativeValue']], AnyUrl, 'URL', str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).",
    )
    tongueWeight: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The permitted vertical load (TWR) of a trailer attached to the vehicle. Also referred"
     "to as Tongue Load Rating (TLR) or Vertical Load Rating (VLR). Typical unit code(s): KGM"
     "for kilogram, LBR for pound * Note 1: You can indicate additional information in the [[name]]"
     "of the [[QuantitativeValue]] node. * Note 2: You may also link to a [[QualitativeValue]]"
     "node that provides additional information using [[valueReference]]. * Note 3: Note"
     "that you can use [[minValue]] and [[maxValue]] to indicate ranges.",
    )
    seatingCapacity: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of persons that can be seated (e.g. in a vehicle), both in terms of the physical"
     "space available, and in terms of limitations set by law. Typical unit code(s): C62 for"
     "persons",
    )
    speed: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The speed range of the vehicle. If the vehicle is powered by an engine, the upper limit"
     "of the speed range (indicated by [[maxValue]]) should be the maximum speed achievable"
     "under regular conditions. Typical unit code(s): KMH for km/h, HM for mile per hour (0.447"
     "04 m/s), KNT for knot *Note 1: Use [[minValue]] and [[maxValue]] to indicate the range."
     "Typically, the minimal value is zero. * Note 2: There are many different ways of measuring"
     "the speed range. You can link to information about how the given value has been determined"
     "using the [[valueReference]] property.",
    )
    numberOfAxles: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of axles. Typical unit code(s): C62",
    )
    fuelType: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'QualitativeValue']], AnyUrl, 'URL', str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only"
     "one engine, this property can be attached directly to the vehicle.",
    )
    trailerWeight: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The permitted weight of a trailer attached to the vehicle. Typical unit code(s): KGM"
     "for kilogram, LBR for pound * Note 1: You can indicate additional information in the [[name]]"
     "of the [[QuantitativeValue]] node. * Note 2: You may also link to a [[QualitativeValue]]"
     "node that provides additional information using [[valueReference]]. * Note 3: Note"
     "that you can use [[minValue]] and [[maxValue]] to indicate ranges.",
    )
    vehicleModelDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The release date of a vehicle model (often used to differentiate versions of the same"
     "make and model).",
    )
    fuelCapacity: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The capacity of the fuel tank or in the case of electric cars, the battery. If there are"
     "multiple components for storage, this should indicate the total of all storage of the"
     "same type. Typical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial"
     "gallons, AMH for ampere-hours (for electrical vehicles).",
    )
    modelDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The release date of a vehicle model (often used to differentiate versions of the same"
     "make and model).",
    )
    vehicleEngine: Optional[Union[List[Union['EngineSpecification', str]], 'EngineSpecification', str]] = Field(
        default=None,
        description="Information about the engine or engines of the vehicle.",
    )
    payload: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The permitted weight of passengers and cargo, EXCLUDING the weight of the empty vehicle."
     "Typical unit code(s): KGM for kilogram, LBR for pound * Note 1: Many databases specify"
     "the permitted TOTAL weight instead, which is the sum of [[weight]] and [[payload]] *"
     "Note 2: You can indicate additional information in the [[name]] of the [[QuantitativeValue]]"
     "node. * Note 3: You may also link to a [[QualitativeValue]] node that provides additional"
     "information using [[valueReference]]. * Note 4: Note that you can use [[minValue]]"
     "and [[maxValue]] to indicate ranges.",
    )
    vehicleIdentificationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Vehicle Identification Number (VIN) is a unique serial number used by the automotive"
     "industry to identify individual motor vehicles.",
    )
    emissionsCO2: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The CO2 emissions in g/km. When used in combination with a QuantitativeValue, put \"g/km\""
     "into the unitText property of that value, since there is no UN/CEFACT Common Code for"
     "\"g/km\".",
    )
    steeringPosition: Optional[Union[List[Union['SteeringPositionValue', str]], 'SteeringPositionValue', str]] = Field(
        default=None,
        description="The position of the steering wheel or similar device (mostly for cars).",
    )
    numberOfForwardGears: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The total number of forward gears available for the transmission system of the vehicle."
     "Typical unit code(s): C62",
    )
    fuelEfficiency: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers"
     "per liter (km/L). * Note 1: There are unfortunately no standard unit codes for miles per"
     "gallon or kilometers per liter. Use [[unitText]] to indicate the unit of measurement,"
     "e.g. mpg or km/L. * Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]]"
     "(e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are"
     "reciprocal. * Note 3: Often, the absolute value is useful only when related to driving"
     "speed (\"at 80 km/h\") or usage pattern (\"city traffic\"). You can use [[valueReference]]"
     "to link the value for the fuel economy to another value.",
    )
    callSign: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",
    )
    numberOfAirbags: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="The number or type of airbags in the vehicle.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.DriveWheelConfigurationValue import DriveWheelConfigurationValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
    from pydantic_schemaorg.CarUsageType import CarUsageType
    from pydantic_schemaorg.EngineSpecification import EngineSpecification
    from pydantic_schemaorg.SteeringPositionValue import SteeringPositionValue
