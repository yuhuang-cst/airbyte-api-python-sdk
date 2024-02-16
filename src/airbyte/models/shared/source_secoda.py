"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Secoda(str, Enum):
    SECODA = 'secoda'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSecoda:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Your API Access Key. See <a href=\\"https://docs.secoda.co/secoda-api/authentication\\">here</a>. The key is case sensitive."""
    SOURCE_TYPE: Final[Secoda] = dataclasses.field(default=Secoda.SECODA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

