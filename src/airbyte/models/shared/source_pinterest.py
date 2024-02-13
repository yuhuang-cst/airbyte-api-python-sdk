"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from airbyte import utils
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from typing import Final, List, Optional

class SourcePinterestAuthMethod(str, Enum):
    OAUTH2_0 = 'oauth2.0'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OAuth20:
    client_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_id') }})
    r"""The Client ID of your OAuth application"""
    client_secret: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('client_secret') }})
    r"""The Client Secret of your OAuth application."""
    refresh_token: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('refresh_token') }})
    r"""Refresh Token to obtain new Access Token, when it's expired."""
    AUTH_METHOD: Final[SourcePinterestAuthMethod] = dataclasses.field(default=SourcePinterestAuthMethod.OAUTH2_0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('auth_method') }})
    


class SourcePinterestValidEnums(str, Enum):
    r"""An enumeration."""
    INDIVIDUAL = 'INDIVIDUAL'
    HOUSEHOLD = 'HOUSEHOLD'

class ClickWindowDays(int, Enum):
    r"""Number of days to use as the conversion attribution window for a pin click action."""
    ZERO = 0
    ONE = 1
    SEVEN = 7
    FOURTEEN = 14
    THIRTY = 30
    SIXTY = 60

class SourcePinterestSchemasValidEnums(str, Enum):
    r"""An enumeration."""
    ADVERTISER_ID = 'ADVERTISER_ID'
    AD_ACCOUNT_ID = 'AD_ACCOUNT_ID'
    AD_GROUP_ENTITY_STATUS = 'AD_GROUP_ENTITY_STATUS'
    AD_GROUP_ID = 'AD_GROUP_ID'
    AD_ID = 'AD_ID'
    CAMPAIGN_DAILY_SPEND_CAP = 'CAMPAIGN_DAILY_SPEND_CAP'
    CAMPAIGN_ENTITY_STATUS = 'CAMPAIGN_ENTITY_STATUS'
    CAMPAIGN_ID = 'CAMPAIGN_ID'
    CAMPAIGN_LIFETIME_SPEND_CAP = 'CAMPAIGN_LIFETIME_SPEND_CAP'
    CAMPAIGN_NAME = 'CAMPAIGN_NAME'
    CHECKOUT_ROAS = 'CHECKOUT_ROAS'
    CLICKTHROUGH_1 = 'CLICKTHROUGH_1'
    CLICKTHROUGH_1_GROSS = 'CLICKTHROUGH_1_GROSS'
    CLICKTHROUGH_2 = 'CLICKTHROUGH_2'
    CPC_IN_MICRO_DOLLAR = 'CPC_IN_MICRO_DOLLAR'
    CPM_IN_DOLLAR = 'CPM_IN_DOLLAR'
    CPM_IN_MICRO_DOLLAR = 'CPM_IN_MICRO_DOLLAR'
    CTR = 'CTR'
    CTR_2 = 'CTR_2'
    ECPCV_IN_DOLLAR = 'ECPCV_IN_DOLLAR'
    ECPCV_P95_IN_DOLLAR = 'ECPCV_P95_IN_DOLLAR'
    ECPC_IN_DOLLAR = 'ECPC_IN_DOLLAR'
    ECPC_IN_MICRO_DOLLAR = 'ECPC_IN_MICRO_DOLLAR'
    ECPE_IN_DOLLAR = 'ECPE_IN_DOLLAR'
    ECPM_IN_MICRO_DOLLAR = 'ECPM_IN_MICRO_DOLLAR'
    ECPV_IN_DOLLAR = 'ECPV_IN_DOLLAR'
    ECTR = 'ECTR'
    EENGAGEMENT_RATE = 'EENGAGEMENT_RATE'
    ENGAGEMENT_1 = 'ENGAGEMENT_1'
    ENGAGEMENT_2 = 'ENGAGEMENT_2'
    ENGAGEMENT_RATE = 'ENGAGEMENT_RATE'
    IDEA_PIN_PRODUCT_TAG_VISIT_1 = 'IDEA_PIN_PRODUCT_TAG_VISIT_1'
    IDEA_PIN_PRODUCT_TAG_VISIT_2 = 'IDEA_PIN_PRODUCT_TAG_VISIT_2'
    IMPRESSION_1 = 'IMPRESSION_1'
    IMPRESSION_1_GROSS = 'IMPRESSION_1_GROSS'
    IMPRESSION_2 = 'IMPRESSION_2'
    INAPP_CHECKOUT_COST_PER_ACTION = 'INAPP_CHECKOUT_COST_PER_ACTION'
    OUTBOUND_CLICK_1 = 'OUTBOUND_CLICK_1'
    OUTBOUND_CLICK_2 = 'OUTBOUND_CLICK_2'
    PAGE_VISIT_COST_PER_ACTION = 'PAGE_VISIT_COST_PER_ACTION'
    PAGE_VISIT_ROAS = 'PAGE_VISIT_ROAS'
    PAID_IMPRESSION = 'PAID_IMPRESSION'
    PIN_ID = 'PIN_ID'
    PIN_PROMOTION_ID = 'PIN_PROMOTION_ID'
    REPIN_1 = 'REPIN_1'
    REPIN_2 = 'REPIN_2'
    REPIN_RATE = 'REPIN_RATE'
    SPEND_IN_DOLLAR = 'SPEND_IN_DOLLAR'
    SPEND_IN_MICRO_DOLLAR = 'SPEND_IN_MICRO_DOLLAR'
    TOTAL_CHECKOUT = 'TOTAL_CHECKOUT'
    TOTAL_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    TOTAL_CLICKTHROUGH = 'TOTAL_CLICKTHROUGH'
    TOTAL_CLICK_ADD_TO_CART = 'TOTAL_CLICK_ADD_TO_CART'
    TOTAL_CLICK_CHECKOUT = 'TOTAL_CLICK_CHECKOUT'
    TOTAL_CLICK_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_CLICK_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    TOTAL_CLICK_LEAD = 'TOTAL_CLICK_LEAD'
    TOTAL_CLICK_SIGNUP = 'TOTAL_CLICK_SIGNUP'
    TOTAL_CLICK_SIGNUP_VALUE_IN_MICRO_DOLLAR = 'TOTAL_CLICK_SIGNUP_VALUE_IN_MICRO_DOLLAR'
    TOTAL_CONVERSIONS = 'TOTAL_CONVERSIONS'
    TOTAL_CUSTOM = 'TOTAL_CUSTOM'
    TOTAL_ENGAGEMENT = 'TOTAL_ENGAGEMENT'
    TOTAL_ENGAGEMENT_CHECKOUT = 'TOTAL_ENGAGEMENT_CHECKOUT'
    TOTAL_ENGAGEMENT_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_ENGAGEMENT_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    TOTAL_ENGAGEMENT_LEAD = 'TOTAL_ENGAGEMENT_LEAD'
    TOTAL_ENGAGEMENT_SIGNUP = 'TOTAL_ENGAGEMENT_SIGNUP'
    TOTAL_ENGAGEMENT_SIGNUP_VALUE_IN_MICRO_DOLLAR = 'TOTAL_ENGAGEMENT_SIGNUP_VALUE_IN_MICRO_DOLLAR'
    TOTAL_IDEA_PIN_PRODUCT_TAG_VISIT = 'TOTAL_IDEA_PIN_PRODUCT_TAG_VISIT'
    TOTAL_IMPRESSION_FREQUENCY = 'TOTAL_IMPRESSION_FREQUENCY'
    TOTAL_IMPRESSION_USER = 'TOTAL_IMPRESSION_USER'
    TOTAL_LEAD = 'TOTAL_LEAD'
    TOTAL_OFFLINE_CHECKOUT = 'TOTAL_OFFLINE_CHECKOUT'
    TOTAL_PAGE_VISIT = 'TOTAL_PAGE_VISIT'
    TOTAL_REPIN_RATE = 'TOTAL_REPIN_RATE'
    TOTAL_SIGNUP = 'TOTAL_SIGNUP'
    TOTAL_SIGNUP_VALUE_IN_MICRO_DOLLAR = 'TOTAL_SIGNUP_VALUE_IN_MICRO_DOLLAR'
    TOTAL_VIDEO_3_SEC_VIEWS = 'TOTAL_VIDEO_3SEC_VIEWS'
    TOTAL_VIDEO_AVG_WATCHTIME_IN_SECOND = 'TOTAL_VIDEO_AVG_WATCHTIME_IN_SECOND'
    TOTAL_VIDEO_MRC_VIEWS = 'TOTAL_VIDEO_MRC_VIEWS'
    TOTAL_VIDEO_P0_COMBINED = 'TOTAL_VIDEO_P0_COMBINED'
    TOTAL_VIDEO_P100_COMPLETE = 'TOTAL_VIDEO_P100_COMPLETE'
    TOTAL_VIDEO_P25_COMBINED = 'TOTAL_VIDEO_P25_COMBINED'
    TOTAL_VIDEO_P50_COMBINED = 'TOTAL_VIDEO_P50_COMBINED'
    TOTAL_VIDEO_P75_COMBINED = 'TOTAL_VIDEO_P75_COMBINED'
    TOTAL_VIDEO_P95_COMBINED = 'TOTAL_VIDEO_P95_COMBINED'
    TOTAL_VIEW_ADD_TO_CART = 'TOTAL_VIEW_ADD_TO_CART'
    TOTAL_VIEW_CHECKOUT = 'TOTAL_VIEW_CHECKOUT'
    TOTAL_VIEW_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_VIEW_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    TOTAL_VIEW_LEAD = 'TOTAL_VIEW_LEAD'
    TOTAL_VIEW_SIGNUP = 'TOTAL_VIEW_SIGNUP'
    TOTAL_VIEW_SIGNUP_VALUE_IN_MICRO_DOLLAR = 'TOTAL_VIEW_SIGNUP_VALUE_IN_MICRO_DOLLAR'
    TOTAL_WEB_CHECKOUT = 'TOTAL_WEB_CHECKOUT'
    TOTAL_WEB_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_WEB_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    TOTAL_WEB_CLICK_CHECKOUT = 'TOTAL_WEB_CLICK_CHECKOUT'
    TOTAL_WEB_CLICK_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_WEB_CLICK_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    TOTAL_WEB_ENGAGEMENT_CHECKOUT = 'TOTAL_WEB_ENGAGEMENT_CHECKOUT'
    TOTAL_WEB_ENGAGEMENT_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_WEB_ENGAGEMENT_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    TOTAL_WEB_SESSIONS = 'TOTAL_WEB_SESSIONS'
    TOTAL_WEB_VIEW_CHECKOUT = 'TOTAL_WEB_VIEW_CHECKOUT'
    TOTAL_WEB_VIEW_CHECKOUT_VALUE_IN_MICRO_DOLLAR = 'TOTAL_WEB_VIEW_CHECKOUT_VALUE_IN_MICRO_DOLLAR'
    VIDEO_3_SEC_VIEWS_2 = 'VIDEO_3SEC_VIEWS_2'
    VIDEO_LENGTH = 'VIDEO_LENGTH'
    VIDEO_MRC_VIEWS_2 = 'VIDEO_MRC_VIEWS_2'
    VIDEO_P0_COMBINED_2 = 'VIDEO_P0_COMBINED_2'
    VIDEO_P100_COMPLETE_2 = 'VIDEO_P100_COMPLETE_2'
    VIDEO_P25_COMBINED_2 = 'VIDEO_P25_COMBINED_2'
    VIDEO_P50_COMBINED_2 = 'VIDEO_P50_COMBINED_2'
    VIDEO_P75_COMBINED_2 = 'VIDEO_P75_COMBINED_2'
    VIDEO_P95_COMBINED_2 = 'VIDEO_P95_COMBINED_2'
    WEB_CHECKOUT_COST_PER_ACTION = 'WEB_CHECKOUT_COST_PER_ACTION'
    WEB_CHECKOUT_ROAS = 'WEB_CHECKOUT_ROAS'
    WEB_SESSIONS_1 = 'WEB_SESSIONS_1'
    WEB_SESSIONS_2 = 'WEB_SESSIONS_2'

