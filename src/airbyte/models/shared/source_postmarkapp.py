"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Postmarkapp(str, Enum):
    POSTMARKAPP = 'postmarkapp'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePostmarkapp:
    x_postmark_account_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('X-Postmark-Account-Token') }})
    r"""API Key for account"""
    x_postmark_server_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('X-Postmark-Server-Token') }})
    r"""API Key for server"""
    SOURCE_TYPE: Final[Postmarkapp] = dataclasses.field(default=Postmarkapp.POSTMARKAPP, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

