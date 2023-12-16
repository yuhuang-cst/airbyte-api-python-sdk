"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final

class Smaily(str, Enum):
    SMAILY = 'smaily'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSmaily:
    api_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_password') }})
    r"""API user password. See https://smaily.com/help/api/general/create-api-user/"""
    api_subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_subdomain') }})
    r"""API Subdomain. See https://smaily.com/help/api/general/create-api-user/"""
    api_username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_username') }})
    r"""API user username. See https://smaily.com/help/api/general/create-api-user/"""
    SOURCE_TYPE: Final[Smaily] = dataclasses.field(default=Smaily.SMAILY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

