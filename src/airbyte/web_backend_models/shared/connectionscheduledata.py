"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional

class ConnectionScheduleDataBasicScheduleTimeUnitEnum(str, Enum):
    MINUTES = 'minutes'
    HOURS = 'hours'
    DAYS = 'days'
    WEEKS = 'weeks'
    MONTHS = 'months'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionScheduleDataBasicSchedule:
    
    time_unit: ConnectionScheduleDataBasicScheduleTimeUnitEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timeUnit') }})
    units: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('units') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionScheduleDataCron:
    
    cron_expression: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cronExpression') }})
    cron_time_zone: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cronTimeZone') }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ConnectionScheduleData:
    r"""schedule for when the the connection should run, per the schedule type"""
    
    basic_schedule: Optional[ConnectionScheduleDataBasicSchedule] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('basicSchedule'), 'exclude': lambda f: f is None }})
    cron: Optional[ConnectionScheduleDataCron] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cron'), 'exclude': lambda f: f is None }})
    