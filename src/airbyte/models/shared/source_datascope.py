"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Datascope(str, Enum):
    DATASCOPE = 'datascope'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDatascope:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key"""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""Start date for the data to be replicated"""
    SOURCE_TYPE: Final[Datascope] = dataclasses.field(default=Datascope.DATASCOPE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

