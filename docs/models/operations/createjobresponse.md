# CreateJobResponse


## Fields

| Field                                                                                                | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                       | *str*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `job_response`                                                                                       | [Optional[shared.JobResponse]](../../models/shared/jobresponse.md)                                   | :heavy_minus_sign:                                                                                   | Kicks off a new Job based on the JobType. The connectionId is the resource that Job will be run for. |
| `status_code`                                                                                        | *int*                                                                                                | :heavy_check_mark:                                                                                   | N/A                                                                                                  |
| `raw_response`                                                                                       | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                | :heavy_minus_sign:                                                                                   | N/A                                                                                                  |