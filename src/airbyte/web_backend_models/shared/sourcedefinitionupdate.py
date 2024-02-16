"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from ..shared import actordefinitionresourcerequirements as shared_actordefinitionresourcerequirements
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDefinitionUpdate:
    r"""Update the SourceDefinition. Currently, the only allowed attribute to update is the default docker image version."""
    
    docker_image_tag: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dockerImageTag') }})
    source_definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinitionId') }})
    resource_requirements: Optional[shared_actordefinitionresourcerequirements.ActorDefinitionResourceRequirements] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceRequirements'), 'exclude': lambda f: f is None }})
    r"""actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level."""
    