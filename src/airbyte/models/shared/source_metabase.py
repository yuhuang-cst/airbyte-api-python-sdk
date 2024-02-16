"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class Metabase(str, Enum):
    METABASE = 'metabase'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMetabase:
    instance_api_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_api_url') }})
    r"""URL to your metabase instance API"""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    session_token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('session_token'), 'exclude': lambda f: f is None }})
    r"""To generate your session token, you need to run the following command: ``` curl -X POST \ 
      -H \"Content-Type: application/json\" \
      -d '{\"username\": \"person@metabase.com\", \"password\": \"fakepassword\"}' \
      http://localhost:3000/api/session
    ``` Then copy the value of the `id` field returned by a successful call to that API.
    Note that by default, sessions are good for 14 days and needs to be regenerated.
    """
    SOURCE_TYPE: Final[Metabase] = dataclasses.field(default=Metabase.METABASE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    

