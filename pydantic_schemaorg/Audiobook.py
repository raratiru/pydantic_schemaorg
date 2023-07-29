from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.AudioObject import AudioObject
from pydantic_schemaorg.Book import Book


class Audiobook(AudioObject, Book):
    """An audiobook.

    See: https://schema.org/Audiobook
    Model depth: 4
    """
    type_: str = Field(default="Audiobook", alias='@type', const=True)
    readBy: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person who reads (performs) the audiobook.",
    )
    duration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Duration import Duration
