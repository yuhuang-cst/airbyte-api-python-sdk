"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class PaypalTransaction(str, Enum):
    PAYPAL_TRANSACTION = 'paypal-transaction'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePaypalTransaction:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your Paypal developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your Paypal developer application."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Start Date for data extraction in <a href=\\\"https://datatracker.ietf.org/doc/html/rfc3339#section-5.6\\\">ISO format</a>. Date must be in range from 3 years till 12 hrs before present time."""
    is_sandbox: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox'), 'exclude': lambda f: f is None }})
    r"""Determines whether to use the sandbox or production environment."""
    refresh_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token'), 'exclude': lambda f: f is None }})
    r"""The key to refresh the expired access token."""
    SOURCE_TYPE: Final[PaypalTransaction] = dataclasses.field(default=PaypalTransaction.PAYPAL_TRANSACTION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    time_window: Optional[int] = dataclasses.field(default=7, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('time_window'), 'exclude': lambda f: f is None }})
    r"""The number of days per request. Must be a number between 1 and 31."""
    

