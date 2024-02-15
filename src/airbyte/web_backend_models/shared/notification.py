"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import notificationtype_enum as shared_notificationtype_enum
from ..shared import slacknotificationconfiguration as shared_slacknotificationconfiguration
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Notification:
    
    notification_type: shared_notificationtype_enum.NotificationTypeEnum = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notificationType') }})
    send_on_failure: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sendOnFailure') }})
    send_on_success: bool = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sendOnSuccess') }})
    customerio_configuration: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customerioConfiguration'), 'exclude': lambda f: f is None }})
    slack_configuration: Optional[shared_slacknotificationconfiguration.SlackNotificationConfiguration] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slackConfiguration'), 'exclude': lambda f: f is None }})
    