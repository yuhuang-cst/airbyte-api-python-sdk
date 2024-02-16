"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

# from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import jobresponse as shared_jobresponse
from typing import Optional


@dataclasses.dataclass
class CreateJobResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    job_response: Optional[shared_jobresponse.JobResponse] = dataclasses.field(default=None)
    r"""Kicks off a new Job based on the JobType. The connectionId is the resource that Job will be run for."""
    

