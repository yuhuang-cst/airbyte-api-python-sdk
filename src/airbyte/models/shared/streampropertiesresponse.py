"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from .streamproperties import StreamProperties
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StreamPropertiesResponse:
    r"""A list of stream properties."""
    streams: Optional[List[StreamProperties]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streams'), 'exclude': lambda f: f is None }})
    

