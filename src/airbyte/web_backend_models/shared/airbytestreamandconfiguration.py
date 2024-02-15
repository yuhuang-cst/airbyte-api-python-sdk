"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import airbytestream as shared_airbytestream
from ..shared import airbytestreamconfiguration as shared_airbytestreamconfiguration
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AirbyteStreamAndConfiguration:
    r"""each stream is split in two parts; the immutable schema from source and mutable configuration for destination"""
    
    config: Optional[shared_airbytestreamconfiguration.AirbyteStreamConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('config'), 'exclude': lambda f: f is None }})
    r"""the mutable part of the stream to configure the destination"""
    stream: Optional[shared_airbytestream.AirbyteStream] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('stream'), 'exclude': lambda f: f is None }})
    r"""the immutable schema defined by the source"""
    