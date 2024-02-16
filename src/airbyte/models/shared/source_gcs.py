"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from typing import Final, List, Optional, Union

class SourceGcsGcs(str, Enum):
    GCS = 'gcs'

class SourceGcsFiletype(str, Enum):
    CSV = 'csv'

class SourceGcsSchemasStreamsHeaderDefinitionType(str, Enum):
    USER_PROVIDED = 'User Provided'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGcsUserProvided:
    column_names: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('column_names') }})
    r"""The column names that will be used while emitting the CSV records"""
    HEADER_DEFINITION_TYPE: Final[Optional[SourceGcsSchemasStreamsHeaderDefinitionType]] = dataclasses.field(default=SourceGcsSchemasStreamsHeaderDefinitionType.USER_PROVIDED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    


class SourceGcsSchemasHeaderDefinitionType(str, Enum):
    AUTOGENERATED = 'Autogenerated'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGcsAutogenerated:
    HEADER_DEFINITION_TYPE: Final[Optional[SourceGcsSchemasHeaderDefinitionType]] = dataclasses.field(default=SourceGcsSchemasHeaderDefinitionType.AUTOGENERATED, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    


class SourceGcsHeaderDefinitionType(str, Enum):
    FROM_CSV = 'From CSV'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGcsFromCSV:
    HEADER_DEFINITION_TYPE: Final[Optional[SourceGcsHeaderDefinitionType]] = dataclasses.field(default=SourceGcsHeaderDefinitionType.FROM_CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition_type'), 'exclude': lambda f: f is None }})
    


class SourceGcsInferenceType(str, Enum):
    r"""How to infer the types of the columns. If none, inference default to strings."""
    NONE = 'None'
    PRIMITIVE_TYPES_ONLY = 'Primitive Types Only'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGcsCSVFormat:
    delimiter: Optional[str] = dataclasses.field(default=',', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delimiter'), 'exclude': lambda f: f is None }})
    r"""The character delimiting individual cells in the CSV data. This may only be a 1-character string. For tab-delimited data enter '\t'."""
    double_quote: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_quote'), 'exclude': lambda f: f is None }})
    r"""Whether two quotes in a quoted CSV value denote a single quote in the data."""
    encoding: Optional[str] = dataclasses.field(default='utf8', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('encoding'), 'exclude': lambda f: f is None }})
    r"""The character encoding of the CSV data. Leave blank to default to <strong>UTF8</strong>. See <a href=\\"https://docs.python.org/3/library/codecs.html#standard-encodings\\" target=\\"_blank\\">list of python encodings</a> for allowable options."""
    escape_char: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('escape_char'), 'exclude': lambda f: f is None }})
    r"""The character used for escaping special characters. To disallow escaping, leave this field blank."""
    false_values: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('false_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as false values."""
    FILETYPE: Final[Optional[SourceGcsFiletype]] = dataclasses.field(default=SourceGcsFiletype.CSV, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('filetype'), 'exclude': lambda f: f is None }})
    header_definition: Optional[Union[SourceGcsFromCSV, SourceGcsAutogenerated, SourceGcsUserProvided]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_definition'), 'exclude': lambda f: f is None }})
    r"""How headers will be defined. `User Provided` assumes the CSV does not have a header row and uses the headers provided and `Autogenerated` assumes the CSV does not have a header row and the CDK will generate headers using for `f{i}` where `i` is the index starting from 0. Else, the default behavior is to use the header from the CSV file. If a user wants to autogenerate or provide column names for a CSV having headers, they can skip rows."""
    inference_type: Optional[SourceGcsInferenceType] = dataclasses.field(default=SourceGcsInferenceType.NONE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('inference_type'), 'exclude': lambda f: f is None }})
    r"""How to infer the types of the columns. If none, inference default to strings."""
    null_values: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('null_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as null values. For example, if the value 'NA' should be interpreted as null, enter 'NA' in this field."""
    quote_char: Optional[str] = dataclasses.field(default='"', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quote_char'), 'exclude': lambda f: f is None }})
    r"""The character used for quoting CSV values. To disallow quoting, make this field blank."""
    skip_rows_after_header: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_rows_after_header'), 'exclude': lambda f: f is None }})
    r"""The number of rows to skip after the header row."""
    skip_rows_before_header: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('skip_rows_before_header'), 'exclude': lambda f: f is None }})
    r"""The number of rows to skip before the header row. For example, if the header row is on the 3rd row, enter 2 in this field."""
    strings_can_be_null: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strings_can_be_null'), 'exclude': lambda f: f is None }})
    r"""Whether strings can be interpreted as null values. If true, strings that match the null_values set will be interpreted as null. If false, strings that match the null_values set will be interpreted as the string itself."""
    true_values: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('true_values'), 'exclude': lambda f: f is None }})
    r"""A set of case-sensitive strings that should be interpreted as true values."""
    


