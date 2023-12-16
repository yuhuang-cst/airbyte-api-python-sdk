"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class Environment(str, Enum):
    r"""The environment to use. Either sandbox or production."""
    SANDBOX = 'sandbox'
    PRODUCTION = 'production'

class CoinAPI(str, Enum):
    COIN_API = 'coin-api'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceCoinAPI:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key"""
    period: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('period') }})
    r"""The period to use. See the documentation for a list. https://docs.coinapi.io/#list-all-periods-get"""
    start_date: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date') }})
    r"""The start date in ISO 8601 format."""
    symbol_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('symbol_id') }})
    r"""The symbol ID to use. See the documentation for a list.
    https://docs.coinapi.io/#list-all-symbols-get
    """
    SOURCE_TYPE: Final[CoinAPI] = dataclasses.field(default=CoinAPI.COIN_API, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    end_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'exclude': lambda f: f is None }})
    r"""The end date in ISO 8601 format. If not supplied, data will be returned
    from the start date to the current time, or when the count of result
    elements reaches its limit.
    """
    environment: Optional[Environment] = dataclasses.field(default=Environment.SANDBOX, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment'), 'exclude': lambda f: f is None }})
    r"""The environment to use. Either sandbox or production."""
    limit: Optional[int] = dataclasses.field(default=100, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    r"""The maximum number of elements to return. If not supplied, the default
    is 100. For numbers larger than 100, each 100 items is counted as one
    request for pricing purposes. Maximum value is 100000.
    """
    

