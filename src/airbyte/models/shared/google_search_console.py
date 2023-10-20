"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GoogleSearchConsoleAuthorization:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The client ID of your Google Search Console developer application. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The client secret of your Google Search Console developer application. Read more <a href=\\"https://developers.google.com/webmaster-tools/v1/how-tos/authorizing\\">here</a>."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GoogleSearchConsole:
    r"""The values required to configure the source."""
    authorization: Optional[GoogleSearchConsoleAuthorization] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization'), 'exclude': lambda f: f is None }})
    

