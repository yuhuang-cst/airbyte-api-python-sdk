"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Emailoctopus(str, Enum):
    EMAILOCTOPUS = 'emailoctopus'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceEmailoctopus:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""EmailOctopus API Key. See the <a href=\\"https://help.emailoctopus.com/article/165-how-to-create-and-delete-api-keys\\">docs</a> for information on how to generate this key."""
    SOURCE_TYPE: Final[Emailoctopus] = dataclasses.field(default=Emailoctopus.EMAILOCTOPUS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

