# SourceOrb

The values required to configure the source.


## Fields

| Field                                                                                                                                                                                         | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   | Example                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_key`                                                                                                                                                                                     | *str*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | Orb API Key, issued from the Orb admin console.                                                                                                                                               |                                                                                                                                                                                               |
| `lookback_window_days`                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | When set to N, the connector will always refresh resources created within the past N days. By default, updated objects that are not newly created are not incrementally synced.               |                                                                                                                                                                                               |
| `numeric_event_properties_keys`                                                                                                                                                               | list[*str*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                            | Property key names to extract from all events, in order to enrich ledger entries corresponding to an event deduction.                                                                         |                                                                                                                                                                                               |
| `plan_id`                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Orb Plan ID to filter subscriptions that should have usage fetched.                                                                                                                           |                                                                                                                                                                                               |
| `source_type`                                                                                                                                                                                 | [SourceOrbOrb](../../models/shared/sourceorborb.md)                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                            | N/A                                                                                                                                                                                           |                                                                                                                                                                                               |
| `start_date`                                                                                                                                                                                  | *str*                                                                                                                                                                                         | :heavy_check_mark:                                                                                                                                                                            | UTC date and time in the format 2022-03-01T00:00:00Z. Any data with created_at before this data will not be synced. For Subscription Usage, this becomes the `timeframe_start` API parameter. | 2022-03-01T00:00:00Z                                                                                                                                                                          |
| `string_event_properties_keys`                                                                                                                                                                | list[*str*]                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                            | Property key names to extract from all events, in order to enrich ledger entries corresponding to an event deduction.                                                                         |                                                                                                                                                                                               |
| `subscription_usage_grouping_key`                                                                                                                                                             | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | Property key name to group subscription usage by.                                                                                                                                             |                                                                                                                                                                                               |