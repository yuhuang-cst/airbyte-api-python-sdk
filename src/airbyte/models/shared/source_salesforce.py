"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from typing import Optional

class SourceSalesforceAuthType(str, Enum):
    CLIENT = 'Client'

class SourceSalesforceSalesforce(str, Enum):
    SALESFORCE = 'salesforce'

class SourceSalesforceStreamsCriteriaSearchCriteria(str, Enum):
    STARTS_WITH = 'starts with'
    ENDS_WITH = 'ends with'
    CONTAINS = 'contains'
    EXACTS = 'exacts'
    STARTS_NOT_WITH = 'starts not with'
    ENDS_NOT_WITH = 'ends not with'
    NOT_CONTAINS = 'not contains'
    NOT_EXACTS = 'not exacts'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSalesforceStreamsCriteria:
    criteria: SourceSalesforceStreamsCriteriaSearchCriteria = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('criteria') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SourceSalesforce:
    r"""The values required to configure the source."""
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""Enter your Salesforce developer application's <a href=\\"https://developer.salesforce.com/forums/?id=9062I000000DLgbQAG\\">Client ID</a>"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""Enter your Salesforce developer application's <a href=\\"https://developer.salesforce.com/forums/?id=9062I000000DLgbQAG\\">Client secret</a>"""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Enter your application's <a href=\\"https://developer.salesforce.com/docs/atlas.en-us.mobile_sdk.meta/mobile_sdk/oauth_refresh_token_flow.htm\\">Salesforce Refresh Token</a> used for Airbyte to access your Salesforce account."""
    source_type: SourceSalesforceSalesforce = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType') }})
    auth_type: Optional[SourceSalesforceAuthType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_type'), 'exclude': lambda f: f is None }})
    force_use_bulk_api: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('force_use_bulk_api'), 'exclude': lambda f: f is None }})
    r"""Toggle to use Bulk API (this might cause empty fields for some streams)"""
    is_sandbox: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_sandbox'), 'exclude': lambda f: f is None }})
    r"""Toggle if you're using a <a href=\\"https://help.salesforce.com/s/articleView?id=sf.deploy_sandboxes_parent.htm&type=5\\">Salesforce Sandbox</a>"""
    start_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Enter the date (or date-time) in the YYYY-MM-DD or YYYY-MM-DDTHH:mm:ssZ format. Airbyte will replicate the data updated on and after this date. If this field is blank, Airbyte will replicate the data for last two years."""
    streams_criteria: Optional[list[SourceSalesforceStreamsCriteria]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('streams_criteria'), 'exclude': lambda f: f is None }})
    r"""Add filters to select only required stream based on `SObject` name. Use this field to filter which tables are displayed by this connector. This is useful if your Salesforce account has a large number of tables (>1000), in which case you may find it easier to navigate the UI and speed up the connector's performance if you restrict the tables displayed by this connector."""
    

