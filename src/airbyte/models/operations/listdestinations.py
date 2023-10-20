"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import destinationsresponse as shared_destinationsresponse
from typing import List, Optional


@dataclasses.dataclass
class ListDestinationsRequest:
    include_deleted: Optional[bool] = dataclasses.field(default=False, metadata={'query_param': { 'field_name': 'includeDeleted', 'style': 'form', 'explode': True }})
    r"""Include deleted destinations in the returned results."""
    limit: Optional[int] = dataclasses.field(default=20, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Set the limit on the number of destinations returned. The default is 20."""
    offset: Optional[int] = dataclasses.field(default=0, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Set the offset to start at when returning destinations. The default is 0"""
    workspace_ids: Optional[List[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'workspaceIds', 'style': 'form', 'explode': True }})
    r"""The UUIDs of the workspaces you wish to list destinations for. Empty list will retrieve all allowed workspaces."""
    



@dataclasses.dataclass
class ListDestinationsResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    destinations_response: Optional[shared_destinationsresponse.DestinationsResponse] = dataclasses.field(default=None)
    r"""Successful operation"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    r"""Raw HTTP response; suitable for custom response parsing"""
    

