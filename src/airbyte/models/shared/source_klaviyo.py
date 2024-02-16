"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class Klaviyo(str, Enum):
    KLAVIYO = 'klaviyo'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceKlaviyo:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Klaviyo API Key. See our <a href=\\"https://docs.airbyte.com/integrations/sources/klaviyo\\">docs</a> if you need help finding this key."""
    SOURCE_TYPE: Final[Klaviyo] = dataclasses.field(default=Klaviyo.KLAVIYO, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated. This field is optional - if not provided, all data will be replicated."""
    

