# SourceMongodb

The values required to configure the source.


## Fields

| Field                                                                                                    | Type                                                                                                     | Required                                                                                                 | Description                                                                                              | Example                                                                                                  |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `auth_source`                                                                                            | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | The authentication source where the user information is stored.                                          | admin                                                                                                    |
| `database`                                                                                               | *str*                                                                                                    | :heavy_check_mark:                                                                                       | The database you want to replicate.                                                                      |                                                                                                          |
| `instance_type`                                                                                          | *Optional[Any]*                                                                                          | :heavy_minus_sign:                                                                                       | The MongoDb instance to connect to. For MongoDB Atlas and Replica Set TLS connection is used by default. |                                                                                                          |
| `password`                                                                                               | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | The password associated with this username.                                                              |                                                                                                          |
| `source_type`                                                                                            | [SourceMongodbMongodb](../../models/shared/sourcemongodbmongodb.md)                                      | :heavy_check_mark:                                                                                       | N/A                                                                                                      |                                                                                                          |
| `user`                                                                                                   | *Optional[str]*                                                                                          | :heavy_minus_sign:                                                                                       | The username which is used to access the database.                                                       |                                                                                                          |