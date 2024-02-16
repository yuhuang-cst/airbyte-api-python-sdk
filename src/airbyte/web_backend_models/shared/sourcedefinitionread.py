"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from ..shared import actordefinitionresourcerequirements as shared_actordefinitionresourcerequirements
from ..shared import releasestage_enum as shared_releasestage_enum
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceDefinitionReadSourceTypeEnum(str, Enum):
    API = 'api'
    FILE = 'file'
    DATABASE = 'database'
    CUSTOM = 'custom'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourceDefinitionRead:
    r"""Successful operation"""
    
    docker_image_tag: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dockerImageTag') }})
    docker_repository: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dockerRepository') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    source_definition_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceDefinitionId') }})
    documentation_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('documentationUrl'), 'exclude': lambda f: f is None }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    protocol_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protocolVersion'), 'exclude': lambda f: f is None }})
    r"""The Airbyte Protocol version supported by the connector"""
    release_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('releaseDate'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The date when this connector was first released, in yyyy-mm-dd format."""
    release_stage: Optional[shared_releasestage_enum.ReleaseStageEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('releaseStage'), 'exclude': lambda f: f is None }})
    resource_requirements: Optional[shared_actordefinitionresourcerequirements.ActorDefinitionResourceRequirements] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resourceRequirements'), 'exclude': lambda f: f is None }})
    r"""actor definition specific resource requirements. if default is set, these are the requirements that should be set for ALL jobs run for this actor definition. it is overriden by the job type specific configurations. if not set, the platform will use defaults. these values will be overriden by configuration at the connection level."""
    source_type: Optional[SourceDefinitionReadSourceTypeEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    