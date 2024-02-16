"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import workspaceresponse as shared_workspaceresponse
from typing import Optional


@dataclasses.dataclass
class GetWorkspaceRequest:
    workspace_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspaceId', 'style': 'simple', 'explode': False }})
    



@dataclasses.dataclass
class GetWorkspaceResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    workspace_response: Optional[shared_workspaceresponse.WorkspaceResponse] = dataclasses.field(default=None)
    r"""Get a Workspace by the id in the path."""
    