class ConversionReportTime(str, Enum):
    r"""The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.."""
    TIME_OF_AD_ACTION = 'TIME_OF_AD_ACTION'
    TIME_OF_CONVERSION = 'TIME_OF_CONVERSION'

class EngagementWindowDays(int, Enum):
    r"""Number of days to use as the conversion attribution window for an engagement action."""
    ZERO = 0
    ONE = 1
    SEVEN = 7
    FOURTEEN = 14
    THIRTY = 30
    SIXTY = 60

class Granularity(str, Enum):
    r"""Chosen granularity for API"""
    TOTAL = 'TOTAL'
    DAY = 'DAY'
    HOUR = 'HOUR'
    WEEK = 'WEEK'
    MONTH = 'MONTH'

class SourcePinterestLevel(str, Enum):
    r"""Chosen level for API"""
    ADVERTISER = 'ADVERTISER'
    ADVERTISER_TARGETING = 'ADVERTISER_TARGETING'
    CAMPAIGN = 'CAMPAIGN'
    CAMPAIGN_TARGETING = 'CAMPAIGN_TARGETING'
    AD_GROUP = 'AD_GROUP'
    AD_GROUP_TARGETING = 'AD_GROUP_TARGETING'
    PIN_PROMOTION = 'PIN_PROMOTION'
    PIN_PROMOTION_TARGETING = 'PIN_PROMOTION_TARGETING'
    KEYWORD = 'KEYWORD'
    PRODUCT_GROUP = 'PRODUCT_GROUP'
    PRODUCT_GROUP_TARGETING = 'PRODUCT_GROUP_TARGETING'
    PRODUCT_ITEM = 'PRODUCT_ITEM'

