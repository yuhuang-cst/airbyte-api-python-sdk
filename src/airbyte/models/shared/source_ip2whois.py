"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class SourceIp2whoisIp2whois(str, Enum):
    IP2WHOIS = 'ip2whois'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceIp2whois:
    r"""The values required to configure the source."""
    api_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key'), 'exclude': lambda f: f is None }})
    r"""Your API Key. See <a href=\\"https://www.ip2whois.com/developers-api\\">here</a>."""
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    r"""Domain name. See <a href=\\"https://www.ip2whois.com/developers-api\\">here</a>."""
    SOURCE_TYPE: Final[Optional[SourceIp2whoisIp2whois]] = dataclasses.field(default=SourceIp2whoisIp2whois.IP2WHOIS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    

