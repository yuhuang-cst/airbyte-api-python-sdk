# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Yu Huang
# @Email: yuhuang-cst@foxmail.com

import os
import json
import airbyte
from airbyte.models import shared
from airbyte.web_backend_models import shared as wb_shared

# Note: 'from __future__ import annotations' in the airbyte package should all be deleted in order to use '__type' when deserializing
# Ref: https://github.com/lidatong/dataclasses-json/issues/458

WORKSPACE_ID = "5f24949b-5fa7-486c-ba25-6c859de7c1d0"

def test_readme_create_connection(s):
    req = shared.ConnectionCreateRequest(
        destination_id='e41ebed7-48d5-460a-8dab-af680bad91c1',
        source_id='af801f7c-af49-4d99-84e6-323355c87009',
        namespace_definition=shared.NamespaceDefinitionEnum.DESTINATION,
        name='test-py-api2',
        configurations=shared.StreamConfigurations(streams=[shared.StreamConfiguration(
            name='v20231031_ods_ae',
            sync_mode=shared.ConnectionSyncModeEnum.FULL_REFRESH_OVERWRITE
        )]),
        schedule=shared.ConnectionSchedule(schedule_type=shared.ScheduleTypeEnum.MANUAL)
    )

    res = s.connections.create_connection(req)

    if res.connection_response is not None:
        print('res', res)


def create_source(s, scp_config):
    # req = shared.SourceCreateRequest(
    #     configuration=shared.SourceFile(
    #         dataset_name='v20231031_ods_ae',
    #         format=shared.FileFormat.CSV,
    #         url='/home/yuhuang/download/henlius_hlx11/v20231031/ae.CSV',
    #         provider=shared.SCPSecureCopyProtocol(
    #             host=scp_config["HOST"],
    #             user=scp_config["USER"],
    #             password=scp_config["PASSWORD"]
    #         ),
    #     ),
    #     name="henlius_hlx11_v20231031_ae_csv_py_api_manual_id",
    #     workspace_id=WORKSPACE_ID,
    # )
    # print('req1', req.to_json())

    req_dict = {
        "configuration": {
            "__type": "SourceFile",
            "sourceType": "file",
            "dataset_name": "v20231031_ods_ae",
            "provider": {
                "__type": "SCPSecureCopyProtocol",
                "storage": "SCP",
                "host": scp_config["HOST"],
                "user": scp_config["USER"],
                "password": scp_config["PASSWORD"],
                "port": "22",
            },
            "url": "/home/yuhuang/download/henlius_hlx11/v20231031/ae.CSV",
            "format": "csv",
        },
        "name": "henlius_hlx11_v20231031_ae_csv_py_api_schema_load",
        "workspaceId": "5f24949b-5fa7-486c-ba25-6c859de7c1d0",
    }
    req = shared.SourceCreateRequest.schema().load(req_dict)
    # req = shared.SourceCreateRequest.from_dict(req_dict) # Note: fail to load
    print('req2 obj', req)
    res = s.sources.create_source(req)
    print('res', res)
    print('source_id:', res.source_response.source_id)


def create_destination(s, db_config):
    req = shared.DestinationCreateRequest(
        configuration=shared.DestinationClickhouse(
            database=db_config["DATABASE"],
            host=db_config["HOST"],
            port=db_config["PORT"],
            username=db_config["USER_NAME"],
            password=db_config["PASSWORD"],
            tunnel_method=shared.NoTunnel(
                TUNNEL_METHOD=shared.TunnelMethod.NO_TUNNEL
            ),
            ssl=False,
        ),
        name="henlius_hlx11_clickhouse",
        workspace_id=WORKSPACE_ID,
    )
    print(req.to_json())
    res = s.destinations.create_destination(req)
    print('res', res)


def test_web_backend_create_connection(s):
    req = wb_shared.WebBackendConnectionCreate(
        destination_id='e41ebed7-48d5-460a-8dab-af680bad91c1',
        source_id='af801f7c-af49-4d99-84e6-323355c87009',
        status=wb_shared.shared_connectionstatus_enum.ConnectionStatusEnum.ACTIVE,
        schedule_type=wb_shared.shared_connectionscheduletype_enum.ConnectionScheduleTypeEnum.MANUAL,
        namespace_definition=wb_shared.shared_namespacedefinitiontype_enum.NamespaceDefinitionTypeEnum.DESTINATION,
        name='test-py-api-web-backend2',
        sync_catalog=wb_shared.shared_airbytecatalog.AirbyteCatalog(
            streams=[wb_shared.shared_airbytestreamandconfiguration.AirbyteStreamAndConfiguration(
                stream=wb_shared.shared_airbytestream.AirbyteStream(
                    name='v20231031_ods_ae',
                    supported_sync_modes=[wb_shared.shared_syncmode_enum.SyncModeEnum.FULL_REFRESH],
                ),
                config=wb_shared.shared_airbytestreamconfiguration.AirbyteStreamConfiguration(
                    destination_sync_mode=wb_shared.shared_destinationsyncmode_enum.DestinationSyncModeEnum.OVERWRITE,
                    sync_mode=wb_shared.shared_syncmode_enum.SyncModeEnum.FULL_REFRESH,
                    alias_name='v20231031_ods_ae',
                    selected=True, # must contain
                ),
            )]
        ),
        operations=[wb_shared.shared_operationcreate.OperationCreate(
            name='Normalization',
            workspace_id=WORKSPACE_ID,
            operator_configuration=wb_shared.shared_operatorconfiguration.OperatorConfiguration(
                operator_type=wb_shared.shared_operatortype_enum.OperatorTypeEnum.NORMALIZATION,
                normalization=wb_shared.shared_operatornormalization.OperatorNormalization(
                    option=wb_shared.shared_operatornormalization.OperatorNormalizationOptionEnum.BASIC
                )
            )
        )]
    )
    print('req', req.to_json())
    res = s.web_backend.web_backend_create_connection(req)

    if res.raw_response is not None:
        print('res', res)
        print('res.raw_response', type(res.raw_response), res.raw_response)


if __name__ == '__main__':
    TEST_PATH = os.path.dirname(os.path.realpath(__file__))
    config = json.load(open(os.path.join(TEST_PATH, 'wilddata.json')))
    server_url = 'http://111.229.107.107:8006/v1' # normal api
    # server_url = 'http://111.229.107.107:8000/api' # web backend

    s = airbyte.Airbyte(
        server_url=server_url,
        security=shared.Security(
            basic_auth=shared.SchemeBasicAuth(
                username=config["USER_NAME"],
                password=config["PASSWORD"],
            ),
        ),
    )
    create_source(s, scp_config=json.load(open(os.path.join(TEST_PATH, 'scp.json'))))
    # create_destination(s, db_config=json.load(open(os.path.join(TEST_PATH, 'clickhouse.json'))))
    # test_readme_create_connection(s)

    # test_web_backend_create_connection(s) # web backend



