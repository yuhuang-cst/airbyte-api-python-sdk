"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum

class SourceBrazeBraze(str, Enum):
    BRAZE = 'braze'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceBraze:
    r"""The values required to configure the source."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Braze REST API key"""
    source_type: SourceBrazeBraze = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""Rows after this date will be synced"""
    url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url') }})
    r"""Braze REST API endpoint"""
    

