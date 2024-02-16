"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final

class Recharge(str, Enum):
    RECHARGE = 'recharge'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceRecharge:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The value of the Access Token generated. See the <a href=\\"https://docs.airbyte.com/integrations/sources/recharge\\">docs</a> for more information."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate data for Recharge API, in the format YYYY-MM-DDT00:00:00Z. Any data before this date will not be replicated."""
    SOURCE_TYPE: Final[Recharge] = dataclasses.field(default=Recharge.RECHARGE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

