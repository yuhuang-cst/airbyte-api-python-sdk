"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import attemptinforead as shared_attemptinforead
from ..shared import jobdebugread as shared_jobdebugread
from ..shared import workflowstateread as shared_workflowstateread
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class JobDebugInfoRead:
    r"""Successful operation"""
    
    attempts: list[shared_attemptinforead.AttemptInfoRead] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attempts') }})
    job: shared_jobdebugread.JobDebugRead = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('job') }})
    workflow_state: Optional[shared_workflowstateread.WorkflowStateRead] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowState'), 'exclude': lambda f: f is None }})
    