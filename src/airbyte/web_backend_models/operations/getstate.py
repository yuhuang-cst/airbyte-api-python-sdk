"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import connectionstate as shared_connectionstate
from ..shared import invalidinputexceptioninfo as shared_invalidinputexceptioninfo
from ..shared import notfoundknownexceptioninfo as shared_notfoundknownexceptioninfo
from typing import Optional


@dataclasses.dataclass
class GetStateResponse:
    
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    connection_state: Optional[shared_connectionstate.ConnectionState] = dataclasses.field(default=None)
    r"""Successful operation"""
    invalid_input_exception_info: Optional[shared_invalidinputexceptioninfo.InvalidInputExceptionInfo] = dataclasses.field(default=None)
    r"""Input failed validation"""
    not_found_known_exception_info: Optional[shared_notfoundknownexceptioninfo.NotFoundKnownExceptionInfo] = dataclasses.field(default=None)
    r"""Object with given id was not found."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    