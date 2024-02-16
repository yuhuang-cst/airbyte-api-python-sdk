"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional, Union

class DestinationMongodbAuthorization(str, Enum):
    LOGIN_PASSWORD = 'login/password'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LoginPassword:
    r"""Login/Password."""
    password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password') }})
    r"""Password associated with the username."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""Username to use to access the database."""
    AUTHORIZATION: Final[DestinationMongodbAuthorization] = dataclasses.field(default=DestinationMongodbAuthorization.LOGIN_PASSWORD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    


class DestinationMongodbSchemasAuthorization(str, Enum):
    NONE = 'none'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NoneT:
    r"""None."""
    AUTHORIZATION: Final[DestinationMongodbSchemasAuthorization] = dataclasses.field(default=DestinationMongodbSchemasAuthorization.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('authorization') }})
    


class Mongodb(str, Enum):
    MONGODB = 'mongodb'

class DestinationMongodbSchemasInstance(str, Enum):
    ATLAS = 'atlas'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class MongoDBAtlas:
    cluster_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cluster_url') }})
    r"""URL of a cluster to connect to."""
    instance: Optional[DestinationMongodbSchemasInstance] = dataclasses.field(default=DestinationMongodbSchemasInstance.ATLAS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance'), 'exclude': lambda f: f is None }})
    


class DestinationMongodbInstance(str, Enum):
    REPLICA = 'replica'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReplicaSet:
    server_addresses: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('server_addresses') }})
    r"""The members of a replica set. Please specify `host`:`port` of each member seperated by comma."""
    instance: Optional[DestinationMongodbInstance] = dataclasses.field(default=DestinationMongodbInstance.REPLICA, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance'), 'exclude': lambda f: f is None }})
    replica_set: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replica_set'), 'exclude': lambda f: f is None }})
    r"""A replica set name."""
    


class Instance(str, Enum):
    STANDALONE = 'standalone'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class StandaloneMongoDbInstance:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The Host of a Mongo database to be replicated."""
    instance: Optional[Instance] = dataclasses.field(default=Instance.STANDALONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance'), 'exclude': lambda f: f is None }})
    port: Optional[int] = dataclasses.field(default=27017, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The Port of a Mongo database to be replicated."""
    


class DestinationMongodbSchemasTunnelMethodTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbPasswordAuthentication:
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[DestinationMongodbSchemasTunnelMethodTunnelMethod] = dataclasses.field(default=DestinationMongodbSchemasTunnelMethodTunnelMethod.SSH_PASSWORD_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class DestinationMongodbSchemasTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbSSHKeyAuthentication:
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[DestinationMongodbSchemasTunnelMethod] = dataclasses.field(default=DestinationMongodbSchemasTunnelMethod.SSH_KEY_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class DestinationMongodbTunnelMethod(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodbNoTunnel:
    TUNNEL_METHOD: Final[DestinationMongodbTunnelMethod] = dataclasses.field(default=DestinationMongodbTunnelMethod.NO_TUNNEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationMongodb:
    auth_type: Union[NoneT, LoginPassword] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type') }})
    r"""Authorization type."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""Name of the database."""
    DESTINATION_TYPE: Final[Mongodb] = dataclasses.field(default=Mongodb.MONGODB, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    instance_type: Optional[Union[StandaloneMongoDbInstance, ReplicaSet, MongoDBAtlas]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_type'), 'exclude': lambda f: f is None }})
    r"""MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default."""
    tunnel_method: Optional[Union[DestinationMongodbNoTunnel, DestinationMongodbSSHKeyAuthentication, DestinationMongodbPasswordAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    

