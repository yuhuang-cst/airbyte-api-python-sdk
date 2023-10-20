"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, List, Optional, Union

class SourceTypeformAuthorizationMethodPrivateTokenAuthType(str, Enum):
    ACCESS_TOKEN = 'access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTypeformAuthorizationMethodPrivateToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Log into your Typeform account and then generate a personal Access Token."""
    AUTH_TYPE: Final[Optional[SourceTypeformAuthorizationMethodPrivateTokenAuthType]] = dataclasses.field(default=SourceTypeformAuthorizationMethodPrivateTokenAuthType.ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class SourceTypeformAuthorizationMethodOAuth20AuthType(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTypeformAuthorizationMethodOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Access Token for making authenticated requests."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of the Typeform developer application."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret the Typeform developer application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""The key to refresh the expired access_token."""
    token_expiry_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token_expiry_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date-time when the access token should be refreshed."""
    AUTH_TYPE: Final[Optional[SourceTypeformAuthorizationMethodOAuth20AuthType]] = dataclasses.field(default=SourceTypeformAuthorizationMethodOAuth20AuthType.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class SourceTypeformAuthorizationMethod:
    pass

class SourceTypeformTypeform(str, Enum):
    TYPEFORM = 'typeform'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceTypeform:
    r"""The values required to configure the source."""
    credentials: Union[SourceTypeformAuthorizationMethodOAuth20, SourceTypeformAuthorizationMethodPrivateToken] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    SOURCE_TYPE: Final[SourceTypeformTypeform] = dataclasses.field(default=SourceTypeformTypeform.TYPEFORM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    form_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('form_ids'), 'exclude': lambda f: f is None }})
    r"""When this parameter is set, the connector will replicate data only from the input forms. Otherwise, all forms in your Typeform account will be replicated. You can find form IDs in your form URLs. For example, in the URL \\"https://mysite.typeform.com/to/u6nXL7\\" the form_id is u6nXL7. You can find form URLs on Share panel"""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""The date from which you'd like to replicate data for Typeform API, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    

