from dagster import (
    job,
    op,
    schedule,
    DefaultScheduleStatus,
    DagsterRunStatus,
    RunsFilter,
    RunRequest
)

from ..assets.my_asset.asset_1_file import asset_1

@op
def print_asset(some_asset):
    print(some_asset)

@job
def my_job():
    print_asset(asset_1.to_source_asset())

@schedule(
    job=my_job,
    cron_schedule="*/5 * * * *",
    default_status=DefaultScheduleStatus.RUNNING
)
def my_job_schedule(context):
    scheduled_date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    run_records = context.instance.get_run_records(
        RunsFilter(job_name='my_job',
                   statuses=[DagsterRunStatus.STARTED, DagsterRunStatus.STARTING, DagsterRunStatus.QUEUED])
    )

    if len(run_records) == 0:
        return RunRequest(
            run_key=None,
            tags={
                "date": scheduled_date,
                "my_dashboard": "my_job_dashboard",
                "dagster/priority": "1"
            }
        )