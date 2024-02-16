"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, Optional

class FileType(str, Enum):
    r"""The file type you want to sync. Currently only 'csv' and 'json' files are supported."""
    CSV = 'csv'
    JSON = 'json'

class SftpBulk(str, Enum):
    SFTP_BULK = 'sftp-bulk'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceSftpBulk:
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""The server host address"""
    start_date: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""The date from which you'd like to replicate data for all incremental streams, in the format YYYY-MM-DDT00:00:00Z. All data generated after this date will be replicated."""
    stream_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream_name') }})
    r"""The name of the stream or table you want to create"""
    username: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username') }})
    r"""The server user"""
    file_most_recent: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_most_recent'), 'exclude': lambda f: f is None }})
    r"""Sync only the most recent file for the configured folder path and file pattern"""
    file_pattern: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_pattern'), 'exclude': lambda f: f is None }})
    r"""The regular expression to specify files for sync in a chosen Folder Path"""
    file_type: Optional[FileType] = dataclasses.field(default=FileType.CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('file_type'), 'exclude': lambda f: f is None }})
    r"""The file type you want to sync. Currently only 'csv' and 'json' files are supported."""
    folder_path: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('folder_path'), 'exclude': lambda f: f is None }})
    r"""The directory to search files for sync"""
    password: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('password'), 'exclude': lambda f: f is None }})
    r"""OS-level password for logging into the jump server host"""
    port: Optional[int] = dataclasses.field(default=22, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""The server port"""
    private_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('private_key'), 'exclude': lambda f: f is None }})
    r"""The private key"""
    separator: Optional[str] = dataclasses.field(default=',', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('separator'), 'exclude': lambda f: f is None }})
    r"""The separator used in the CSV files. Define None if you want to use the Sniffer functionality"""
    SOURCE_TYPE: Final[SftpBulk] = dataclasses.field(default=SftpBulk.SFTP_BULK, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    

