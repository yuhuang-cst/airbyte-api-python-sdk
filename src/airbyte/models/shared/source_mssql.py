"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, List, Optional, Union

class SourceMssqlUpdateMethodScanChangesWithUserDefinedCursorMethod(str, Enum):
    STANDARD = 'STANDARD'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlUpdateMethodScanChangesWithUserDefinedCursor:
    r"""Incrementally detects new inserts and updates using the <a href=\\"https://docs.airbyte.com/understanding-airbyte/connections/incremental-append/#user-defined-cursor\\">cursor column</a> chosen when configuring a connection (e.g. created_at, updated_at)."""
    METHOD: Final[SourceMssqlUpdateMethodScanChangesWithUserDefinedCursorMethod] = dataclasses.field(default=SourceMssqlUpdateMethodScanChangesWithUserDefinedCursorMethod.STANDARD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    


class SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCDataToSync(str, Enum):
    r"""What data should be synced under the CDC. \\"Existing and New\\" will read existing data as a snapshot, and sync new changes through CDC. \\"New Changes Only\\" will skip the initial snapshot, and only sync new changes through CDC."""
    EXISTING_AND_NEW = 'Existing and New'
    NEW_CHANGES_ONLY = 'New Changes Only'

class SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCMethod(str, Enum):
    CDC = 'CDC'

class SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCInitialSnapshotIsolationLevel(str, Enum):
    r"""Existing data in the database are synced through an initial snapshot. This parameter controls the isolation level that will be used during the initial snapshotting. If you choose the \\"Snapshot\\" level, you must enable the <a href=\\"https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/snapshot-isolation-in-sql-server\\">snapshot isolation mode</a> on the database."""
    SNAPSHOT = 'Snapshot'
    READ_COMMITTED = 'Read Committed'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDC:
    r"""<i>Recommended</i> - Incrementally reads new inserts, updates, and deletes using the SQL Server's <a href=\\"https://docs.airbyte.com/integrations/sources/mssql/#change-data-capture-cdc\\">change data capture feature</a>. This must be enabled on your database."""
    METHOD: Final[SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCMethod] = dataclasses.field(default=SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCMethod.CDC, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('method') }})
    data_to_sync: Optional[SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCDataToSync] = dataclasses.field(default=SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCDataToSync.EXISTING_AND_NEW, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data_to_sync'), 'exclude': lambda f: f is None }})
    r"""What data should be synced under the CDC. \\"Existing and New\\" will read existing data as a snapshot, and sync new changes through CDC. \\"New Changes Only\\" will skip the initial snapshot, and only sync new changes through CDC."""
    initial_waiting_seconds: Optional[int] = dataclasses.field(default=300, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initial_waiting_seconds'), 'exclude': lambda f: f is None }})
    r"""The amount of time the connector will wait when it launches to determine if there is new data to sync or not. Defaults to 300 seconds. Valid range: 120 seconds to 1200 seconds. Read about <a href=\\"https://docs.airbyte.com/integrations/sources/mysql/#change-data-capture-cdc\\">initial waiting time</a>."""
    snapshot_isolation: Optional[SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCInitialSnapshotIsolationLevel] = dataclasses.field(default=SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDCInitialSnapshotIsolationLevel.SNAPSHOT, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('snapshot_isolation'), 'exclude': lambda f: f is None }})
    r"""Existing data in the database are synced through an initial snapshot. This parameter controls the isolation level that will be used during the initial snapshotting. If you choose the \\"Snapshot\\" level, you must enable the <a href=\\"https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/snapshot-isolation-in-sql-server\\">snapshot isolation mode</a> on the database."""
    



@dataclasses.dataclass
class SourceMssqlUpdateMethod:
    pass

class SourceMssqlMssql(str, Enum):
    MSSQL = 'mssql'

