from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Comment(CreativeWork):
    """A comment on an item - for example, a comment on a blog post. The comment's content is expressed"
     "via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.

    See: https://schema.org/Comment
    Model depth: 3
    """
    type_: str = Field(default="Comment", alias='@type', const=True)
    parentItem: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        default=None,
        description="The parent of a question, answer or item in general.",
    )
    upvoteCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of upvotes this question, answer or comment has received from the community.",
    )
    downvoteCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of downvotes this question, answer or comment has received from the community.",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
