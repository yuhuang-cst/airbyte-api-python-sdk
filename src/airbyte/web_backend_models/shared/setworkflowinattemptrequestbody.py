"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SetWorkflowInAttemptRequestBody:
    
    attempt_number: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attemptNumber') }})
    job_id: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('jobId') }})
    workflow_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workflowId') }})
    processing_task_queue: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('processingTaskQueue'), 'exclude': lambda f: f is None }})
    