class ViewWindowDays(int, Enum):
    r"""Number of days to use as the conversion attribution window for a view action."""
    ZERO = 0
    ONE = 1
    SEVEN = 7
    FOURTEEN = 14
    THIRTY = 30
    SIXTY = 60


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ReportConfig:
    r"""Config for custom report"""
    columns: List[SourcePinterestSchemasValidEnums] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('columns') }})
    r"""A list of chosen columns"""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name value of report"""
    attribution_types: Optional[List[SourcePinterestValidEnums]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attribution_types'), 'exclude': lambda f: f is None }})
    r"""List of types of attribution for the conversion report"""
    click_window_days: Optional[ClickWindowDays] = dataclasses.field(default=ClickWindowDays.THIRTY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('click_window_days'), 'exclude': lambda f: f is None }})
    r"""Number of days to use as the conversion attribution window for a pin click action."""
    conversion_report_time: Optional[ConversionReportTime] = dataclasses.field(default=ConversionReportTime.TIME_OF_AD_ACTION, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('conversion_report_time'), 'exclude': lambda f: f is None }})
    r"""The date by which the conversion metrics returned from this endpoint will be reported. There are two dates associated with a conversion event: the date that the user interacted with the ad, and the date that the user completed a conversion event.."""
    engagement_window_days: Optional[EngagementWindowDays] = dataclasses.field(default=EngagementWindowDays.THIRTY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('engagement_window_days'), 'exclude': lambda f: f is None }})
    r"""Number of days to use as the conversion attribution window for an engagement action."""
    granularity: Optional[Granularity] = dataclasses.field(default=Granularity.TOTAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('granularity'), 'exclude': lambda f: f is None }})
    r"""Chosen granularity for API"""
    level: Optional[SourcePinterestLevel] = dataclasses.field(default=SourcePinterestLevel.ADVERTISER, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('level'), 'exclude': lambda f: f is None }})
    r"""Chosen level for API"""
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""A date in the format YYYY-MM-DD. If you have not set a date, it would be defaulted to latest allowed date by report api (913 days from today)."""
    view_window_days: Optional[ViewWindowDays] = dataclasses.field(default=ViewWindowDays.THIRTY, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('view_window_days'), 'exclude': lambda f: f is None }})
    r"""Number of days to use as the conversion attribution window for a view action."""
    


