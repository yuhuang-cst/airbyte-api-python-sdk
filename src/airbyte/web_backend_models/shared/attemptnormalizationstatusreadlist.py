"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import attemptnormalizationstatusread as shared_attemptnormalizationstatusread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AttemptNormalizationStatusReadList:
    r"""Successful operation"""
    
    attempt_normalization_statuses: Optional[list[shared_attemptnormalizationstatusread.AttemptNormalizationStatusRead]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attemptNormalizationStatuses'), 'exclude': lambda f: f is None }})
    