class SourceGcsValidationPolicy(str, Enum):
    r"""The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema."""
    EMIT_RECORD = 'Emit Record'
    SKIP_RECORD = 'Skip Record'
    WAIT_FOR_DISCOVER = 'Wait for Discover'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGCSStreamConfig:
    format: Union[SourceGcsCSVFormat] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('format') }})
    r"""The configuration options that are used to alter how to read incoming files that deviate from the standard formatting."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the stream."""
    days_to_sync_if_history_is_full: Optional[int] = dataclasses.field(default=3, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('days_to_sync_if_history_is_full'), 'exclude': lambda f: f is None }})
    r"""When the state history of the file store is full, syncs will only read files that were last modified in the provided day range."""
    globs: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('globs'), 'exclude': lambda f: f is None }})
    r"""The pattern used to specify which files should be selected from the file system. For more information on glob pattern matching look <a href=\\"https://en.wikipedia.org/wiki/Glob_(programming)\\">here</a>."""
    input_schema: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('input_schema'), 'exclude': lambda f: f is None }})
    r"""The schema that will be used to validate records extracted from the file. This will override the stream schema that is auto-detected from incoming files."""
    legacy_prefix: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('legacy_prefix'), 'exclude': lambda f: f is None }})
    r"""The path prefix configured in previous versions of the GCS connector. This option is deprecated in favor of a single glob."""
    primary_key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('primary_key'), 'exclude': lambda f: f is None }})
    r"""The column or columns (for a composite key) that serves as the unique identifier of a record. If empty, the primary key will default to the parser's default primary key."""
    schemaless: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('schemaless'), 'exclude': lambda f: f is None }})
    r"""When enabled, syncs will not validate or structure records against the stream's schema."""
    validation_policy: Optional[SourceGcsValidationPolicy] = dataclasses.field(default=SourceGcsValidationPolicy.EMIT_RECORD, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('validation_policy'), 'exclude': lambda f: f is None }})
    r"""The name of the validation policy that dictates sync behavior when a record does not adhere to the stream schema."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceGcs:
    r"""NOTE: When this Spec is changed, legacy_config_transformer.py must also be
    modified to uptake the changes because it is responsible for converting
    legacy GCS configs into file based configs using the File-Based CDK.
    """
    bucket: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('bucket') }})
    r"""Name of the GCS bucket where the file(s) exist."""
    service_account: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('service_account') }})
    r"""Enter your Google Cloud <a href=\\"https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys\\">service account key</a> in JSON format"""
    streams: List[SourceGCSStreamConfig] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streams') }})
    r"""Each instance of this configuration defines a <a href=https://docs.airbyte.com/cloud/core-concepts#stream>stream</a>. Use this to define which files belong in the stream, their format, and how they should be parsed and validated. When sending data to warehouse destination such as Snowflake or BigQuery, each stream is a separate table."""
    SOURCE_TYPE: Final[SourceGcsGcs] = dataclasses.field(default=SourceGcsGcs.GCS, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'exclude': lambda f: f is None }})
    r"""UTC date and time in the format 2017-01-25T00:00:00.000000Z. Any file modified before this date will not be replicated."""
    

