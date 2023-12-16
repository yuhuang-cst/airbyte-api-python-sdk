"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional

class PolygonStockAPI(str, Enum):
    POLYGON_STOCK_API = 'polygon-stock-api'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePolygonStockAPI:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiKey') }})
    r"""Your API ACCESS Key"""
    end_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The target date for the aggregate window."""
    multiplier: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('multiplier') }})
    r"""The size of the timespan multiplier."""
    start_date: date = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(False), 'decoder': utils.datefromisoformat }})
    r"""The beginning date for the aggregate window."""
    stocks_ticker: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stocksTicker') }})
    r"""The exchange symbol that this item is traded under."""
    timespan: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timespan') }})
    r"""The size of the time window."""
    SOURCE_TYPE: Final[PolygonStockAPI] = dataclasses.field(default=PolygonStockAPI.POLYGON_STOCK_API, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    adjusted: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('adjusted'), 'exclude': lambda f: f is None }})
    r"""Determines whether or not the results are adjusted for splits. By default, results are adjusted and set to true. Set this to false to get results that are NOT adjusted for splits."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('limit'), 'exclude': lambda f: f is None }})
    r"""The target date for the aggregate window."""
    sort: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sort'), 'exclude': lambda f: f is None }})
    r"""Sort the results by timestamp. asc will return results in ascending order (oldest at the top), desc will return results in descending order (newest at the top)."""
    

