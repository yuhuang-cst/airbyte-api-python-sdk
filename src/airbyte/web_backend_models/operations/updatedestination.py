"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationread as shared_destinationread
from ..shared import invalidinputexceptioninfo as shared_invalidinputexceptioninfo
from typing import Optional


@dataclasses.dataclass
class UpdateDestinationResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    destination_read: Optional[shared_destinationread.DestinationRead] = dataclasses.field(default=None)
    r"""Successful operation"""
    invalid_input_exception_info: Optional[shared_invalidinputexceptioninfo.InvalidInputExceptionInfo] = dataclasses.field(default=None)
    r"""Input failed validation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    