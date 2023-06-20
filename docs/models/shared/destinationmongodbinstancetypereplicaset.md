# DestinationMongodbInstanceTypeReplicaSet

MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default.


## Fields

| Field                                                                                                                       | Type                                                                                                                        | Required                                                                                                                    | Description                                                                                                                 | Example                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `instance`                                                                                                                  | [DestinationMongodbInstanceTypeReplicaSetInstance](../../models/shared/destinationmongodbinstancetypereplicasetinstance.md) | :heavy_check_mark:                                                                                                          | N/A                                                                                                                         |                                                                                                                             |
| `replica_set`                                                                                                               | *Optional[str]*                                                                                                             | :heavy_minus_sign:                                                                                                          | A replica set name.                                                                                                         |                                                                                                                             |
| `server_addresses`                                                                                                          | *str*                                                                                                                       | :heavy_check_mark:                                                                                                          | The members of a replica set. Please specify `host`:`port` of each member seperated by comma.                               | host1:27017,host2:27017,host3:27017                                                                                         |