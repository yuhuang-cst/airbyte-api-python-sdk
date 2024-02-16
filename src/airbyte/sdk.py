"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .connections import Connections
from .destinations import Destinations
from .jobs import Jobs
from .sdkconfiguration import SDKConfiguration
from .sources import Sources
from .streams import Streams
from .workspaces import Workspaces
from airbyte.web_backend import WebBackend
from airbyte import utils
from airbyte.models import shared
from typing import Callable, Dict, Union

class Airbyte:
    r"""airbyte-api: Programatically control Airbyte Cloud, OSS & Enterprise."""
    connections: Connections
    destinations: Destinations
    jobs: Jobs
    sources: Sources
    streams: Streams
    workspaces: Workspaces

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: Union[shared.Security,Callable[[], shared.Security]] = None,
                 server_idx: int = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None,
                 airbyte_wb_server_url: str = None,
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: Union[shared.Security,Callable[[], shared.Security]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)

        self.sdk_configuration = SDKConfiguration(
            client, security, server_url, server_idx, retry_config=retry_config,
            airbyte_wb_server_url=airbyte_wb_server_url)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.connections = Connections(self.sdk_configuration)
        self.destinations = Destinations(self.sdk_configuration)
        self.jobs = Jobs(self.sdk_configuration)
        self.sources = Sources(self.sdk_configuration)
        self.streams = Streams(self.sdk_configuration)
        self.workspaces = Workspaces(self.sdk_configuration)
        self.init_web_backend()


    def init_web_backend(self):
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)

        self.web_backend = WebBackend(
            client,
            client,
            self.sdk_configuration.airbyte_wb_server_url,
            self.sdk_configuration.language,
            self.sdk_configuration.sdk_version,
            self.sdk_configuration.gen_version,
        )
    