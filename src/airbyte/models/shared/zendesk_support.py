"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ZendeskSupportCredentials:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""The OAuth client's ID. See <a href=\\"https://docs.searchunify.com/Content/Content-Sources/Zendesk-Authentication-OAuth-Client-ID-Secret.htm#:~:text=Get%20Client%20ID%20and%20Client%20Secret&text=Go%20to%20OAuth%20Clients%20and,will%20be%20displayed%20only%20once.\\">this guide</a> for more information."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""The OAuth client secret. See <a href=\\"https://docs.searchunify.com/Content/Content-Sources/Zendesk-Authentication-OAuth-Client-ID-Secret.htm#:~:text=Get%20Client%20ID%20and%20Client%20Secret&text=Go%20to%20OAuth%20Clients%20and,will%20be%20displayed%20only%20once.\\">this guide</a> for more information."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ZendeskSupport:
    r"""The values required to configure the source."""
    credentials: Optional[ZendeskSupportCredentials] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    

