"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class Insightly(str, Enum):
    INSIGHTLY = 'insightly'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceInsightly:
    start_date: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""The date from which you'd like to replicate data for Insightly in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated. Note that it will be used only for incremental streams."""
    token: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token') }})
    r"""Your Insightly API token."""
    SOURCE_TYPE: Final[Insightly] = dataclasses.field(default=Insightly.INSIGHTLY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

