# SourceTwilio

The values required to configure the source.


## Fields

| Field                                                                                                   | Type                                                                                                    | Required                                                                                                | Description                                                                                             | Example                                                                                                 |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `account_sid`                                                                                           | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Twilio account SID                                                                                      |                                                                                                         |
| `auth_token`                                                                                            | *str*                                                                                                   | :heavy_check_mark:                                                                                      | Twilio Auth Token.                                                                                      |                                                                                                         |
| `lookback_window`                                                                                       | *Optional[int]*                                                                                         | :heavy_minus_sign:                                                                                      | How far into the past to look for records. (in minutes)                                                 | 60                                                                                                      |
| `source_type`                                                                                           | [SourceTwilioTwilio](../../models/shared/sourcetwiliotwilio.md)                                         | :heavy_check_mark:                                                                                      | N/A                                                                                                     |                                                                                                         |
| `start_date`                                                                                            | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                    | :heavy_check_mark:                                                                                      | UTC date and time in the format 2020-10-01T00:00:00Z. Any data before this date will not be replicated. | 2020-10-01T00:00:00Z                                                                                    |