class SourceMssqlSSLMethodEncryptedVerifyCertificateSSLMethod(str, Enum):
    ENCRYPTED_VERIFY_CERTIFICATE = 'encrypted_verify_certificate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlSSLMethodEncryptedVerifyCertificate:
    r"""Verify and use the certificate provided by the server."""
    SSL_METHOD: Final[SourceMssqlSSLMethodEncryptedVerifyCertificateSSLMethod] = dataclasses.field(default=SourceMssqlSSLMethodEncryptedVerifyCertificateSSLMethod.ENCRYPTED_VERIFY_CERTIFICATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    host_name_in_certificate: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostNameInCertificate'), 'exclude': lambda f: f is None }})
    r"""Specifies the host name of the server. The value of this property must match the subject property of the certificate."""
    


class SourceMssqlSSLMethodEncryptedTrustServerCertificateSSLMethod(str, Enum):
    ENCRYPTED_TRUST_SERVER_CERTIFICATE = 'encrypted_trust_server_certificate'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlSSLMethodEncryptedTrustServerCertificate:
    r"""Use the certificate provided by the server without verification. (For testing purposes only!)"""
    SSL_METHOD: Final[SourceMssqlSSLMethodEncryptedTrustServerCertificateSSLMethod] = dataclasses.field(default=SourceMssqlSSLMethodEncryptedTrustServerCertificateSSLMethod.ENCRYPTED_TRUST_SERVER_CERTIFICATE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method') }})
    



@dataclasses.dataclass
class SourceMssqlSSLMethod:
    pass

class SourceMssqlSSHTunnelMethodPasswordAuthenticationTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and password authentication"""
    SSH_PASSWORD_AUTH = 'SSH_PASSWORD_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlSSHTunnelMethodPasswordAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host"""
    tunnel_user_password: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user_password') }})
    r"""OS-level password for logging into the jump server host"""
    TUNNEL_METHOD: Final[SourceMssqlSSHTunnelMethodPasswordAuthenticationTunnelMethod] = dataclasses.field(default=SourceMssqlSSHTunnelMethodPasswordAuthenticationTunnelMethod.SSH_PASSWORD_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and password authentication"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class SourceMssqlSSHTunnelMethodSSHKeyAuthenticationTunnelMethod(str, Enum):
    r"""Connect through a jump server tunnel host using username and ssh key"""
    SSH_KEY_AUTH = 'SSH_KEY_AUTH'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlSSHTunnelMethodSSHKeyAuthentication:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    ssh_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssh_key') }})
    r"""OS-level user account ssh key credentials in RSA PEM format ( created with ssh-keygen -t rsa -m PEM -f myuser_rsa )"""
    tunnel_host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_host') }})
    r"""Hostname of the jump server host that allows inbound ssh tunnel."""
    tunnel_user: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_user') }})
    r"""OS-level username for logging into the jump server host."""
    TUNNEL_METHOD: Final[SourceMssqlSSHTunnelMethodSSHKeyAuthenticationTunnelMethod] = dataclasses.field(default=SourceMssqlSSHTunnelMethodSSHKeyAuthenticationTunnelMethod.SSH_KEY_AUTH, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""Connect through a jump server tunnel host using username and ssh key"""
    tunnel_port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_port'), 'exclude': lambda f: f is None }})
    r"""Port on the proxy/jump server that accepts inbound ssh connections."""
    


class SourceMssqlSSHTunnelMethodNoTunnelTunnelMethod(str, Enum):
    r"""No ssh tunnel needed to connect to database"""
    NO_TUNNEL = 'NO_TUNNEL'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssqlSSHTunnelMethodNoTunnel:
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    TUNNEL_METHOD: Final[SourceMssqlSSHTunnelMethodNoTunnelTunnelMethod] = dataclasses.field(default=SourceMssqlSSHTunnelMethodNoTunnelTunnelMethod.NO_TUNNEL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method') }})
    r"""No ssh tunnel needed to connect to database"""
    



@dataclasses.dataclass
class SourceMssqlSSHTunnelMethod:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceMssql:
    r"""The values required to configure the source."""
    database: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('database') }})
    r"""The name of the database."""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The hostname of the database."""
    port: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port') }})
    r"""The port of the database."""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""The username which is used to access the database."""
    SOURCE_TYPE: Final[SourceMssqlMssql] = dataclasses.field(default=SourceMssqlMssql.MSSQL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    jdbc_url_params: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jdbc_url_params'), 'exclude': lambda f: f is None }})
    r"""Additional properties to pass to the JDBC URL string when connecting to the database formatted as 'key=value' pairs separated by the symbol '&'. (example: key1=value1&key2=value2&key3=value3)."""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""The password associated with the username."""
    replication_method: Optional[Union[SourceMssqlUpdateMethodReadChangesUsingChangeDataCaptureCDC, SourceMssqlUpdateMethodScanChangesWithUserDefinedCursor]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('replication_method'), 'exclude': lambda f: f is None }})
    r"""Configures how data is extracted from the database."""
    schemas: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemas'), 'exclude': lambda f: f is None }})
    r"""The list of schemas to sync from. Defaults to user. Case sensitive."""
    ssl_method: Optional[Union[SourceMssqlSSLMethodEncryptedTrustServerCertificate, SourceMssqlSSLMethodEncryptedVerifyCertificate]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ssl_method'), 'exclude': lambda f: f is None }})
    r"""The encryption method which is used when communicating with the database."""
    tunnel_method: Optional[Union[SourceMssqlSSHTunnelMethodNoTunnel, SourceMssqlSSHTunnelMethodSSHKeyAuthentication, SourceMssqlSSHTunnelMethodPasswordAuthentication]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tunnel_method'), 'exclude': lambda f: f is None }})
    r"""Whether to initiate an SSH tunnel before connecting to the database, and if so, which kind of authentication to use."""
    