class SourcePinterestPinterest(str, Enum):
    PINTEREST = 'pinterest'

class Status(str, Enum):
    ACTIVE = 'ACTIVE'
    PAUSED = 'PAUSED'
    ARCHIVED = 'ARCHIVED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SourcePinterest:
    UNSET='__SPEAKEASY_UNSET__'
    credentials: Optional[OAuth20] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('credentials'), 'exclude': lambda f: f is None }})
    custom_reports: Optional[List[ReportConfig]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_reports'), 'exclude': lambda f: f is None }})
    r"""A list which contains ad statistics entries, each entry must have a name and can contains fields, breakdowns or action_breakdowns. Click on \\"add\\" to fill this field."""
    SOURCE_TYPE: Final[Optional[SourcePinterestPinterest]] = dataclasses.field(default=SourcePinterestPinterest.PINTEREST, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sourceType'), 'exclude': lambda f: f is None }})
    start_date: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_date'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'exclude': lambda f: f is None }})
    r"""A date in the format YYYY-MM-DD. If you have not set a date, it would be defaulted to latest allowed date by api (89 days from today)."""
    status: Optional[List[Status]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is SourcePinterest.UNSET }})
    r"""For the ads, ad_groups, and campaigns streams, specifying a status will filter out records that do not match the specified ones. If a status is not specified, the source will default to records with a status of either ACTIVE or PAUSED."""
    

