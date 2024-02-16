"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from ..shared import sourcedefinitionread as shared_sourcedefinitionread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDefinitionReadList:
    r"""Successful operation"""
    
    source_definitions: list[shared_sourcedefinitionread.SourceDefinitionRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinitions') }})
    