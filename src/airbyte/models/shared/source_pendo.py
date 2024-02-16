"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Pendo(str, Enum):
    PENDO = 'pendo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePendo:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    SOURCE_TYPE: Final[Pendo] = dataclasses.field(default=Pendo.PENDO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

