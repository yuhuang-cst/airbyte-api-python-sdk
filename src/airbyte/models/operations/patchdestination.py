"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import destinationpatchrequest as shared_destinationpatchrequest
from ...models.shared import destinationresponse as shared_destinationresponse
from typing import Optional


@dataclasses.dataclass
class PatchDestinationRequest:
    destination_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'destinationId', 'style': 'simple', 'explode': False }})
    destination_patch_request: Optional[shared_destinationpatchrequest.DestinationPatchRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    



@dataclasses.dataclass
class PatchDestinationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    destination_response: Optional[shared_destinationresponse.DestinationResponse] = dataclasses.field(default=None)
    r"""Update a Destination"""
    

