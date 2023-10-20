"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Final, Optional

class DestinationTypesenseTypesense(str, Enum):
    TYPESENSE = 'typesense'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DestinationTypesense:
    r"""The values required to configure the destination."""
    api_key: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('api_key') }})
    r"""Typesense API Key"""
    host: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('host') }})
    r"""Hostname of the Typesense instance without protocol."""
    DESTINATION_TYPE: Final[DestinationTypesenseTypesense] = dataclasses.field(default=DestinationTypesenseTypesense.TYPESENSE, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('destinationType') }})
    batch_size: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('batch_size'), 'exclude': lambda f: f is None }})
    r"""How many documents should be imported together. Default 1000"""
    port: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('port'), 'exclude': lambda f: f is None }})
    r"""Port of the Typesense instance. Ex: 8108, 80, 443. Default is 443"""
    protocol: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('protocol'), 'exclude': lambda f: f is None }})
    r"""Protocol of the Typesense instance. Ex: http or https. Default is https"""
    

