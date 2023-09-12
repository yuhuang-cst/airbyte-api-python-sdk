"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Any, Optional

class DestinationSnowflakeCredentialsUsernameAndPasswordAuthType(str, Enum):
    USERNAME_AND_PASSWORD = 'Username and Password'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationSnowflakeCredentialsUsernameAndPassword:
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Enter the password associated with the username."""
    auth_type: Optional[DestinationSnowflakeCredentialsUsernameAndPasswordAuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    


class DestinationSnowflakeCredentialsKeyPairAuthenticationAuthType(str, Enum):
    KEY_PAIR_AUTHENTICATION = 'Key Pair Authentication'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationSnowflakeCredentialsKeyPairAuthentication:
    private_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key') }})
    r"""RSA Private key to use for Snowflake connection. See the <a href=\\"https://docs.airbyte.com/integrations/destinations/snowflake\\">docs</a> for more information on how to obtain this key."""
    auth_type: Optional[DestinationSnowflakeCredentialsKeyPairAuthenticationAuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    private_key_password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key_password'), 'exclude': lambda f: f is None }})
    r"""Passphrase for private key"""
    


class DestinationSnowflakeCredentialsOAuth20AuthType(str, Enum):
    O_AUTH2_0 = 'OAuth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationSnowflakeCredentialsOAuth20:
    access_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('access_token') }})
    r"""Enter you application's Access Token"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Enter your application's Refresh Token"""
    auth_type: Optional[DestinationSnowflakeCredentialsOAuth20AuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Enter your application's Client ID"""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""Enter your application's Client secret"""
    


class DestinationSnowflakeSnowflake(str, Enum):
    SNOWFLAKE = 'snowflake'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DestinationSnowflake:
    r"""The values required to configure the destination."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Enter the name of the <a href=\\"https://docs.snowflake.com/en/sql-reference/ddl-database.html#database-schema-share-ddl\\">database</a> you want to sync data into"""
    destination_type: DestinationSnowflakeSnowflake = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Enter your Snowflake account's <a href=\\"https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#using-an-account-locator-as-an-identifier\\">locator</a> (in the format <account_locator>.<region>.<cloud>.snowflakecomputing.com)"""
    role: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('role') }})
    r"""Enter the <a href=\\"https://docs.snowflake.com/en/user-guide/security-access-control-overview.html#roles\\">role</a> that you want to use to access Snowflake"""
    schema: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schema') }})
    r"""Enter the name of the default <a href=\\"https://docs.snowflake.com/en/sql-reference/ddl-database.html#database-schema-share-ddl\\">schema</a>"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Enter the name of the user you want to use to access the database"""
    warehouse: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('warehouse') }})
    r"""Enter the name of the <a href=\\"https://docs.snowflake.com/en/user-guide/warehouses-overview.html#overview-of-warehouses\\">warehouse</a> that you want to sync data into"""
    credentials: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Enter the additional properties to pass to the JDBC URL string when connecting to the database (formatted as key=value pairs separated by the symbol &). Example: key1=value1&key2=value2&key3=value3"""
    raw_data_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('raw_data_schema'), 'exclude': lambda f: f is None }})
    r"""The schema to write raw tables into"""
    

