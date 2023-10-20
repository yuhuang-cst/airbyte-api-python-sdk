"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, Optional, Union

class SourceTiktokMarketingAuthenticationMethodSandboxAccessTokenAuthType(str, Enum):
    SANDBOX_ACCESS_TOKEN = 'sandbox_access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTiktokMarketingAuthenticationMethodSandboxAccessToken:
    r"""Authentication method"""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""The long-term authorized access token."""
    advertiser_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advertiser_id') }})
    r"""The Advertiser ID which generated for the developer's Sandbox application."""
    AUTH_TYPE: Final[Optional[SourceTiktokMarketingAuthenticationMethodSandboxAccessTokenAuthType]] = dataclasses.field(default=SourceTiktokMarketingAuthenticationMethodSandboxAccessTokenAuthType.SANDBOX_ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceTiktokMarketingAuthenticationMethodOAuth20AuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTiktokMarketingAuthenticationMethodOAuth20:
    r"""Authentication method"""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Long-term Authorized Access Token."""
    app_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('app_id') }})
    r"""The Developer Application App ID."""
    secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('secret') }})
    r"""The Developer Application Secret."""
    advertiser_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('advertiser_id'), 'exclude': lambda f: f is None }})
    r"""The Advertiser ID to filter reports and streams. Let this empty to retrieve all."""
    AUTH_TYPE: Final[Optional[SourceTiktokMarketingAuthenticationMethodOAuth20AuthType]] = dataclasses.field(default=SourceTiktokMarketingAuthenticationMethodOAuth20AuthType.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class SourceTiktokMarketingAuthenticationMethod:
    pass

class SourceTiktokMarketingTiktokMarketing(str, Enum):
    TIKTOK_MARKETING = 'tiktok-marketing'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTiktokMarketing:
    r"""The values required to configure the source."""
    attribution_window: Optional[int] = dataclasses.field(default=3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribution_window'), 'exclude': lambda f: f is None }})
    r"""The attribution window in days."""
    credentials: Optional[Union[SourceTiktokMarketingAuthenticationMethodOAuth20, SourceTiktokMarketingAuthenticationMethodSandboxAccessToken]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Authentication method"""
    end_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The date until which you'd like to replicate data for all incremental streams, in the format YYYY-MM-DD. All data generated between start_date and this date will be replicated. Not setting this option will result in always syncing the data till the current date."""
    include_deleted: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('include_deleted'), 'exclude': lambda f: f is None }})
    r"""Set to active if you want to include deleted data in reports."""
    SOURCE_TYPE: Final[Optional[SourceTiktokMarketingTiktokMarketing]] = dataclasses.field(default=SourceTiktokMarketingTiktokMarketing.TIKTOK_MARKETING, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    start_date: Optional[date] = dataclasses.field(default=dateutil.parser.parse('2016-09-01').date(), metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""The Start Date in format: YYYY-MM-DD. Any data before this date will not be replicated. If this parameter is not set, all data will be replicated."""
    

