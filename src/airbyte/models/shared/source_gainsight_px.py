"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class GainsightPx(str, Enum):
    GAINSIGHT_PX = 'gainsight-px'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGainsightPx:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""The Aptrinsic API Key which is recieved from the dashboard settings (ref - https://app.aptrinsic.com/settings/api-keys)"""
    SOURCE_TYPE: Final[GainsightPx] = dataclasses.field(default=GainsightPx.GAINSIGHT_PX, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

