from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class LendAction(TransferAction):
    """The act of providing an object under an agreement that it will be returned at a later date."
     "Reciprocal of BorrowAction. Related actions: * [[BorrowAction]]: Reciprocal of LendAction.

    See: https://schema.org/LendAction
    Model depth: 4
    """
    type_: str = Field(default="LendAction", alias='@type', const=True)
    borrower: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A sub property of participant. The person that borrows the object being lent.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
