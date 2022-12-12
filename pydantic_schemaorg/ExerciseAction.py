from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.PlayAction import PlayAction


class ExerciseAction(PlayAction):
    """The act of participating in exertive activity for the purposes of improving health and"
     "fitness.

    See: https://schema.org/ExerciseAction
    Model depth: 4
    """

    type_: str = Field(default="ExerciseAction", alias="@type", const=True)
    toLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    course: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The course where this action was taken.",
    )
    fromLocation: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The original location of the object or the agent before the"
        "action.",
    )
    exerciseRelatedDiet: Optional[Union[List[Union["Diet", str]], "Diet", str]] = Field(
        default=None,
        description="A sub property of instrument. The diet used in this action.",
    )
    exerciseCourse: Optional[Union[List[Union["Place", str]], "Place", str]] = Field(
        default=None,
        description="A sub property of location. The course where this action was taken.",
    )
    opponent: Optional[Union[List[Union["Person", str]], "Person", str]] = Field(
        default=None,
        description="A sub property of participant. The opponent on this action.",
    )
    sportsTeam: Optional[
        Union[List[Union["SportsTeam", str]], "SportsTeam", str]
    ] = Field(
        default=None,
        description="A sub property of participant. The sports team that participated on this action.",
    )
    sportsEvent: Optional[
        Union[List[Union["SportsEvent", str]], "SportsEvent", str]
    ] = Field(
        default=None,
        description="A sub property of location. The sports event where this action occurred.",
    )
    diet: Optional[Union[List[Union["Diet", str]], "Diet", str]] = Field(
        default=None,
        description="A sub property of instrument. The diet used in this action.",
    )
    exercisePlan: Optional[
        Union[List[Union["ExercisePlan", str]], "ExercisePlan", str]
    ] = Field(
        default=None,
        description="A sub property of instrument. The exercise plan used on this action.",
    )
    exerciseType: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training,"
        "aerobics, cardiac rehabilitation, etc.",
    )
    distance: Optional[Union[List[Union["Distance", str]], "Distance", str]] = Field(
        default=None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    sportsActivityLocation: Optional[
        Union[List[Union["SportsActivityLocation", str]], "SportsActivityLocation", str]
    ] = Field(
        default=None,
        description="A sub property of location. The sports activity location where this action occurred.",
    )


if TYPE_CHECKING:
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.Diet import Diet
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.SportsTeam import SportsTeam
    from pydantic_schemaorg.SportsEvent import SportsEvent
    from pydantic_schemaorg.ExercisePlan import ExercisePlan
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
