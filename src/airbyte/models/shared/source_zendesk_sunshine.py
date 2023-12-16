"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional, Union

class SourceZendeskSunshineSchemasAuthMethod(str, Enum):
    API_TOKEN = 'api_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskSunshineAPIToken:
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""API Token. See the <a href=\\"https://docs.airbyte.com/integrations/sources/zendesk_sunshine\\">docs</a> for information on how to generate this key."""
    email: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email') }})
    r"""The user email for your Zendesk account"""
    AUTH_METHOD: Final[Optional[SourceZendeskSunshineSchemasAuthMethod]] = dataclasses.field(default=SourceZendeskSunshineSchemasAuthMethod.API_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    


class SourceZendeskSunshineAuthMethod(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskSunshineOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Long-term access Token for making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your OAuth application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your OAuth application."""
    AUTH_METHOD: Final[Optional[SourceZendeskSunshineAuthMethod]] = dataclasses.field(default=SourceZendeskSunshineAuthMethod.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method'), 'exclude': lambda f: f is None }})
    


class SourceZendeskSunshineZendeskSunshine(str, Enum):
    ZENDESK_SUNSHINE = 'zendesk-sunshine'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceZendeskSunshine:
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate data for Zendesk Sunshine API, in the format YYYY-MM-DDT00:00:00Z."""
    subdomain: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('subdomain') }})
    r"""The subdomain for your Zendesk Account."""
    SOURCE_TYPE: Final[SourceZendeskSunshineZendeskSunshine] = dataclasses.field(default=SourceZendeskSunshineZendeskSunshine.ZENDESK_SUNSHINE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    credentials: Optional[Union[SourceZendeskSunshineOAuth20, SourceZendeskSunshineAPIToken]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    

