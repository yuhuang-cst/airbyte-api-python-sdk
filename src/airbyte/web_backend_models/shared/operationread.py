"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from ..shared import operatorconfiguration as shared_operatorconfiguration
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OperationRead:
    r"""Successful operation"""
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    operation_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operationId') }})
    operator_configuration: shared_operatorconfiguration.OperatorConfiguration = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('operatorConfiguration') }})
    workspace_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspaceId') }})
    