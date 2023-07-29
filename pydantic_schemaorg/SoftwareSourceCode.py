from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet"
     "samples, scripts, templates.

    See: https://schema.org/SoftwareSourceCode
    Model depth: 3
    """
    type_: str = Field(default="SoftwareSourceCode", alias='@type', const=True)
    runtime: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3,"
     ".NET Framework 3.0).",
    )
    codeSampleType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    targetProduct: Optional[Union[List[Union['SoftwareApplication', str]], 'SoftwareApplication', str]] = Field(
        default=None,
        description="Target Operating System / Product to which the code applies. If applies to several versions,"
     "just the product name can be used.",
    )
    programmingLanguage: Optional[Union[List[Union[str, 'Text', 'ComputerLanguage']], str, 'Text', 'ComputerLanguage']] = Field(
        default=None,
        description="The computer programming language.",
    )
    codeRepository: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Link to the repository where the un-compiled, human readable code and related code is"
     "located (SVN, GitHub, CodePlex).",
    )
    sampleType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    runtimePlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3,"
     ".NET Framework 3.0).",
    )
    

if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.SoftwareApplication import SoftwareApplication
    from pydantic_schemaorg.ComputerLanguage import ComputerLanguage
    from pydantic_schemaorg.URL import URL
