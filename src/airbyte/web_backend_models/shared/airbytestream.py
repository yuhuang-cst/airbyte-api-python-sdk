"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from ..shared import syncmode_enum as shared_syncmode_enum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AirbyteStream:
    r"""the immutable schema defined by the source"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""Stream's name."""
    default_cursor_field: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('defaultCursorField'), 'exclude': lambda f: f is None }})
    r"""Path to the field that will be used to determine if a record is new or modified since the last sync. If not provided by the source, the end user will have to specify the comparable themselves."""
    json_schema: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jsonSchema'), 'exclude': lambda f: f is None }})
    r"""Stream schema using Json Schema specs."""
    namespace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('namespace'), 'exclude': lambda f: f is None }})
    r"""Optional Source-defined namespace. Airbyte streams from the same sources should have the same namespace. Currently only used by JDBC destinations to determine what schema to write to."""
    source_defined_cursor: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinedCursor'), 'exclude': lambda f: f is None }})
    r"""If the source defines the cursor field, then any other cursor field inputs will be ignored. If it does not, either the user_provided one is used, or the default one is used as a backup."""
    source_defined_primary_key: Optional[list[list[str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinedPrimaryKey'), 'exclude': lambda f: f is None }})
    r"""If the source defines the primary key, paths to the fields that will be used as a primary key. If not provided by the source, the end user will have to specify the primary key themselves."""
    supported_sync_modes: Optional[list[shared_syncmode_enum.SyncModeEnum]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('supportedSyncModes'), 'exclude': lambda f: f is None }})
    