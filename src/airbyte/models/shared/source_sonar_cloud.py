"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Any, Final, List, Optional

class SonarCloud(str, Enum):
    SONAR_CLOUD = 'sonar-cloud'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSonarCloud:
    component_keys: List[Any] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('component_keys') }})
    r"""Comma-separated list of component keys."""
    organization: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization') }})
    r"""Organization key. See <a href=\\"https://docs.sonarcloud.io/appendices/project-information/#project-and-organization-keys\\">here</a>."""
    user_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_token') }})
    r"""Your User Token. See <a href=\\"https://docs.sonarcloud.io/advanced-setup/user-accounts/\\">here</a>. The token is case sensitive."""
    SOURCE_TYPE: Final[SonarCloud] = dataclasses.field(default=SonarCloud.SONAR_CLOUD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""To retrieve issues created before the given date (inclusive)."""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""To retrieve issues created after the given date (inclusive)."""
    

