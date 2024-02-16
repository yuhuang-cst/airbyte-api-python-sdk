"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union

class SourceAuth0SchemasCredentialsAuthenticationMethod(str, Enum):
    OAUTH2_ACCESS_TOKEN = 'oauth2_access_token'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OAuth2AccessToken:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Also called <a href=\\"https://auth0.com/docs/secure/tokens/access-tokens/get-management-api-access-tokens-for-testing\\">API Access Token </a> The access token used to call the Auth0 Management API Token. It's a JWT that contains specific grant permissions knowns as scopes."""
    AUTH_TYPE: Final[SourceAuth0SchemasCredentialsAuthenticationMethod] = dataclasses.field(default=SourceAuth0SchemasCredentialsAuthenticationMethod.OAUTH2_ACCESS_TOKEN, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    


class SourceAuth0SchemasAuthenticationMethod(str, Enum):
    OAUTH2_CONFIDENTIAL_APPLICATION = 'oauth2_confidential_application'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OAuth2ConfidentialApplication:
    audience: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('audience') }})
    r"""The audience for the token, which is your API. You can find this in the Identifier field on your  <a href=\\"https://manage.auth0.com/#/apis\\">API's settings tab</a>"""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Your application's Client ID. You can find this value on the <a href=\\"https://manage.auth0.com/#/applications\\">application's settings tab</a> after you login the admin portal."""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Your application's Client Secret. You can find this value on the <a href=\\"https://manage.auth0.com/#/applications\\">application's settings tab</a> after you login the admin portal."""
    AUTH_TYPE: Final[SourceAuth0SchemasAuthenticationMethod] = dataclasses.field(default=SourceAuth0SchemasAuthenticationMethod.OAUTH2_CONFIDENTIAL_APPLICATION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    


class Auth0(str, Enum):
    AUTH0 = 'auth0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceAuth0:
    base_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('base_url') }})
    r"""The Authentication API is served over HTTPS. All URLs referenced in the documentation have the following base `https://YOUR_DOMAIN`"""
    credentials: Union[OAuth2ConfidentialApplication, OAuth2AccessToken] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials') }})
    SOURCE_TYPE: Final[Auth0] = dataclasses.field(default=Auth0.AUTH0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[str] = dataclasses.field(default='2023-08-05T00:43:59.244Z', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00Z. Any data before this date will not be replicated."""
    

