"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import destinationcloneconfiguration as shared_destinationcloneconfiguration
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationCloneRequestBody:
    r"""The values required to configure the destination. The schema for this should have an id of the existing destination along with the configuration you want to change in case."""
    
    destination_clone_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationCloneId') }})
    destination_configuration: Optional[shared_destinationcloneconfiguration.DestinationCloneConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationConfiguration'), 'exclude': lambda f: f is None }})
    