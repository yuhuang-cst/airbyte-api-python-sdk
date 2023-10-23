# SourceSnowflakeAuthorizationMethodOAuth20


## Fields

| Field                                                                                                                         | Type                                                                                                                          | Required                                                                                                                      | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `access_token`                                                                                                                | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Access Token for making authenticated requests.                                                                               |
| `auth_type`                                                                                                                   | [SourceSnowflakeAuthorizationMethodOAuth20AuthType](../../models/shared/sourcesnowflakeauthorizationmethodoauth20authtype.md) | :heavy_check_mark:                                                                                                            | N/A                                                                                                                           |
| `client_id`                                                                                                                   | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | The Client ID of your Snowflake developer application.                                                                        |
| `client_secret`                                                                                                               | *str*                                                                                                                         | :heavy_check_mark:                                                                                                            | The Client Secret of your Snowflake developer application.                                                                    |
| `refresh_token`                                                                                                               | *Optional[str]*                                                                                                               | :heavy_minus_sign:                                                                                                            | Refresh Token for making authenticated requests.                                                                              |