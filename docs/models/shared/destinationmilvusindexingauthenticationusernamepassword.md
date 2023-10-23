# DestinationMilvusIndexingAuthenticationUsernamePassword

Authenticate using username and password (suitable for self-managed Milvus clusters)


## Fields

| Field                                                                                                                                                       | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `mode`                                                                                                                                                      | [Optional[DestinationMilvusIndexingAuthenticationUsernamePasswordMode]](../../models/shared/destinationmilvusindexingauthenticationusernamepasswordmode.md) | :heavy_minus_sign:                                                                                                                                          | N/A                                                                                                                                                         |
| `password`                                                                                                                                                  | *str*                                                                                                                                                       | :heavy_check_mark:                                                                                                                                          | Password for the Milvus instance                                                                                                                            |
| `username`                                                                                                                                                  | *str*                                                                                                                                                       | :heavy_check_mark:                                                                                                                                          | Username for the Milvus instance                                                                                                                            |