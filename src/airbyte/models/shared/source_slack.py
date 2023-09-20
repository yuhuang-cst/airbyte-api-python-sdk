"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Any, Optional

class SourceSlackCredentialsAPITokenOptionTitle(str, Enum):
    API_TOKEN_CREDENTIALS = 'API Token Credentials'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSlackCredentialsAPIToken:
    r"""Choose how to authenticate into Slack"""
    api_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_token') }})
    r"""A Slack bot token. See the <a href=\\"https://docs.airbyte.com/integrations/sources/slack\\">docs</a> for instructions on how to generate it."""
    option_title: SourceSlackCredentialsAPITokenOptionTitle = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title') }})
    


class SourceSlackCredentialsSignInViaSlackOAuthOptionTitle(str, Enum):
    DEFAULT_O_AUTH2_0_AUTHORIZATION = 'Default OAuth2.0 authorization'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSlackCredentialsSignInViaSlackOAuth:
    r"""Choose how to authenticate into Slack"""
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Slack access_token. See our <a href=\\"https://docs.airbyte.com/integrations/sources/slack\\">docs</a> if you need help generating the token."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Slack client_id. See our <a href=\\"https://docs.airbyte.com/integrations/sources/slack\\">docs</a> if you need help finding this id."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Slack client_secret. See our <a href=\\"https://docs.airbyte.com/integrations/sources/slack\\">docs</a> if you need help finding this secret."""
    option_title: SourceSlackCredentialsSignInViaSlackOAuthOptionTitle = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('option_title') }})
    


class SourceSlackSlack(str, Enum):
    SLACK = 'slack'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSlack:
    r"""The values required to configure the source."""
    source_type: SourceSlackSlack = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    channel_filter: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('channel_filter'), 'exclude': lambda f: f is None }})
    r"""A channel name list (without leading '#' char) which limit the channels from which you'd like to sync. Empty list means no filter."""
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    r"""Choose how to authenticate into Slack"""
    join_channels: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('join_channels'), 'exclude': lambda f: f is None }})
    r"""Whether to join all channels or to sync data only from channels the bot is already in.  If false, you'll need to manually add the bot to all the channels from which you'd like to sync messages."""
    lookback_window: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lookback_window'), 'exclude': lambda f: f is None }})
    r"""How far into the past to look for messages in threads, default is 0 days"""
    

