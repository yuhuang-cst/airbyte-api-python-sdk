"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class ZendeskSell(str, Enum):
    ZENDESK_SELL = 'zendesk-sell'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskSell:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""The API token for authenticating to Zendesk Sell"""
    SOURCE_TYPE: Final[ZendeskSell] = dataclasses.field(default=ZendeskSell.ZENDESK_SELL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

