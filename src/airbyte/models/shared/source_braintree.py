"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class SourceBraintreeEnvironment(str, Enum):
    r"""Environment specifies where the data will come from."""
    DEVELOPMENT = 'Development'
    SANDBOX = 'Sandbox'
    QA = 'Qa'
    PRODUCTION = 'Production'

class SourceBraintreeBraintree(str, Enum):
    BRAINTREE = 'braintree'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceBraintree:
    r"""The values required to configure the source."""
    environment: SourceBraintreeEnvironment = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('environment') }})
    r"""Environment specifies where the data will come from."""
    merchant_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('merchant_id') }})
    r"""The unique identifier for your entire gateway account. See the <a href=\\"https://docs.airbyte.com/integrations/sources/braintree\\">docs</a> for more information on how to obtain this ID."""
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key') }})
    r"""Braintree Private Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/braintree\\">docs</a> for more information on how to obtain this key."""
    public_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public_key') }})
    r"""Braintree Public Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/braintree\\">docs</a> for more information on how to obtain this key."""
    SOURCE_TYPE: Final[SourceBraintreeBraintree] = dataclasses.field(default=SourceBraintreeBraintree.BRAINTREE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    

