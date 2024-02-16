"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from ..shared import attemptfailureorigin_enum as shared_attemptfailureorigin_enum
from ..shared import attemptfailuretype_enum as shared_attemptfailuretype_enum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AttemptFailureReason:
    
    timestamp: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('timestamp') }})
    external_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('externalMessage'), 'exclude': lambda f: f is None }})
    failure_origin: Optional[shared_attemptfailureorigin_enum.AttemptFailureOriginEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failureOrigin'), 'exclude': lambda f: f is None }})
    r"""Indicates where the error originated. If not set, the origin of error is not well known."""
    failure_type: Optional[shared_attemptfailuretype_enum.AttemptFailureTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('failureType'), 'exclude': lambda f: f is None }})
    r"""Categorizes well known errors into types for programmatic handling. If not set, the type of error is not well known."""
    internal_message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('internalMessage'), 'exclude': lambda f: f is None }})
    retryable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('retryable'), 'exclude': lambda f: f is None }})
    r"""True if it is known that retrying may succeed, e.g. for a transient failure. False if it is known that a retry will not succeed, e.g. for a configuration issue. If not set, retryable status is not well known."""
    stacktrace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stacktrace'), 'exclude': lambda f: f is None }})
    