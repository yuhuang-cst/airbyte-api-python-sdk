"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
from enum import Enum

class AttemptFailureTypeEnum(str, Enum):
    r"""Categorizes well known errors into types for programmatic handling. If not set, the type of error is not well known."""
    CONFIG_ERROR = 'config_error'
    SYSTEM_ERROR = 'system_error'
    MANUAL_CANCELLATION = 'manual_cancellation'
    REFRESH_SCHEMA = 'refresh_schema'