"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class Posthog(str, Enum):
    POSTHOG = 'posthog'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePosthog:
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""API Key. See the <a href=\\"https://docs.airbyte.com/integrations/sources/posthog\\">docs</a> for information on how to generate this key."""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate the data. Any data before this date will not be replicated."""
    base_url: Optional[str] = dataclasses.field(default='https://app.posthog.com', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url'), 'exclude': lambda f: f is None }})
    r"""Base PostHog url. Defaults to PostHog Cloud (https://app.posthog.com)."""
    events_time_step: Optional[int] = dataclasses.field(default=30, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('events_time_step'), 'exclude': lambda f: f is None }})
    r"""Set lower value in case of failing long running sync of events stream."""
    SOURCE_TYPE: Final[Posthog] = dataclasses.field(default=Posthog.POSTHOG, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

