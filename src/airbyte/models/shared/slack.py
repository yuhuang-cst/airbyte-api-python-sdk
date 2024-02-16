"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SlackCredentials:
    client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id'), 'exclude': lambda f: f is None }})
    r"""Slack client_id. See our <a href=\\"https://docs.airbyte.com/integrations/sources/slack\\">docs</a> if you need help finding this id."""
    client_secret: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret'), 'exclude': lambda f: f is None }})
    r"""Slack client_secret. See our <a href=\\"https://docs.airbyte.com/integrations/sources/slack\\">docs</a> if you need help finding this secret."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Slack:
    credentials: Optional[SlackCredentials] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    

